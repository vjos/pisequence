import pygame
import time as t

pygame.mixer.init(channels=4)
pygame.mixer.pre_init(22050, -16, 1, 256)
pygame.init()

chan1 = pygame.mixer.Channel(0)
chan2 = pygame.mixer.Channel(1) 
chan3 = pygame.mixer.Channel(2) 

'''
t.sleep(1)
chan1.play(pygame.mixer.Sound('kick.wav'))
t.sleep(0.5)
chan2.play(pygame.mixer.Sound('snare.wav'))
t.sleep(0.5)
chan3.play(pygame.mixer.Sound('hats.wav'))
'''

chan1.set_volume(1.0)
chan2.set_volume(0.6)
chan3.set_volume(0.5)


'''chan1.stop()
chan2.stop()
chan3.stop()'''
t.sleep(0.3)
chan1.play(pygame.mixer.Sound('kick2.wav'))
chan3.play(pygame.mixer.Sound('hats.wav'))
t.sleep(0.3)
chan1.stop()
chan3.play(pygame.mixer.Sound('hats.wav'))
t.sleep(0.3)
chan3.stop()
chan2.play(pygame.mixer.Sound('snare.wav'))
chan3.play(pygame.mixer.Sound('hats.wav'))
t.sleep(0.3)
chan2.stop()
chan3.play(pygame.mixer.Sound('hats.wav'))
