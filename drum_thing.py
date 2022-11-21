from email.header import Header
import pygame
from pygame import mixer
pygame.init()

WDTH = 1400
HEIGHT = 800

black = (0, 0, 0)
white = (255, 255, 255)
grey = (128, 128, 128)


screen = pygame.display.set_mode([WDTH, HEIGHT])
pygame.display.set_caption('Beat Maker')
label_font = pygame.font.Font('freesansbold.ttf', 32)

fps = 60
timer = pygame.time.Clock()
beats = 8
instraments = 6

def draw_grid():
    left_box = pygame.draw.rect(screen, grey, [0, 0, 200, HEIGHT - 200], 5)
    BOTTOM_BOX = pygame.draw.rect(screen, grey, [0, HEIGHT - 200, WDTH, 200], 5)
    boxes = []
    colors = [grey, white, grey]
    hi_hat_text = label_font.render('Hi Hat', True, white)
    screen.blit(hi_hat_text, (30, 30))
    snare_text = label_font.render('Snare', True, white)
    screen.blit(snare_text, (30, 130))
    kick_text = label_font.render('Bass Drum', True, white)
    screen.blit(kick_text, (30, 230))
    crash_text = label_font.render('Crash', True, white)
    screen.blit(crash_text, (30, 330))
    kick_text = label_font.render('Clap', True, white)
    screen.blit(kick_text, (30, 430))
    crash_text = label_font.render('Floor Tom', True, white)
    screen.blit(crash_text, (30, 530))
    for i in range (instraments):
        pygame.draw.line(screen, grey, (0, (i * 100) + 100), (200,  (i * 100) + 100), 3)

    for i in range(beats):
        for j in range(instraments):
            rect = pygame.draw.rect(screen, grey, [i * ((WDTH - 200) // beats) + 200, (j * 100), ((WDTH - 200) // beats), ((HEIGHT - 200) //instraments)], 5, 5)



run = True
while run:
    timer.tick(fps)
    screen.fill(black)
    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.flip()
pygame.quit()