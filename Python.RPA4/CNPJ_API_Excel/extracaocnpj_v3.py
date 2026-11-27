
import http.client
import json
import pandas as pd


def limpar_cnpj(cnpj):

    return ''.join(filter(str.isdigit, str(cnpj)))


def obter_dados_empresa_por_cnpj(cnpj):

    cnpj = limpar_cnpj(cnpj)

    conexao = http.client.HTTPSConnection("www.receitaws.com.br")

    try:

        conexao.request("GET", f"/v1/cnpj/{cnpj}")

        resposta = conexao.getresponse()

        print(f"Processando CNPJ {cnpj}: Status {resposta.status}")

        if resposta.status != 200:
            return None

        dados = resposta.read()

        empresa = json.loads(dados.decode("utf-8"))

        if empresa.get("status") == "ERROR":

            print(
                f"Erro ao consultar CNPJ {cnpj}: "
                f"{empresa.get('message', 'Erro desconhecido')}"
            )

            return None

        return empresa

    except (OSError, json.JSONDecodeError) as erro:

        print(f"Erro na consulta do CNPJ {cnpj}: {erro}")

        return None

    finally:

        conexao.close()


def tratar_dados_empresa(dados):

    atividade = dados.get("atividade_principal", [])

    if atividade:
        atividade_principal = "; ".join(
            item.get("text", "") for item in atividade
        )
    else:
        atividade_principal = ""

    empresa = {

        "cnpj": dados.get("cnpj", ""),
        "nome": dados.get("nome", ""),
        "telefone": dados.get("telefone", ""),
        "email": dados.get("email", ""),
        "logradouro": dados.get("logradouro", ""),
        "bairro": dados.get("bairro", ""),
        "municipio": dados.get("municipio", ""),
        "uf": dados.get("uf", ""),
        "cep": dados.get("cep", ""),
        "atividade_principal": atividade_principal

    }

    return empresa


# Caminho da planilha de entrada e saída
caminho_planilha = r"C:\Users\Henrique Oliveira\OneDrive\Documentos\Projeto-RPA\CNPJ.xlsx"


# Leitura da aba de entrada
planilha_cnpjs = pd.read_excel(
    caminho_planilha,
    sheet_name="CNPJ",
    dtype={"CNPJ": str}
)


# Lista para armazenar os dados das empresas
resultados = []


# Percorrendo todos os CNPJs da planilha
for cnpj in planilha_cnpjs["CNPJ"].dropna():

    print(f"\nLendo CNPJ: {cnpj}")

    dados_empresa = obter_dados_empresa_por_cnpj(cnpj)

    if dados_empresa:

        empresa_tratada = tratar_dados_empresa(dados_empresa)

        resultados.append(empresa_tratada)

        print(f"CNPJ {cnpj} consultado com sucesso!")

    else:

        print(f"Não foi possível consultar o CNPJ {cnpj}.")


# Criando a tabela de resultados
if resultados:

    dataframe = pd.DataFrame(resultados)

    # Gravando os resultados na segunda aba
    with pd.ExcelWriter(
        caminho_planilha,
        engine="openpyxl",
        mode="a",
        if_sheet_exists="replace"
    ) as escritor:

        dataframe.to_excel(
            escritor,
            sheet_name="Dados",
            index=False
        )

    print("\nConsulta finalizada!")
    print("Dados salvos na aba 'Dados' da planilha CNPJ.xlsx.")

else:

    print("\nNenhum resultado válido foi encontrado.")
