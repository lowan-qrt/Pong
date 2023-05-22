# Import des modules
import pygame
import random
import time

# Définition des couleurs (RGB)
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Initialisation de Pygame
pygame.init()

# /// FENETRE ///
sw = 800  # screen with
sh = 500  # screen height
# Affichage de la fenêtre
screen = pygame.display.set_mode((sw, sh))
# Nom de la fenêtre
pygame.display.set_caption('Pong')

# Chargement de l'image
image = pygame.image.load("image/pong_image.png")
# Redimensionnement de l'image pour l'adapter à la fenêtre
fenetre_rect = screen.get_rect()
image_rect = image.get_rect()
image_rect.center = fenetre_rect.center
image = pygame.transform.scale(image, (fenetre_rect.width, fenetre_rect.height))
# Affichage de l'image
screen.blit(image, (0, 0))
pygame.display.flip()

# Coordonnées et rayon de la balle
y = random.randint(1, 500)
cercle_x = sw // 2
cercle_y = y
rayon_cercle = 5
right_or_left = [-1, 1]
cercle_vx = 0.2*random.choice(right_or_left)  # vitesse de déplacement horizontal
cercle_vy = 0.2  # vitesse de déplacement vertical

# Dimensions des curseurs
rect_width = 15
rect_height = 100
# Vitesse de déplacement des curseurs
rect_speed = 0.5
# Coordonnées des curseurs
rect_player1_x = 50
rect_player1_y = sh // 2 - rect_height // 2
rect_player2_x = sw - rect_width - 50
rect_player2_y = sh // 2 - rect_height // 2

# Position et dimensions du carré
cote_carre = 50
carre_x = sw // 2 - cote_carre 
carre_y = 0
carre2_x = sw // 2
carre2_y = 0

# Position du trait vertical
trait_x = sw // 2
trait_longueur = sh

# Variables de score
score_joueur1 = 0
score_joueur2 = 0
font = pygame.font.Font(None, 36)  # Police d'écriture

# Temps d'attente de 5 secondes
debut = time.time()
# Temps d'attente de 5 secondes
debut = time.time()
while time.time() - debut < 5:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            

# Boucle principale
running = True
while running:
    # Ecoute des événements "quit"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Ecoute des événements "joueur"
    keys = pygame.key.get_pressed()
    # Joueur 1 : si [flèches directionnelles], monter ou descendre
    if keys[pygame.K_UP] and rect_player2_y >= 0:
        rect_player2_y -= rect_speed
    if keys[pygame.K_DOWN] and rect_player2_y + rect_height < sh:
        rect_player2_y += rect_speed
    # Joueur 2 : si [z] ou [s], monter ou descendre
    if keys[pygame.K_z] and rect_player1_y >= 0:
        rect_player1_y -= rect_speed
    if keys[pygame.K_s] and rect_player1_y + rect_height < sh:
        rect_player1_y += rect_speed

    # Mise à jour des coordonnées de la balle
    cercle_x += cercle_vx
    cercle_y += cercle_vy

    # Vérification des collisions avec les bords de l'écran (pour la balle)
    if cercle_y - rayon_cercle < 0 or cercle_y + rayon_cercle > sh:
        cercle_vy *= -1
    if cercle_x - rayon_cercle < 0 or cercle_x + rayon_cercle > sw:
        # Augmentation du score pour le joueur correspondant
        if cercle_x - rayon_cercle < 0:
            score_joueur2 += 1
        else:
            score_joueur1 += 1
        # Réinitialisation de la position de la balle
        cercle_x = sw // 2
        cercle_y = random.randint(1, 500)
        cercle_vx = 0.2*random.choice(right_or_left) 
        cercle_vy = 0.2

    # Vérification des collisions avec les curseurs (pour balle)
    if rect_player1_x + rect_width > cercle_x - rayon_cercle > rect_player1_x and rect_player1_y + rect_height > cercle_y > rect_player1_y:
        cercle_vx *= -1.1
    if rect_player2_x < cercle_x + rayon_cercle < rect_player2_x + rect_width and rect_player2_y + rect_height > cercle_y > rect_player2_y:
        cercle_vx *= -1.1

    # Disposition de l'écran en noir
    screen.fill(NOIR)

    # Dessin de la balle
    pygame.draw.circle(screen, BLANC, (int(cercle_x), int(cercle_y)), rayon_cercle)
    # Dessin des curseurs "Joueur x"
    pygame.draw.rect(screen, BLANC, (rect_player1_x, rect_player1_y, rect_width, rect_height))
    pygame.draw.rect(screen, BLANC, (rect_player2_x, rect_player2_y, rect_width, rect_height))
    # Dessin des carrés tableau
    pygame.draw.rect(screen, BLANC, (carre_x, carre_y, cote_carre, cote_carre), 1)
    pygame.draw.rect(screen, BLANC, (carre2_x, carre2_y, cote_carre, cote_carre), 1)
    # Dessin de la ligne verticale
    pygame.draw.line(screen, BLANC, (trait_x, 0), (trait_x, trait_longueur), 1)

    # Affichage du score
    score_texte = f"{score_joueur1} - {score_joueur2}"
    score_render = font.render(score_texte, True, BLANC)
    screen.blit(score_render, (sw // 2 - score_render.get_width() // 2, 10))

    # Mise à jour de l'affichage
    pygame.display.flip()

# Quitter Pygame + quitter le programme
pygame.quit()
exit()