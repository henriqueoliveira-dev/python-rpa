import pyautogui as posicaoMouse
#Tempo de espera para o computador pensar
posicaoMouse.sleep(2)

#Mover o mouse
posicaoMouse.moveTo(x=22, y=1002)
#Cliancado com o botão start ou seja no botão do windows
posicaoMouse.click(x=22, y=1002)
#Tempo para o computador pensar
posicaoMouse.sleep(4)

posicaoMouse.moveTo(x=173, y=554)
posicaoMouse.click(x=173, y=554)

#Colsutando execel no buscado do windows
#posicaoMouse.typewrite("execel")

print(posicaoMouse.position())

