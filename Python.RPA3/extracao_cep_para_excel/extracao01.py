import http.client
import json
import re


def normalizar_cep(cep):
    """Retorna os oito dígitos do CEP ou levanta ValueError."""
    digitos = re.sub(r"\D", "", str(cep))
    if len(digitos) != 8:
        raise ValueError("O CEP deve conter exatamente 8 dígitos.")
    return digitos


def obter_endereco_por_cep(cep):
    cep = normalizar_cep(cep)
    conexao = http.client.HTTPSConnection("viacep.com.br", timeout=10)
    try:
        conexao.request("GET", f"/ws/{cep}/json/")
        resposta = conexao.getresponse()
        if resposta.status != 200:
            raise RuntimeError(f"A API ViaCEP respondeu com HTTP {resposta.status}.")
        endereco = json.loads(resposta.read().decode("utf-8"))
        if not isinstance(endereco, dict):
            raise RuntimeError("A resposta da API ViaCEP não tem o formato esperado.")
        if "erro" in endereco:
            return None
        return endereco
    finally:
        conexao.close()


def main():
    cep = input("Digite o CEP que deseja consultar: ")
    try:
        endereco = obter_endereco_por_cep(cep)
    except (ValueError, OSError, http.client.HTTPException, RuntimeError, json.JSONDecodeError) as erro:
        print(f"Não foi possível consultar o CEP: {erro}")
        return
    print(endereco if endereco is not None else "CEP não encontrado.")


if __name__ == "__main__":
    main()
