import pygame

mp3Path = 'loveMe.mp3'

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(mp3Path)
pygame.mixer.music.play()
pygame.event.wait()

# Nota: Funcionou as primeiras vezes, mas a música ficou bizarra.... buscar outro módulo para isso