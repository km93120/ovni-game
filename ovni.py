import pygame
import time
from random import*#etoile = tout importer


#Verifier si environnement_txt ("appuyez sur une touche pour continuer", petit_txt ) n'est pas un pb, sinon remettre à l'état d'origine




#couleurs
blue = (113,177,227)
white = (255, 255, 255)

pygame.init()

#taille de l'écran, de l'objet et des obstacles
screenW = 800#de la fenetre
screenH = 500
screen = pygame.display.set_mode((screenW, screenH))#donne les valeurs de size à la taille de l'écran
pygame.display.set_caption("Objet volant")#nomme la fenêtre



explications = false
jeu = false

police = pygame.font.Font('freesans', 50)

Title = police.render("OVNI", True,White)

TitlePosition = Title.get_rect()
TitlePosition.centerx = screen.get_rect()center.x
TitlePosition.centery = 20
screen.blit(Title, TitlePosition)

police_p = pygame.font.Font('freesans',20)
Play = police_p.render("Jouer !! (F1)",True,white)
PlayPosition = Play.get_rect()
PlayPosition.centerx = screen.get_rect().centerx
PlayPosition.centery = 150
screen.blit(Play, PlayPosition)

Help = police_p.render("Aide (F2)",True,white)
HelpPosition = Help.get_rect()
HelpPosition.centerx = screen.get_rect().centerx
HelpPosition.centery = 150
screen.blit(Help, HelpPosition)

def aide :
	police_instruction = pygame.font.Font('Freesans',10)
	instructions = police_instruction.render("Bienvenue dans OVNI, le but est d'éviter les obstacles. fleche haut : monter, fleche bas : descendre",True,white)
	positionInstructions = instructions.get_rect()
	positionInstructions.centerx =  screen.get_rect().centerx
	positionInstructions.centery =  250
	screen.blit(Title, TitlePosition)	
	commencerJeu = police_instruction.render("Jouez maintenant -> F1",True,white)
	while not jeu
	for event in pygame.event.get()
		if event.type == pygame.K_F1
			jeu = True
	
while not jeu
	for event in pygame.event.get()
		if event.type == pygame.K_F1
			jeu = True
			
if jeu == True
	main()
	
			
while not explications
	for event in pygame.event.get()
		if event.type == pygame.K_F2
			explications = True
			
if explications == True
	aide()
objetW = 50#de l'ovni
objetH = 50

obstacleH = 300#des obstacles
obstacleW = 121

clock = pygame.time.Clock()#la var clock correspond à Clock cherchée dans la bibliotheque python

#charge les imgs
img = pygame.image.load('Objet.png')
img_obstacle = pygame.image.load('Obstacle.png')#l'image de l'obstacle



#compteur de points
def score(compte) :
    police = pygame.font.Font('BradBunR.ttf', 16)
    texte = police.render("score : " + str(compte), True, white)#affiche le texte "score:" auquel on ajoute compte en string pour éviter les pb d'addition de deux formats différents
    screen.blit(texte, [10,0])#position du texte


#importation des obstacles et de leur position
def obstacle(x_obstacle, y_obstacle, espace):#x: position abscisse, y:position ordonnée, espace: l'espace entre l'obstacle du haut et du bas
    screen.blit(img_obstacle, (x_obstacle, y_obstacle))#obstacle du haut
    screen.blit(img_obstacle,(x_obstacle,y_obstacle+ obstacleH +espace))#obstacle du bas et espace entre les deux


#rejouer ou quitter
def rejoueOuQuitte():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):#cherche les évènements mis en paramètre
        if event.type == pygame.QUIT :#si parmis ces évènements il y a pygame.QUIT
            pygame.quit()
            quit()#quitte le jeu
        elif event.type == pygame.KEYUP:#si je joueur relache la touche et perd
            continue
        return event.key#on renvoie un évènement clé, comme ca si aucun de ces évèments apparait, la fct renvoie none

    return  None

#police d'écriture
def environnement_txt (texte, font):
    screen_txt = font.render(texte,True,white)#screen_txt: texte(on veut texte), true(on veut l'afficher), white(en blanc)
    return screen_txt, screen_txt.get_rect()#retourne screen_txt et la valeur du rectangle qui le contient

