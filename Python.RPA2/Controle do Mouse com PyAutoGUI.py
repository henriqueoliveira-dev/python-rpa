import pyautogui as posicao_mouse


def main():
    # As coordenadas variam conforme a resolução e a posição da barra de tarefas.
    posicao_mouse.sleep(2)
    posicao_mouse.moveTo(x=22, y=1002)
    posicao_mouse.click(x=22, y=1002)
    posicao_mouse.sleep(4)
    posicao_mouse.moveTo(x=173, y=554)
    posicao_mouse.click(x=173, y=554)
    print(posicao_mouse.position())


if __name__ == "__main__":
    main()
