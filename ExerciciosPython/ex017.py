from math import sqrt, pow

catetoOposto = float(input('Digite o tamanho do cateto oposto: '))
catetoAdjacente = float(input('Digite o tamanho do cateto adjacente: '))
hipotenusa = sqrt(pow(catetoOposto, 2) + pow(catetoAdjacente, 2))
msg = 'O valor da hipotenusa de um triângulo retângulo com um cateto oposto de {} e cateto adjacente de {} é {}'

print(msg.format(catetoOposto, catetoAdjacente, hipotenusa))

'''resposta da aula: 
math.hipot(co, ca)
'''