import pyautogui
import pyautogui as escolha_opcao

opcao = pyautogui.confirm(
    "Clique no botão desejado",
    buttons=['Excel', 'Word', 'Notepad']
)

if opcao == "Excel":
    escolha_opcao.hotkey('win', 'r')

    escolha_opcao.sleep(2)

    escolha_opcao.typewrite('Excel')

    escolha_opcao.press('Enter')

    escolha_opcao.sleep(3)

    escolha_opcao.click(x=461, y=257)

    escolha_opcao.sleep(3)

    escolha_opcao.typewrite("Excel aberto com sucesso!")
    
    #print(escolha_opcao.position())



elif opcao == "Word":
    escolha_opcao.hotkey('win', 'r')
    
    escolha_opcao.sleep(2)
    
    escolha_opcao.typewrite('winword')
    
    escolha_opcao.press('Enter')

    escolha_opcao.sleep(2.5)
    
    escolha_opcao.click(x=318, y=200)
    
    escolha_opcao.sleep(3)
    
    escolha_opcao.typewrite("Word aberto com sucesso!")
        
    print(escolha_opcao.position())
    
elif opcao == "Notepad":
    
    escolha_opcao.hotkey('win', 'r')
        
    escolha_opcao.sleep(2)
    
    escolha_opcao.typewrite('Notepad')
    
    escolha_opcao.press('Enter')

    escolha_opcao.sleep(2.5)
    
    escolha_opcao.typewrite("Notepad aberto com sucesso!")
        
    #print(escolha_opcao.position())  