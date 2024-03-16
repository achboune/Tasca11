import pygame
from random import randint

pygame.init()
w = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Joc")

pilota = pygame.image.load("ball.png")
pilotarect = pilota.get_rect()
speed = [randint(2, 6), randint(2, 6)]
pilotarect.move_ip(0, 0)

barra = pygame.image.load("bate.png")
barrarect = barra.get_rect()
barrarect.move_ip(240, 450)

fuente = pygame.font.Font(None, 36)

def handle_input():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and barrarect.left > 0:
        barrarect.move_ip(-3, 0)
    if keys[pygame.K_RIGHT] and barrarect.right < w.get_width():
        barrarect.move_ip(3, 0)

def update_state():
    global speed
    pilotarect.move_ip(speed)

    if pilotarect.left < 0 or pilotarect.right > w.get_width():
        speed[0] = -speed[0]
    if pilotarect.top < 0:
        speed[1] = -speed[1]

    if pilotarect.colliderect(barrarect):
        speed[1] = -speed[1]

def draw_screen():
    w.fill((252, 243, 207))
    w.blit(pilota, pilotarect)
    w.blit(barra, barrarect)

def show_game_over():
    texto = fuente.render("Has perdut!", True, (125, 125, 125))
    texto_rect = texto.get_rect()
    texto_x = w.get_width() / 2 - texto_rect.width / 2
    texto_y = w.get_height() / 2 - texto_rect.height / 2
    w.blit(texto, [texto_x, texto_y])

# Bucle principal
j = True
while j:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            j = False

    handle_input()
    update_state()

    if pilotarect.bottom > w.get_height():
        show_game_over()
    else:
        draw_screen()

    pygame.display.flip()
    pygame.time.Clock().tick(60)
