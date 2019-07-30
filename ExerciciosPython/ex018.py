import math

angulo = float(input('Digite um um ângulo: '))
print('Para o ângulo {}, o valor de seno é {:.2f}, de cosseno é {:.2f} e o valor da tangente é {:.2f}'.format(angulo,
                                                                                                  math.sin(math.radians(angulo)),
                                                                                                  math.cos(math.radians(angulo)),
                                                                                                  math.tan(math.radians(angulo))))
