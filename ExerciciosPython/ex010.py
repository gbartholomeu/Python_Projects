reais = float(input('Quantos reais você possui na carteira? R$'))
dolar = reais/3.27
print('Com R${:.2f} você pode comprar US${:.2f}!'.format(reais, dolar))
