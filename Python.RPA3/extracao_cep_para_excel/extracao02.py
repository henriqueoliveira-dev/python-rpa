import http.client
import json
import re
from pathlib import Path

import pandas as pd


def obter_endereco_por_cep(cep):
    digitos = re.sub(r"\D", "", str(cep))
    if len(digitos) != 8:
        raise ValueError("O CEP deve conter exatamente 8 dígitos.")
    conexao = http.client.HTTPSConnection("viacep.com.br", timeout=10)
    try:
        conexao.request("GET", f"/ws/{digitos}/json/")
        resposta = conexao.getresponse()
        if resposta.status != 200:
            raise RuntimeError(f"A API ViaCEP respondeu com HTTP {resposta.status}.")
        endereco = json.loads(resposta.read().decode("utf-8"))
        if not isinstance(endereco, dict):
            raise RuntimeError("A resposta da API ViaCEP não tem o formato esperado.")
        return None if "erro" in endereco else endereco
    finally:
        conexao.close()


def salvar_endereco_excel(endereco, nome_arquivo="endereco.xlsx"):
    if endereco is None:
        print("Não foi possível salvar os dados: CEP não encontrado.")
        return False
    caminho = Path(nome_arquivo).expanduser()
    caminho.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame([endereco]).to_excel(caminho, index=False)
    print(f"Dados salvos com sucesso no arquivo {caminho}")
    return True


def main():
    cep = input("Digite o CEP que deseja consultar: ")
    try:
        endereco = obter_endereco_por_cep(cep)
        salvar_endereco_excel(endereco)
    except (ValueError, OSError, http.client.HTTPException, RuntimeError, json.JSONDecodeError) as erro:
        print(f"Não foi possível processar o CEP: {erro}")


if __name__ == "__main__":
    main()
