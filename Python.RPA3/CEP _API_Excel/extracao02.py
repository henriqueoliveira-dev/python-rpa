
import http.client
import json
import pandas as pd


def obter_endereco_por_cep(cep):

    conexao = http.client.HTTPConnection('viacep.com.br')

    conexao.request("GET", f"/ws/{cep}/json/")

    resposta = conexao.getresponse()

    dados = resposta.read()

    endereco = json.loads(dados.decode('utf-8'))

    conexao.close()

    return endereco


def salvar_endereco_excel(endereco, nome_arquivo="endereco.xlsx"):

    if 'erro' not in endereco:

        df = pd.DataFrame([endereco])

        df.to_excel(
    r'C:\Users\Henrique Oliveira\OneDrive\Documentos\Projeto-RPA\endereco.xlsx',
    index=False
)

        print(f"Dados salvos com sucesso no arquivo {nome_arquivo}")

    else:

        print("Não foi possível salvar os dados: CEP não encontrado.")


cep_exemplo = input("Digite o CEP que deseja consultar: ")

cep_exemplo = cep_exemplo.replace("-", "").strip()

endereco_resultado = obter_endereco_por_cep(cep_exemplo)

salvar_endereco_excel(endereco_resultado)
