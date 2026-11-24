import pyautogui as automacao


def main():
    automacao.hotkey("win", "r")
    automacao.sleep(0.5)
    automacao.write("notepad")
    automacao.press("enter")
    automacao.sleep(1.5)
    automacao.write("Aprendendo RPA, na pratica!!!")
    automacao.sleep(1)
    janela = automacao.getActiveWindow()
    if janela is None:
        print("Não foi possível identificar a janela ativa; ela não será fechada.")
        return
    janela.close()
    # Confirma o diálogo de salvamento sem salvar o documento de exemplo.
    automacao.sleep(0.5)
    automacao.press("tab")
    automacao.press("enter")


if __name__ == "__main__":
    main()
