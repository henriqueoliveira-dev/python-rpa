
import http.client
import json
import pandas as pd

# FUNÇÃO PARA CONSULTAR O CEP NA API VIACEP
def obter_endereco_por_cep(cep):

    conexao = http.client.HTTPConnection('viacep.com.br')

    conexao.request("GET", f"/ws/{cep}/json/")

    resposta = conexao.getresponse()

    if resposta.status != 200:
        conexao.close()
        return None

    dados = resposta.read()

    endereco = json.loads(dados.decode('utf-8'))

    conexao.close()

    return endereco if "erro" not in endereco else None


# CAMINHO DA PLANILHA EXCEL
caminho_planilha = r'C:\Users\Henrique Oliveira\OneDrive\Documentos\Projeto-RPA\CEP.xlsx'


# LER A ABA CEP
planilha_ceps = pd.read_excel(
    caminho_planilha,
    sheet_name='CEP'
)


# OBTER OS CEPS DA COLUNA CEP
ceps = planilha_ceps['CEP'].dropna()


# CRIAR DATAFRAME PARA ARMAZENAR OS RESULTADOS
resultados = pd.DataFrame(
    columns=['CEP', 'Logradouro', 'Bairro', 'Localidade', 'UF']
)


# PERCORRER TODOS OS CEPS
for cep in ceps:

    cep = str(cep).replace('-', '').replace('.', '').strip()

    # CONSULTAR O ENDEREÇO
    endereco = obter_endereco_por_cep(cep)

    if endereco:

        nova_linha = pd.DataFrame([{

            'CEP': endereco.get('cep', ''),
            'Logradouro': endereco.get('logradouro', ''),
            'Bairro': endereco.get('bairro', ''),
            'Localidade': endereco.get('localidade', ''),
            'UF': endereco.get('uf', '')

        }])

        # ADICIONAR O ENDEREÇO AO DATAFRAME
        resultados = pd.concat(
            [resultados, nova_linha],
            ignore_index=True
        )

        print(f"CEP {cep} consultado com sucesso!")

    else:

        print(f"CEP {cep} não encontrado!")


# SALVAR OS RESULTADOS NA MESMA PLANILHA
with pd.ExcelWriter(
    caminho_planilha,
    engine='openpyxl',
    mode='a',
    if_sheet_exists='replace'
) as writer:

    resultados.to_excel(
        writer,
        sheet_name='Dados',
        index=False
    )


print("Endereços salvos com sucesso na aba 'Dados' da planilha CEP.xlsx!")
