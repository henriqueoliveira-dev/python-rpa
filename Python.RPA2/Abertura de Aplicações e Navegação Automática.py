import pyautogui as automacao


def main():
    automacao.sleep(4)
    # Ajuste as coordenadas ao atalho do navegador na sua área de trabalho.
    automacao.doubleClick(x=120, y=131)
    automacao.sleep(5)
    automacao.write("https://www.facebook.com/")
    automacao.press("enter")


if __name__ == "__main__":
    main()
