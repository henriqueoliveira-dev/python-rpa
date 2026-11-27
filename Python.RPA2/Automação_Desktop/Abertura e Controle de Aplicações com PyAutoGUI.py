import pyautogui as posicaoAbriArquivos
#O hotkey nos permite executar mais de uma tecla de atalho do windows, ou seja do teclado
#Nesse caso é a mesma coisa que precionar Windows + R
posicaoAbriArquivos.hotkey('win','r')

posicaoAbriArquivos.sleep(0.1)

posicaoAbriArquivos.typewrite('notepad')

posicaoAbriArquivos.press('enter')

posicaoAbriArquivos.sleep(0.5)

posicaoAbriArquivos.typewrite('Aprendendo RPA, na pratica!!!')

posicaoAbriArquivos.sleep(1.5)
#O getActive Windows permite pega a janela  que está ativa
fecharjanelaNotpad = posicaoAbriArquivos.getActiveWindow()

fecharjanelaNotpad.close()

posicaoAbriArquivos.press('tab')

posicaoAbriArquivos.sleep(1.6)

posicaoAbriArquivos.press('enter')

