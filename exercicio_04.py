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

  
media_semestre_1,contador = 0,0
media_semestre_3,contador1 = 0,0

#PROCESSANDO

for aluno in alunos:
  if aluno['ano'] == 1:
    media_semestre_1 += aluno['nota_semestre_1']
    contador+= 1
  elif aluno['ano'] == 3:
    media_semestre_3 += aluno['nota_semestre_1']
    contador1+=1  

media_final_1 =  media_semestre_1/contador
media_final_3 =  media_semestre_3/contador1 

print(f'A media final de alunos do 3 ano é {media_final_3:.2f} > media final de alunos ano 1 é {media_final_1:.2f}')




#GRAFICO

import matplotlib.pyplot as plt



data = {'Notas Aluno ano 1': media_final_1,
        'Notas Aluno ano 3': media_final_3
        }

chave = list(data.keys())
valores = list(data.values())
color = 'red', 'green', 

plt.bar(chave, valores, color=color, width=0.8)
plt.title('Análise de notas Semestre ')
plt.show()