import http.client
import json
import re
from pathlib import Path

import pandas as pd


def limpar_cnpj(cnpj):
    valor = str(cnpj).strip()
    if valor.endswith(".0"):
        valor = valor[:-2]
    digitos = re.sub(r"\D", "", valor)
    if len(digitos) > 14 or not digitos:
        raise ValueError(f"CNPJ inválido: {cnpj}")
    return digitos.zfill(14)


def obter_dados_empresa_por_cnpj(cnpj):
    cnpj = limpar_cnpj(cnpj)
    conexao = http.client.HTTPSConnection("www.receitaws.com.br", timeout=15)
    try:
        conexao.request("GET", f"/v1/cnpj/{cnpj}")
        resposta = conexao.getresponse()
        if resposta.status != 200:
            print(f"CNPJ {cnpj}: resposta HTTP {resposta.status}.")
            return None
        empresa = json.loads(resposta.read().decode("utf-8"))
        if not isinstance(empresa, dict) or empresa.get("status") == "ERROR":
            mensagem = empresa.get("message", "Resposta inválida.") if isinstance(empresa, dict) else "Resposta inválida."
            print(f"Erro ao consultar CNPJ {cnpj}: {mensagem}")
            return None
        return empresa
    except (OSError, http.client.HTTPException, json.JSONDecodeError) as erro:
        print(f"Erro na consulta do CNPJ {cnpj}: {erro}")
        return None
    finally:
        conexao.close()


def tratar_dados_empresa(dados):
    atividade = dados.get("atividade_principal") or []
    if not isinstance(atividade, list):
        atividade = []
    atividade_principal = "; ".join(
        str(item.get("text", "")) for item in atividade if isinstance(item, dict)
    )
    return {
        "cnpj": dados.get("cnpj", ""),
        "nome": dados.get("nome", ""),
        "telefone": dados.get("telefone", ""),
        "email": dados.get("email", ""),
        "logradouro": dados.get("logradouro", ""),
        "bairro": dados.get("bairro", ""),
        "municipio": dados.get("municipio", ""),
        "uf": dados.get("uf", ""),
        "cep": dados.get("cep", ""),
        "atividade_principal": atividade_principal,
    }


def processar_planilha(caminho_planilha):
    caminho_planilha = Path(caminho_planilha).expanduser()
    planilha_cnpjs = pd.read_excel(caminho_planilha, sheet_name="CNPJ", dtype={"CNPJ": str})
    if "CNPJ" not in planilha_cnpjs.columns:
        raise ValueError("A aba 'CNPJ' precisa conter uma coluna chamada 'CNPJ'.")

    resultados = []
    for cnpj in planilha_cnpjs["CNPJ"].dropna():
        print(f"\nLendo CNPJ: {cnpj}")
        try:
            dados_empresa = obter_dados_empresa_por_cnpj(cnpj)
        except ValueError as erro:
            print(erro)
            continue
        if dados_empresa:
            resultados.append(tratar_dados_empresa(dados_empresa))
            print(f"CNPJ {cnpj} consultado com sucesso!")
        else:
            print(f"Não foi possível consultar o CNPJ {cnpj}.")

    with pd.ExcelWriter(
        caminho_planilha,
        engine="openpyxl",
        mode="a",
        if_sheet_exists="replace",
    ) as escritor:
        pd.DataFrame(resultados).to_excel(escritor, sheet_name="Dados", index=False)
    print("Consulta finalizada. Resultados gravados na aba 'Dados'.")


def main():
    caminho_planilha = Path(__file__).with_name("CNPJ.xlsx")
    try:
        processar_planilha(caminho_planilha)
    except (OSError, ValueError, KeyError, ImportError) as erro:
        print(f"Não foi possível processar a planilha {caminho_planilha}: {erro}")


if __name__ == "__main__":
    main()
