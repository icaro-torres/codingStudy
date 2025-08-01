import pygame

# inicializando o mixer do pygame
pygame.mixer.init()

# carregando a música
pygame.mixer.music.set_volume(0.5)  # ajustando o volume
pygame.mixer.music.load('mundo01/musica.mp3')

# tocando a música
pygame.mixer.music.play()

# manter o programa rodando enquanto a música toca
input('Pressione Enter para parar a música...')
pygame.mixer.music.stop()