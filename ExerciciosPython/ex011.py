larguraParede = float(input('Digite a largura da parede: '))
alturaParede = float(input('Digite a altura da parede: '))
dimensao = str('{}x{}'.format(larguraParede, alturaParede))
area = float('{:.3f}'.format(alturaParede*larguraParede))
qtdTinta = area/2
print('Sua parede tem dimensão {} e sua área é de {}m².'.format(dimensao, area))
print('Para pintar essa parede, você precisará  de {:.4f}l de tinta.'.format(qtdTinta))
