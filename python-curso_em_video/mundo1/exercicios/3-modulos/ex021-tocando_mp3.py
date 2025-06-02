# Tocando música no python
# OBS: antes de qualquer coisa, add a música que vai ser tocada na mesma pasta do código

import pygame
pygame.init()
pygame.mixer.music.load('nome_do_arquivo')
pygame.mixer.music.play()
pygame.event.wait()     # Espera a musica acabar para encerrar o programa


