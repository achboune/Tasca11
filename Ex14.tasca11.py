import pygame
from random import randint  # Importa randint del módulo random

# Inicializamos la biblioteca, creamos la ventana y le ponemos un título
pygame.init()                      	 
w = pygame.display.set_mode((640,480))  
pygame.display.set_caption("Joc")   
    
# Cargamos una imagen, obtenemos su rectángulo, le asignamos una velocidad y la posicionamos arriba a la izquierda
pilota = pygame.image.load("ball.png")  
pilotarect = pilota.get_rect()    	 
speed = [randint(2,6), randint(2,6)]	 
pilotarect.move_ip(0,0)
    
# Cargamos otra imagen, obtenemos su rectángulo y la movemos casi a la parte inferior y al centro
barra = pygame.image.load("bate.png")
barrarect = barra.get_rect()
barrarect.move_ip(240, 450)

# Tamaño de la fuente que se mostrará en pantalla
fuente = pygame.font.Font(None, 36)

# Bucle principal
j = True
while j:
    # Controlamos todos los eventos y si el jugador cierra, terminamos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            j = False
            
    # Controlamos la barra con el teclado: flecha izquierda y derecha, movemos en la dirección adecuada.
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        barrarect = barrarect.move(-3, 0)
    if keys[pygame.K_RIGHT]:
        barrarect = barrarect.move(3, 0)
        
    if barrarect.colliderect(pilotarect):
        speed[1] = -speed[1]
        
    # Controlamos la pelota: si colisiona, cambiamos la dirección en un eje, dependiendo de dónde sea.
    pilotarect = pilotarect.move(speed)
    if pilotarect.left < 0 or pilotarect.right > w.get_width():
        speed[0] = -speed[0]
    if pilotarect.top < 0:
        speed[1] = -speed[1]
        
    # Si la pelota toca el suelo, ¡hemos perdido! si no, la barra nos ha salvado.
    if pilotarect.bottom > w.get_height():
        texto = fuente.render("Has perdut!", True, (125, 125, 125))
        texto_rect = texto.get_rect()
        texto_x = w.get_width() / 2 - texto_rect.width / 2
        texto_y = w.get_height() / 2 - texto_rect.height / 2
        w.blit(texto, [texto_x, texto_y])
    else:
        # Borramos todo, volvemos a dibujar la pelota y la barra
        w.fill((252, 243, 207))
        w.blit(pilota, pilotarect)
        w.blit(barra, barrarect)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
