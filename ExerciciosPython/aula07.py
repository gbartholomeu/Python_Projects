#Ordem de precedêncida em Python
#1.()
#2.** -> Exponenciação
#3. * / // % -> Multiplicação, divisão, divisão inteira, resto da divisão
#4. + - -> soma e subtração binárias
#podemos fazer exponenciação utilizando ** ou o mẽtodo pow(x,y), porém isso não respeitará a ordem de precedência.

##String Formatting
msg = input('Digite seu nome: ')
print('Seu nome possui {} caracteres, porém será impresso utilizando 20: {:20}!'.format(len(msg), msg))

#No .format, podemos utilizar :n onde n será o número de caracteres que a string usará como espaçamento. No caso, apenas para aumentar. (Tamanho mĩnimo)

msg = input('Digite alguma outra coisa: ')
print('Posso imprimir sua coisa alinhando para a direita com 20 caracteres: {:>20}!'.format(msg))
print('Ou posso imprimir sua coisa alinhando para a esquerda com 20 caracteres: {:<20}!'.format(msg))
print('Ou até mesmo posso imprimir sua coisa centralizado entre 20 caracteres: {:^20}!'.format(msg))
print('E não se surpreenda, mas posso até trocar os espaços por outro caractere: {:=^20}!'.format(msg))

msg = int(input('Digite um número: '))
print('Posso utilizar o format para definir quantas casas decimais eu apresentarei, no caso, 3 casas: {:.3f}'.format(msg))

print('O print é tão versátil, que posso até mesmo imprimir dois comandos print sem quebrar a linha: ')
print('Por exemplo essa primeira linha.', end='')
print('Seguindo com essa.')

print('Mas se preferir posso usar o \\n para quebrar a linha... digamos... \n aqui')
print('O poder do \ me permite imprimir códigos como \\n ao invés de utilizamos ele como formatação, porém posso dobrar o {{}} ( {{{{}}}} ) para imprimir literal ao invés de \nobter o antigo valor do msg: {}'.format(msg))
