import pygame
import time as t

# Initialize the mixer
pygame.mixer.init()
# Load two sounds
snd1 = pygame.mixer.Sound('kick3.wav')
snd2 = pygame.mixer.Sound('hats2.wav')
snd3 = pygame.mixer.Sound('snare2.wav')
# Play the sounds; these will play simultaneously
t.sleep(0.5)

snd1.play()
t.sleep(0.3)
snd2.play()
t.sleep(0.3)
snd1.play()
t.sleep(0.3)
snd2.play()
t.sleep(0.3)
