import os
from pathlib import Path

import xlsxwriter


def criar_planilha(nome_caminho_arquivo="Nome,Idade.xlsx"):
    caminho = Path(nome_caminho_arquivo).expanduser()
    caminho.parent.mkdir(parents=True, exist_ok=True)
    with xlsxwriter.Workbook(caminho) as planilha:
        aba = planilha.add_worksheet()
        aba.write_row("A1", ["Nome", "Idade"])
        aba.write_row("A2", ["Amanda", 28])
        aba.write_row("A3", ["Roberto", 25])
    return caminho


def main():
    caminho = criar_planilha()
    print(f"Planilha criada: {caminho.resolve()}")
    if hasattr(os, "startfile"):
        os.startfile(caminho)
    else:
        print("A abertura automática está disponível somente no Windows.")


if __name__ == "__main__":
    main()
