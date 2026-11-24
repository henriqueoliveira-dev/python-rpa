import pyautogui


def abrir_aplicacao(aplicacao):
    comandos = {"Excel": "excel", "Word": "winword", "Notepad": "notepad"}
    if aplicacao not in comandos:
        return
    pyautogui.hotkey("win", "r")
    pyautogui.sleep(1)
    pyautogui.write(comandos[aplicacao])
    pyautogui.press("enter")
    pyautogui.sleep(3)
    pyautogui.write(f"{aplicacao} aberto com sucesso!")


def main():
    opcao = pyautogui.confirm(
        "Clique no botão desejado",
        buttons=["Excel", "Word", "Notepad"],
    )
    if opcao is not None:
        abrir_aplicacao(opcao)


if __name__ == "__main__":
    main()
