import http.client
import json
import re
from pathlib import Path

import pandas as pd


def normalizar_cep(cep):
    valor = str(cep).strip()
    if valor.endswith(".0"):
        valor = valor[:-2]
    digitos = re.sub(r"\D", "", valor)
    if len(digitos) > 8 or not digitos:
        raise ValueError(f"CEP inválido: {cep}")
    return digitos.zfill(8)


def obter_endereco_por_cep(cep):
    cep = normalizar_cep(cep)
    conexao = http.client.HTTPSConnection("viacep.com.br", timeout=10)
    try:
        conexao.request("GET", f"/ws/{cep}/json/")
        resposta = conexao.getresponse()
        if resposta.status != 200:
            raise RuntimeError(f"HTTP {resposta.status}")
        endereco = json.loads(resposta.read().decode("utf-8"))
        if not isinstance(endereco, dict):
            raise RuntimeError("Resposta da API em formato inesperado")
        return None if "erro" in endereco else endereco
    finally:
        conexao.close()


def consultar_planilha(caminho_planilha):
    caminho_planilha = Path(caminho_planilha).expanduser()
    planilha_ceps = pd.read_excel(caminho_planilha, sheet_name="CEP", dtype={"CEP": str})
    if "CEP" not in planilha_ceps.columns:
        raise ValueError("A aba 'CEP' precisa conter uma coluna chamada 'CEP'.")

    resultados = []
    for cep in planilha_ceps["CEP"].dropna():
        try:
            cep_normalizado = normalizar_cep(cep)
            endereco = obter_endereco_por_cep(cep_normalizado)
        except (ValueError, OSError, http.client.HTTPException, RuntimeError, json.JSONDecodeError) as erro:
            print(f"CEP {cep} não consultado: {erro}")
            continue
        if endereco is None:
            print(f"CEP {cep_normalizado} não encontrado!")
            continue
        resultados.append({
            "CEP": endereco.get("cep", cep_normalizado),
            "Logradouro": endereco.get("logradouro", ""),
            "Bairro": endereco.get("bairro", ""),
            "Localidade": endereco.get("localidade", ""),
            "UF": endereco.get("uf", ""),
        })
        print(f"CEP {cep_normalizado} consultado com sucesso!")

    with pd.ExcelWriter(
        caminho_planilha,
        engine="openpyxl",
        mode="a",
        if_sheet_exists="replace",
    ) as writer:
        pd.DataFrame(resultados, columns=["CEP", "Logradouro", "Bairro", "Localidade", "UF"]).to_excel(
            writer, sheet_name="Dados", index=False
        )
    print("Endereços salvos com sucesso na aba 'Dados'.")


def main():
    caminho_padrao = Path(__file__).with_name("CEP.xlsx")
    try:
        consultar_planilha(caminho_padrao)
    except (OSError, ValueError, KeyError, ImportError) as erro:
        print(f"Não foi possível processar a planilha {caminho_padrao}: {erro}")


if __name__ == "__main__":
    main()
