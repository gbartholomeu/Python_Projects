import random

alunoUm = str(input('Digite o nome do primeiro aluno: '))
alunoDois = str(input('Digite o nome do segundo aluno: '))
alunoTres = str(input('Digite o nome do terceiro aluno: '))
alunoQuatro = str(input('Digite o nome do quarto aluno: '))

alunosMisturados = [alunoUm, alunoDois, alunoTres, alunoQuatro]
random.shuffle(alunosMisturados)

print('Os alunos foram sorteados na ortem: 1º {}, 2º {}, 3º {} e 4º {}'.format(alunosMisturados[0],
                                                                               alunosMisturados[1],
                                                                               alunosMisturados[2],
                                                                               alunosMisturados[3]))

'''Resposta da aula: ao invés do .format, ele imprimiu a lista diretament'''