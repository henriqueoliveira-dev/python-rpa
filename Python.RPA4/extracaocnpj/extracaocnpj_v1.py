import http.client
import json
import re


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
        corpo = resposta.read()
        if resposta.status != 200:
            return {"status": "ERROR", "message": f"Resposta HTTP {resposta.status}."}
        empresa = json.loads(corpo.decode("utf-8"))
        if not isinstance(empresa, dict):
            return {"status": "ERROR", "message": "Resposta da API em formato inesperado."}
        return empresa
    except (OSError, http.client.HTTPException, json.JSONDecodeError) as erro:
        return {"status": "ERROR", "message": f"Falha na consulta: {erro}"}
    finally:
        conexao.close()


def main():
    cnpj_exemplo = "33157312000162"
    try:
        dados_empresa = obter_dados_empresa_por_cnpj(cnpj_exemplo)
    except ValueError as erro:
        print(erro)
        return
    print(dados_empresa.get("message") if dados_empresa.get("status") == "ERROR" else dados_empresa)


if __name__ == "__main__":
    main()
