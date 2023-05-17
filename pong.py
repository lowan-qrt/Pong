# Importation du module Pygame
import pygame

# Initialisation de Pygame
pygame.init()

# Définition des couleurs (RGB)
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Dimensions
sw = 800 # screen width
sh = 500 # screen height

# Dimensions de la fenêtre
screen = pygame.display.set_mode((sw, sh))
# Nom de la fenêtre
pygame.display.set_caption('Pong')

# Coordonnées et rayon de la balle
cercle_x = sw // 2
cercle_y = sh // 2
rayon_cercle = 5

# Dimensions curseurs
rect_width = 15
rect_height = 100
# Vitesse de déplacement curseurs
rect_speed = 0.2
# Coordonnées curseurs
rect_player1_x = 50
rect_player1_y = sh // 2 - rect_height // 2
rect_player2_x = sw - rect_width - 50
rect_player2_y = sh // 2 - rect_height // 2

# Boucle principale
running = True
while running:
    # Ecoute des events "quit"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ecoute des events "joueur"
    keys = pygame.key.get_pressed()
    # Joueur 1 : si [flèches directionnelles], monter ou descendre
    if keys[pygame.K_z] and rect_player2_y > 0:
        rect_player2_y -= rect_speed
    if keys[pygame.K_s] and rect_player2_y + rect_height < sh:
        rect_player2_y += rect_speed
    # Joueur 2 : si [z] ou [s], monter ou descendre
    if keys[pygame.K_UP] and rect_player1_y > 0:
        rect_player1_y -= rect_speed
    if keys[pygame.K_DOWN] and rect_player1_y + rect_height < sh:
        rect_player1_y += rect_speed    

    # Disposition de l'écran en noir
    screen.fill(NOIR)

    # Dessin de la balle
    pygame.draw.circle(screen, BLANC, (cercle_x, cercle_y), rayon_cercle)
    # Dessin curseurs "Joueur x"
    pygame.draw.rect(screen, BLANC, (rect_player1_x, rect_player1_y, rect_width, rect_height))
    pygame.draw.rect(screen, BLANC, (rect_player2_x, rect_player2_y, rect_width, rect_height))
    # Mise à jour de l'affichage
    pygame.display.flip()

# Quitter Pygame + quitter le programme
pygame.quit()
exit()