import matplotlib.pyplot as plt
nome_arquivo = 'alunos.csv'
arquivo = open(nome_arquivo, 'r')
linhas = arquivo.readlines()

alunos = []


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


# RESPOSTA QUESTAO 1

soma_semestre_1 = 0
soma_semestre_2 = 0

for aluno in alunos:
    soma_semestre_1 = soma_semestre_1 + aluno['nota_semestre_1']
    soma_semestre_2 = soma_semestre_2 + aluno['nota_semestre_2']


if soma_semestre_1 > soma_semestre_2:
    print(f'A soma semestre 1 é {soma_semestre_1} é > que a soma semestre 2 {soma_semestre_2}')
elif soma_semestre_2 > soma_semestre_1:
    print(f'A soma semestre 2 é {soma_semestre_2} é > que a soma semestre 1 {soma_semestre_1}')

 # GRAFICO


# GRAFICO

total_soma = soma_semestre_1 + soma_semestre_2

data = {'Total Semestre 1': soma_semestre_1,
        'Total Semestre 2': soma_semestre_2, 'Soma Total': total_soma}

chave = list(data.keys())
valores = list(data.values())
color = 'red', 'green', 'blue'

plt.bar(chave, valores, color=color, width=0.8)
plt.title('Análise de notas ')
plt.show()