def message (texte):
    gros_txt = pygame.font.Font('BradBunR.ttf', 150)#police du texte si gameover
    petit_txt = pygame.font.Font('BradBunR.ttf', 20)#police du petit texte en dessous

    petit_txt_screen, petit_txt_rectangle = environnement_txt ("appuyez sur une touche pour continuer", petit_txt)#declaration des variables :"petit_txt_screen" et de son contenant
    petit_txt_rectangle.center = screenW/2, ((screenH/2) +50)#création de la variable petit_txt_rectangle.center qui permet de centrer le rectangle qui contient le petit txt
    screen.blit(petit_txt_screen, petit_txt_rectangle)

    gros_txt_screen, gros_txt_rectangle = environnement_txt(texte, gros_txt)
    gros_txt_rectangle.center = screenW/2,((screenH/2)-50)
    screen.blit(gros_txt_screen, gros_txt_rectangle)

    pygame.display.update()
    time.sleep(2)#evite de relancer le jeu si on appuie sur une touche sans faire exprès

    while rejoueOuQuitte() == None :
        clock.tick()#0 images / sec, img bloquée

    main()#retourne dans la fct principale, continue le jeu

#declaration de la fct gameOver, qd elle est appellée le message s'affichera. Message() est déclaré juste après
def gameOver():
    message("T'es mort")


#affiche l'image "img" (notre ovni) en fonction des paramètres x, y et image
def objet(x,y, image):
    screen.blit(image, (x,y))


def main():
    #position de base de notre ovni, point d'origine des axes: en haut à gauche
    x=150
    y=225
    y_move=0#au lancement l'ovni ne bouge pas


    x_obstacle = screenW #l'obstacle apparraît tout à droite
    y_obstacle = randint(-300,10)#la position en hauteur de l'obstacle est aléatoire, ils peuvent monter de 300px au max ou descendre de 10
    espace = objetH*5#l'espacement entre les obstacles sera au début de 3x la hauteur de l'ovni
    obstacle_vitesse = 1

    score_actuel = 0

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                game_over= True

            if event.type == pygame.KEYDOWN:#si l'évenement correspond à un appui sur une touche
                if event.key == pygame.K_UP:#si la touche en question est la flèche "UP"
                    y_move = -1#mvt de -1px vers le haut
            if event.type ==pygame.KEYUP :#s'il correspont à un relachement de la touche
                y_move = 1#descente de 1px

        y += y_move#la position y vaudra y + y_move, on aura donc un déplacement

        screen.fill(blue)#l'ordre dans lequel sont implémentés nos fct est important car le dernier implémenté est surperposé sur celui d'avant
        objet(x,y,img)

        obstacle(x_obstacle,y_obstacle, espace)

        score(score_actuel)

        x_obstacle -=obstacle_vitesse#permet de faire avancer les obstacles vers l'ovni

        #si l'ovni dépasse de 2px le bord sup ou de 1px le bord inf de l'écran, gameover
        if y>screenH -2 or y <-1:
            gameOver()

        if x_obstacle < (-1*obstacleW):#si l'obstacle se retrouve sorti sur la gauche de l'cran,
            x_obstacle = screenW#alors l'obstacle revient à sa position initiale (tout à droite avec y aléatoire)
            y_obstacle = randint(-300,10)
            

            #augmente la difficulé en fct du score
            if 3 <= score_actuel < 5:
                obstacle_vitesse = 1.2
                espace = objetH*4
            if 5 <= score_actuel < 7 :
                obstacle_vitesse = 1.5
                espace = objetH*3.5
            if 7 <= score_actuel < 10 :
                obstacle_vitesse = 1.8
                espace = objetH*3
            if 10 <= score_actuel <22:
                obstacle_vitesse = 2.2
                espace = objetH*2.5
            if 22 <= score_actuel:
                obstacle_vitesse = 3
                espace = objetH*2


        #si la position en abscisse de l'ovni + sa largeur (donc le coin en haut à droite de l'ovni) est supérieur à la position gauche de l'obstacle +10px de marge
        if x +objetW > x_obstacle + 10 :
            if y < y_obstacle + obstacleH -10:#si l'ovni déborde sur l'obstacle du haut +10px de marge
                if x < x_obstacle +obstacleW -10 :#si l'ovni n'a pas dépassé l'obstacle -10px de marge
                    gameOver()

        if x +objetW >x_obstacle + 10 :#idem: si le x du coin droit de l'ovni dépasse le x de gauche des obstacles,
            if y +objetH > y_obstacle + obstacleH + espace +10 :#si l'ovni arrive plus bas que l'obstacle du bas (rappel: l'obstacle du bas = obstacle du haut mais déscendu de sa hauteur + de l'espace)
                if x < x_obstacle+ obstacleW - 10:#si l'ovni n'a pas dépassé les obstacles
                    gameOver()
                    
        x_obstacle_centre = x_obstacle+obstacleW/2

        if x_obstacle_centre-1 < x < x_obstacle_centre+1 :
            score_actuel +=1

        pygame.display.update()




pygame.quit()
quit()
