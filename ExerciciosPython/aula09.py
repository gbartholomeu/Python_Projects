#Manipulando Strings
frase = 'Curso em video python'
frase2 = '     que vazio, que solidão      '

''' Parte 1 '''
print(frase[9]) # imprime caractere na 9ª posição
print(frase[9:13]) # imprime caracteres a partir da 9ª posição até a 13ª. NÃO INCLUSIVO! Ou seja, o último caractere não é impresso
print(frase[9:21:2]) # imprime caracteres entre a 9ª até a 21ª posição indo de 2 em 2 caracteres
print(frase[:5]) # imprime todos os caracteres até a posição informada. NÃO INCLUSIVO! Ou seja, o último caractere não é impresso
print(frase[15:]) # imprime todos os caracteres a partir da posição informada até o final
print(frase[9::3]) # imprime todos os caracteres a partir da 9ª posição até o final, indo de 3 em 3 caracteres

''' Parte 2 '''
print(len(frase)) # O número da posição começa em 0, ou seja, minha variável frase vai de 0 até 20 - 21 caracteres
print(frase.count('o')) # conta o número de vezes que a letra aparece dentro da string
print(frase.count('o', 0, 13)) # conta o número de vezes que a letra aparece dentro da string dentro do intervalo fornecido
print(frase.find('deo')) # imprime a posição de inicio de onde o texto foi encontrado
print(frase.find('Android'))

''' Parte 3 '''
print(frase.replace('python', 'Android')) # Substitui o primeiro texto pelo segundo
print(frase.upper()) # Imprime o texto todo em maiúsculo
print(frase.lower()) # Imprime o texto todo em minúsculo
print(frase.capitalize()) # Imprime tudo em minúsculo exceto pelo primeiro caractere
print(frase.title()) # Imprime o primeiro caractere de cada palavra em maiúsculo

''' Parte 4'''
print(frase2.strip()) # Remove todos os espaços excedentes antes e depois do texto
print(frase2.rstrip()) # Remove todos os espaços excedentes antes do texto (Right strip)
print(frase2.lstrip()) # Remove todos os espaços excedentes depois do texto (Left strip)

#Curso pausado em 25:10#