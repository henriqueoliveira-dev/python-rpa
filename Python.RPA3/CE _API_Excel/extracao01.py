
import http.client
import json

def obter_endereco_por_cep(cep):

    conexao = http.client.HTTPConnection("viacep.com.br")

    conexao.request('GET', f"/ws/{cep}/json/")

    resposta = conexao.getresponse()

    dados = resposta.read()

    endereco = json.loads(dados.decode('utf-8'))

    if 'erro' not in endereco:
        return endereco
    else:
        return 'CEP não encontrado.'

    conexao.close()


#cep_exemplo = '01001000'

cep_exemplo = input("Digite o CEP que deseja consultar: ")

endereco_resultado = obter_endereco_por_cep(cep_exemplo)

print(endereco_resultado)
