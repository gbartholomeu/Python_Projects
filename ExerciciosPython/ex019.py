import random

alunoUm = str(input('Digite o nome do primeiro aluno: '))
alunoDois = str(input('Digite o nome do segundo aluno: '))
alunoTres = str(input('Digite o nome do terceiro aluno: '))
alunoQuatro = str(input('Digite o nome do quarto aluno: '))
alunoEscolhido = random.choice([alunoUm, alunoDois, alunoTres, alunoQuatro])

print('O aluno escolhido para ajudar o professor foi o/a {}'.format(alunoEscolhido))

'''Resposta corrigida: ele apenas fez o import do choice direto e declarou a lista fora do método'''