import matplotlib.pyplot as plt


def str_bool(valor):
  if valor == 'True':
    return True
  else:
    return False  


alunos = []    
    
nome_arquivo = 'alunos.csv'  
arquivo = open(nome_arquivo, 'r') 
linhas = arquivo.readlines()


    
for linha in linhas[1:]: #percorre apartir linha 1
   linha = linha.replace('\n', '') # retira \n da linha
   registro = linha.split(',')#separa por virgula, vira um elemento
   aluno = {
            'nome': registro[0],
            'ano': int(registro[1]),
            'escola': registro [2],
            'nota_semestre_1': float(registro[3]),
            'nota_semestre_2': float(registro[4]),
            'faltas': int(registro[5]),
            'nota_exame': float(registro[6]),
            'monitoria': str_bool(registro[7])
                
        }
        
        
   alunos.append(aluno)





alunos_utilizou_monitoria = 0
alunos_nao_utilizou_monitoria = 0

for aluno in alunos:
  if aluno['monitoria'] == True:
    alunos_utilizou_monitoria += 1
  else :
    alunos_nao_utilizou_monitoria += 1  


   
total_monitorados = alunos_utilizou_monitoria + alunos_nao_utilizou_monitoria

media_utiizou_monitorados = alunos_utilizou_monitoria/total_monitorados
media_nao_utiizou_monitorados = alunos_nao_utilizou_monitoria/total_monitorados

print(f'O total de pessoas que utilizou monitoria é {media_utiizou_monitorados}%')
print(f'O total de pessoas que nao utilizou monitoria é {media_nao_utiizou_monitorados}%')





#GRAFICO PIZZA 


labels = 'Utilizou Monitoria','Nao Utilizou Monitoria'
sizes = media_utiizou_monitorados,media_nao_utiizou_monitorados
cores = ('red','green')
explode = [0.08,0.081]
plt.pie(sizes, labels=labels, shadow=True, startangle=50, colors=cores, autopct='%1.1f%%', explode=explode)
plt.show()



