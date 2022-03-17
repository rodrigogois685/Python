import pygame
pygame.init()
pygame.mixer.music.load('C:\Users\rodrigo.gois\OneDrive\Área de Trabalho\estudos\Curso--Python\Exercicíos\Mundo 1/musica_do_sherek.mp3')
pygame.mixer.music.play()
pygame.event.wait()
print('Tocando agora o áudio do Banhão dos Campeões')
