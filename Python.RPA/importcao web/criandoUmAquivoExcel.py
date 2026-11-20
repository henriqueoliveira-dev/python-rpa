
import xlsxwriter
import os


# Caminho do arquivo Excel
nomeCaminhoArquivo = 'C:\\Users\\Henrique Oliveira\\OneDrive\\Documentos\\Projeto-RPA\\Nome,Idade .xlsx'

# Criar arquivo Excel
planilhaCriada = xlsxwriter.Workbook(nomeCaminhoArquivo)

# Criar aba da planilha
sheet1 = planilhaCriada.add_worksheet()

# Escrever informações nas células
sheet1.write('A1', 'Nome')
sheet1.write('B1', 'Idade')
sheet1.write('A2', 'Amanda')
sheet1.write('B2', '28')
sheet1.write('A3', 'Roberto')
sheet1.write('B3', '25')

# Salvar e fechar arquivo
planilhaCriada.close()

# Abrir arquivo Excel
os.startfile(nomeCaminhoArquivo)

