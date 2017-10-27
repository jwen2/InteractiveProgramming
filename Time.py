"""
    Subeen Kim
    Input handling & time
"""
import pygame, time

pygame.init()
pygame.display.set_mode((400,300))
pygame.display.set_caption('Mouse Input Test')

"""pause untile frames_per_sec has passed"""
clock = pygame.time.Clock()
frames_per_sec = 30

"""
Input Handling
    pygame.event.wait() : sit and block further game execution until an events comes along
    pygame.event.poll() : will see whether there are any events wating for processing
    pygame.event.get() : returns all of the currently-outstanding events
"""

playtime = 0
running = True
while running:
    seconds = clock.tick(frames_per_sec)//30
    playtime += seconds

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            print (event.button)

pygame.display.quit()
