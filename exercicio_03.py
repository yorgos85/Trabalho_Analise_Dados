alunos = []

NOME_ARQUIVO = 'alunos.csv'
arquivo = open(NOME_ARQUIVO, 'r')
linhas = arquivo.readlines()


for linha in linhas[1:]:  # percorre apartir linha 1
    linha = linha.replace('\n', '')  # retira \n da linha
    registro = linha.split(',')  # separa por virgula, vira um elemento
    aluno = {
        'nome': registro[0],
        'ano': int(registro[1]),
        'escola': registro[2],
        'nota_semestre_1': float(registro[3]),
        'nota_semestre_2': float(registro[4]),
        'faltas': int(registro[5]),
        'nota_exame': float(registro[6]),
        'monitoria': registro[7]

    }

    alunos.append(aluno)

aluno_pedro = 0
faltas = 0

for aluno in alunos:
    if aluno['escola'] == 'Pedro II':
      faltas += aluno['faltas']  
      aluno_pedro += 1
      media = faltas/aluno_pedro
      
      
      
      
#MEDIA DE ALUNOS DE CASA ESCOLA

total_escolas = []
medias = []     
contador = []      
for i in alunos:
    controle = 0
    for j in range(len(total_escolas)):
        if i['escola'] == total_escolas[j] and controle == 0:
            medias[j] += i['faltas']
            contador[j] += 1
            controle = 1


    if controle == 0:
      total_escolas += [i['escola']]    
      medias += [i['faltas']]
      contador += [0]       
      
for i in range(len(medias)):
    medias[i] = medias[i]/contador[i]
        
         
      
 #IMPORTANDO O GRAFICO 
 
   
import matplotlib.pyplot as plt

plt.plot(total_escolas,medias)
plt.xticks(rotation = 13)
plt.ylabel('Média de Faltas')
plt.show()



