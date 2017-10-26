import pygame


background_color = (255,255,255)
RED = (255,0,0)
width, height = 640, 480

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Plague Simulation')
screen.fill(background_color)

pygame.init()

intro = True

while intro:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                intro = False
                running = True
            if event.key == pygame.K_q:
                pygame.quit()
                quit()


    basicfont = pygame.font.SysFont(None, 48)
    text = basicfont.render('Welcome To A Plague Simulation!', True, (0, 0, 0), (255, 255, 255))
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery
    screen.blit(text, textrect)

    pygame.display.update()

running = True
while running:
    screen.fill(background_color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    """ circles represent classes for now"""
    pygame.draw.circle(screen, RED, (300,200), 38)
    pygame.draw.circle(screen, (0,255,0), (150,250),36)
    pygame.draw.circle(screen, (0,0,255), (200,350),30)

    pygame.display.update()
