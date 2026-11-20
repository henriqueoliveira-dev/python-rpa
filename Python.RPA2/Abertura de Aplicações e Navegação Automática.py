import pyautogui as posicaoAbriGoogle
posicaoAbriGoogle.sleep(4)

#print(posicaoAbriGoogle.position())
posicaoAbriGoogle.moveTo(x=120, y=131)
posicaoAbriGoogle.doubleClick(x=120, y=131)

posicaoAbriGoogle.sleep(5)

posicaoAbriGoogle.typewrite('https://www.facebook.com/')

posicaoAbriGoogle.sleep(3)

posicaoAbriGoogle.press('enter')