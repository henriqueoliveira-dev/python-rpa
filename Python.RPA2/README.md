# Automação de aplicações com PyAutoGUI

Exercícios introdutórios de automação de interface gráfica: controle do mouse, abertura de aplicações, navegação e escolha por menu.

## Scripts

- `Controle do Mouse com PyAutoGUI.py`: movimentação e clique em posições da tela.
- `Abertura de Aplicações e Navegação Automática.py`: abertura do navegador por uma posição predefinida e navegação para um endereço.
- `Abertura e Controle de Aplicações com PyAutoGUI.py`: abertura e fechamento de uma janela do Bloco de Notas.
- `Automação de Aplicações com Menu de Seleção.py`: menu para iniciar Excel, Word ou Bloco de Notas.

## Requisitos e execução

Os exemplos dependem de Python 3 e PyAutoGUI:

```bash
python -m pip install pyautogui
python "Controle do Mouse com PyAutoGUI.py"
```

São exemplos destinados a uma sessão gráfica Windows. As coordenadas de tela e os nomes das aplicações variam conforme o computador; ajuste-os antes de executar. O PyAutoGUI pode controlar o computador real, portanto revise cada ação e mantenha a opção de parada de emergência padrão (mover o cursor para um canto da tela).
