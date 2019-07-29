import math

catetoOposto = float(input('Digite o tamanho do cateto oposto: '))
catetoAdjacente = float(input('Digite o tamanho do cateto adjacente: '))
hipotenusa = math.sqrt(math.pow(catetoOposto, 2) + math.pow(catetoAdjacente, 2))

print('O valor da hipotenusa de um triângulo retângulo com um cateto oposto de {} e cateto adjacente de {} é {}'.format(catetoOposto, catetoAdjacente, hipotenusa))
