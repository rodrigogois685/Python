import pygame
pygame.init()
pygame.mixer.music.load('C:/Users/rodri/OneDrive/Área de Trabalho/banhodoscampeoes.mpeg')
pygame.mixer.music.play()
pygame.event.wait()
print('Tocando agora o áudio do Banhão dos Campeões')