import http.client
import json
import re
from pathlib import Path

import pandas as pd


def limpar_cnpj(cnpj):
    digitos = re.sub(r"\D", "", str(cnpj))
    if len(digitos) != 14:
        raise ValueError("O CNPJ deve conter exatamente 14 dígitos.")
    return digitos


def obter_dados_empresa_por_cnpj(cnpj):
    cnpj = limpar_cnpj(cnpj)
    conexao = http.client.HTTPSConnection("www.receitaws.com.br", timeout=15)
    try:
        conexao.request("GET", f"/v1/cnpj/{cnpj}")
        resposta = conexao.getresponse()
        if resposta.status != 200:
            return {"status": "ERROR", "message": f"Resposta HTTP {resposta.status}."}
        empresa = json.loads(resposta.read().decode("utf-8"))
        if not isinstance(empresa, dict):
            return {"status": "ERROR", "message": "Resposta da API em formato inesperado."}
        return empresa
    except (OSError, http.client.HTTPException, json.JSONDecodeError) as erro:
        return {"status": "ERROR", "message": f"Falha na consulta: {erro}"}
    finally:
        conexao.close()


def tratar_dados_aninhados(dados):
    dados = dict(dados)
    for campo in ("atividade_principal", "atividades_secundarias"):
        itens = dados.get(campo)
        if isinstance(itens, list):
            dados[campo] = "; ".join(
                str(item.get("text", "")) for item in itens if isinstance(item, dict)
            )
    qsa = dados.get("qsa")
    if isinstance(qsa, list):
        dados["qsa"] = "; ".join(
            f"{item.get('nome', '')} - {item.get('qual', '')}"
            for item in qsa if isinstance(item, dict)
        )
    for campo in ("extra", "simples", "simei", "billing"):
        if isinstance(dados.get(campo), (dict, list)):
            dados[campo] = json.dumps(dados[campo], ensure_ascii=False)
    return dados


def salvar_dados_empresa_excel(dados_empresa, nome_arquivo="dados_empresa.xlsx"):
    if dados_empresa.get("status") == "ERROR":
        print(dados_empresa.get("message", "Erro desconhecido."))
        return False
    caminho = Path(nome_arquivo).expanduser()
    caminho.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([tratar_dados_aninhados(dados_empresa)]).to_excel(caminho, index=False)
    print(f"Dados da empresa salvos com sucesso em: {caminho}")
    return True


def main():
    cnpj_exemplo = "33157312000162"
    try:
        dados_empresa = obter_dados_empresa_por_cnpj(cnpj_exemplo)
        salvar_dados_empresa_excel(dados_empresa)
    except (ValueError, OSError) as erro:
        print(f"Não foi possível processar o CNPJ: {erro}")


if __name__ == "__main__":
    main()
