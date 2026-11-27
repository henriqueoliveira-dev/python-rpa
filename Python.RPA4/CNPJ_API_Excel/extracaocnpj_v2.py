
import http.client
import json
import pandas as pd


def obter_dados_empresa_por_cnpj(cnpj):

    conexao = http.client.HTTPSConnection("www.receitaws.com.br")

    conexao.request("GET", f"/v1/cnpj/{cnpj}")

    resposta = conexao.getresponse()

    print(f"Status da Resposta HTTP: {resposta.status}")

    if resposta.status != 200:
        conexao.close()
        return {
            "status": "ERROR",
            "message": f"Resposta HTTP com status {resposta.status}"
        }

    dados = resposta.read()

    conexao.close()

    try:
        empresa = json.loads(dados.decode("utf-8"))

        print(f"Empresa decodificada: {empresa}")

        return empresa

    except json.JSONDecodeError as e:

        print(f"Erro na decodificação do JSON: {str(e)}")

        return {
            "status": "ERROR",
            "message": "Erro na decodificação do JSON."
        }


def tratar_dados_aninhados(dados):

    if "atividade_principal" in dados:
        dados["atividade_principal"] = "; ".join(
            ativ["text"] for ativ in dados["atividade_principal"]
        )

    if "atividades_secundarias" in dados:
        dados["atividades_secundarias"] = "; ".join(
            ativ["text"] for ativ in dados["atividades_secundarias"]
        )

    if "qsa" in dados:
        dados["qsa"] = "; ".join(
            f"{q['nome']} - {q.get('qual', '')}"
            for q in dados["qsa"]
        )

    if "extra" in dados:
        dados["extra"] = str(dados["extra"])

    if "simples" in dados:
        dados["simples"] = str(dados["simples"])

    if "simei" in dados:
        dados["simei"] = str(dados["simei"])

    if "billing" in dados:
        dados["billing"] = str(dados["billing"])

    return dados

    
def salvar_dados_empresa_excel(dados_empresa, nome_arquivo="dados_empresa.xlsx"):

    if dados_empresa.get("status") == "ERROR":
        print(dados_empresa.get("message", "Erro desconhecido."))
        return

    dados_empresa = tratar_dados_aninhados(dados_empresa)

    dataframe = pd.DataFrame([dados_empresa])

    dataframe.to_excel(
        r"C:\Users\Henrique Oliveira\OneDrive\Documentos\Projeto-RPA\dados_empresa.xlsx",
        index=False
    )

    print(f"Dados da empresa salvos com sucesso em: {nome_arquivo}")

cnpj_exemplo = "33157312000162"

dados_empresa = obter_dados_empresa_por_cnpj(cnpj_exemplo)

salvar_dados_empresa_excel(dados_empresa)
