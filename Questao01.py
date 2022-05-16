

from openpyxl import load_workbook

#https://letscode.com.br/blog/aprenda-a-integrar-python-e-excel
#https://openpyxl.readthedocs.io/en/stable/tutorial.html

#caminho = 'AULAS-EAD-REGISTRO-DE-ATIVIDADE.xlsx'
caminho = 'trabalhandocomplanilhas(1).xlsx'
arquivo_excel = load_workbook(caminho, data_only=True)

planilha = arquivo_excel.active
#conteudo = planilha['B5']
#celula = []
#celula.append(conteudo.value)

notas1 = []
notas2 = []
notas3 = []

#for i in range(7, 12):


#Capturar os valores das colunas
for i in range(7, 12):
    conteudo = planilha[f'C{i}']
    notas1.append(conteudo.value)

for i in range(7, 12):
    conteudo = planilha[f'D{i}']
    notas2.append(conteudo.value)

for i in range(7, 12):
    conteudo = planilha[f'E{i}']
    notas3.append(conteudo.value)

#Codigo incompleto

