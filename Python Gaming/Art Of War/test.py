"""
    Author:   Byron Dowling
    Class:    5443 2D Python Gaming

    Asset Credits:

        - Viking Sprites:
            - Author: [Ragewortt]
            - https:\\ragewortt.itch.io\fantasy-heroes-vikings-sprite-sheet

        - Pirate Sprites:
            - Author: [Free Game Assets]
            - https:\\free-game-assets.itch.io\free-2d-pirate-sprites

        - Knight Sprites:
            - Author: [Free Game Assets]
            - https:\\free-game-assets.itch.io\free-2d-knight-sprite-sheets

        Background Art:
            - [Author] "klyaksun"
            - https:\\www.vecteezy.com\vector-art\15370321-ancient-roman-arena-for-gladiators-fight
            - https:\\www.vecteezy.com\vector-art\13852032-ancient-roman-arena-for-gladiators-fight-at-night

"""

import pygame
import pprint
import copy
import os
from PlayerSelection import PlayerSelector
from PIL import Image, ImageDraw
import utilities


###################################################################################################

"""
 ██████╗  █████╗  ██████╗██╗  ██╗ ██████╗ ██████╗  ██████╗ ██╗   ██╗███╗   ██╗██████╗ 
 ██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝ ██╔══██╗██╔═══██╗██║   ██║████╗  ██║██╔══██╗
 ██████╔╝███████║██║     █████╔╝ ██║  ███╗██████╔╝██║   ██║██║   ██║██╔██╗ ██║██║  ██║
 ██╔══██╗██╔══██║██║     ██╔═██╗ ██║   ██║██╔══██╗██║   ██║██║   ██║██║╚██╗██║██║  ██║
 ██████╔╝██║  ██║╚██████╗██║  ██╗╚██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██████╔╝
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═════╝ 
                                                                                      
 ██╗███╗   ███╗ █████╗  ██████╗ ███████╗██████╗ ██╗   ██╗                             
 ██║████╗ ████║██╔══██╗██╔════╝ ██╔════╝██╔══██╗╚██╗ ██╔╝                             
 ██║██╔████╔██║███████║██║  ███╗█████╗  ██████╔╝ ╚████╔╝                              
 ██║██║╚██╔╝██║██╔══██║██║   ██║██╔══╝  ██╔══██╗  ╚██╔╝                               
 ██║██║ ╚═╝ ██║██║  ██║╚██████╔╝███████╗██║  ██║   ██║                                
 ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝                                


      Helper background class from Dr. Griffin used on Batteship demo                                                                                 
"""

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location, size):

        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.width, self.height = self.getImgWidthHeight(image_file)
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, size)

        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


    def getImgWidthHeight(self, path):
        """Uses pil to image size in pixels.
        Params:
            path (string) : path to the image
        """
        if os.path.isfile(path):
            im = Image.open(path)
            return im.size
        return None


###################################################################################################

"""
  ██████╗  █████╗ ███╗   ███╗███████╗        
 ██╔════╝ ██╔══██╗████╗ ████║██╔════╝        
 ██║  ███╗███████║██╔████╔██║█████╗          
 ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝          
 ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗        
  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝        
                                             
 ███████╗██████╗ ██████╗ ██╗████████╗███████╗
 ██╔════╝██╔══██╗██╔══██╗██║╚══██╔══╝██╔════╝
 ███████╗██████╔╝██████╔╝██║   ██║   █████╗  
 ╚════██║██╔═══╝ ██╔══██╗██║   ██║   ██╔══╝  
 ███████║██║     ██║  ██║██║   ██║   ███████╗
 ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝
                                             
"""

class GameSprite:
    def __init__(self, imgLink, location, smsc_dimensions, inverted=False):
        
        if not inverted:
            GS = pygame.image.load(imgLink)
            GS = pygame.transform.smoothscale(GS, smsc_dimensions)
            screen.blit(GS, location)

        ## Inverted case where the Sprite is facing left
        else:
            GS = pygame.image.load(imgLink)
            GS = pygame.transform.smoothscale(GS, smsc_dimensions)
            GS_Copy = GS.copy()
            IGS = pygame.transform.flip(GS_Copy, True, False)
            screen.blit(IGS, location)

###################################################################################################

"""
 ██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗ 
 ██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗
 ██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝
 ██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗
 ██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║
 ╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                  
"""
class Player:
    def __init__(self, SP, P):
        self.StartingPosition = SP
        self.spriteObject = P
        self.player_X = SP[0]
        self.player_Y = SP[1]
        self.Standing = True
        self.Jumping = False
        self.Descending = False
        self.Projectile = False
        self.Jump_Height = 0
        self.idle_frameCount = P["Action"]["Idle"]["frameCount"]
        self.jump_frameCount = P["Action"]["Jump"]["frameCount"]
        self.idle_frame = 0
        self.jump_frame = 0
        self.name = P["Screen Name"]

###################################################################################################

""" 
  ██████╗  █████╗ ███╗   ███╗███████╗                                                 
 ██╔════╝ ██╔══██╗████╗ ████║██╔════╝                                                 
 ██║  ███╗███████║██╔████╔██║█████╗                                                   
 ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝                                                   
 ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗                                                 
  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝                                                 
                                                                                      
  ██████╗ ██████╗ ███╗   ██╗████████╗██████╗  ██████╗ ██╗     ██╗     ███████╗██████╗ 
 ██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝██╔══██╗██╔═══██╗██║     ██║     ██╔════╝██╔══██╗
 ██║     ██║   ██║██╔██╗ ██║   ██║   ██████╔╝██║   ██║██║     ██║     █████╗  ██████╔╝
 ██║     ██║   ██║██║╚██╗██║   ██║   ██╔══██╗██║   ██║██║     ██║     ██╔══╝  ██╔══██╗
 ╚██████╗╚██████╔╝██║ ╚████║   ██║   ██║  ██║╚██████╔╝███████╗███████╗███████╗██║  ██║
  ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
                                                                                      
"""
class GameController:
    def __init__(self, width, height):
        self.Running = True
        self.screenWidth = width
        self.screenHeight = height
        self.PLAYER_SPEED = 10
        self.VERTICAL_SPEED = 15
        self.JUMP_HEIGHT = 150
        self.PROJECTILE_VELOCITY = 75
        self.Default_Smoothscale_Dimensions = (250,250)
        self.Projectile_Smoothscale_Dimensions = (150,50)
        self.Players = []

    def getScreenSize(self):
        dimensions = (self.screenWidth, self.screenHeight)
        return dimensions
    
    def loadPlayers(self):
        C4 = PlayerSelector()
        sprites = C4.chooseSprites()
        P1 = Player((350, 500), sprites[0])
        P2 = Player((1350, 500), sprites[1])

        self.Players.append(copy.deepcopy(P1))
        self.Players.append(copy.deepcopy(P2))

        return self.Players


###################################################################################################

"""
  ██████╗  █████╗ ███╗   ███╗███████╗                                
 ██╔════╝ ██╔══██╗████╗ ████║██╔════╝                                
 ██║  ███╗███████║██╔████╔██║█████╗                                  
 ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝                                  
 ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗                                
  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝                                
                                                                     
 ██╗   ██╗ █████╗ ██████╗ ██╗ █████╗ ██████╗ ██╗     ███████╗███████╗
 ██║   ██║██╔══██╗██╔══██╗██║██╔══██╗██╔══██╗██║     ██╔════╝██╔════╝
 ██║   ██║███████║██████╔╝██║███████║██████╔╝██║     █████╗  ███████╗
 ╚██╗ ██╔╝██╔══██║██╔══██╗██║██╔══██║██╔══██╗██║     ██╔══╝  ╚════██║
  ╚████╔╝ ██║  ██║██║  ██║██║██║  ██║██████╔╝███████╗███████╗███████║
   ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝╚══════╝                                                                   
 """

## Initialize Pygame Stuff
pygame.init()
pygame.font.init()
pygame.mixer.init()
utilities.background_music()
running = True

## Rough Dimensions of Byron's Monitor
screenWidth = 1750
screenHeight = 800

## New Game Controller PBject
AOF = GameController(screenWidth, screenHeight)

## Set the size of the window using the above dimensions
size = (screenWidth, screenHeight)
screen = pygame.display.set_mode(size)

## Setting the background image and orienting starting from (0,0) origin i.e top left corner
BackGround = Background("Arena_Night.jpg", [0, 0], (screenWidth, screenHeight))

players = AOF.loadPlayers()

P1 = players[0]
P2 = players[1]

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(players)


## Set the title of the window
banner = f'Get Ready for Deadliest Warrior! {P1.name} vs {P2.name}'
pygame.display.set_caption(banner)

tick = 0

###################################################################################################

"""
  ██████╗ ██████╗ ██╗     ██╗     ██╗███████╗██╗ ██████╗ ███╗   ██╗
 ██╔════╝██╔═══██╗██║     ██║     ██║██╔════╝██║██╔═══██╗████╗  ██║
 ██║     ██║   ██║██║     ██║     ██║███████╗██║██║   ██║██╔██╗ ██║
 ██║     ██║   ██║██║     ██║     ██║╚════██║██║██║   ██║██║╚██╗██║
 ╚██████╗╚██████╔╝███████╗███████╗██║███████║██║╚██████╔╝██║ ╚████║
  ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝
                                                                   
  ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗     
 ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝     
 ██║     ███████║█████╗  ██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗    
 ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║    
 ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝    
  ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝     
                                                                    
"""
            
def checkForHorizontalCollisions(currentX):
    if currentX <= 10:
        return True
    elif currentX >= (screenWidth - 225):
        return True
    else:
        return False

###################################################################################################

"""
  ██████╗  █████╗ ███╗   ███╗███████╗    ██╗      ██████╗  ██████╗ ██████╗ 
 ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██║     ██╔═══██╗██╔═══██╗██╔══██╗
 ██║  ███╗███████║██╔████╔██║█████╗      ██║     ██║   ██║██║   ██║██████╔╝
 ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║     ██║   ██║██║   ██║██╔═══╝ 
 ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ███████╗╚██████╔╝╚██████╔╝██║     
  ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝                                                                             
"""

## Run the game loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    """
        Player Sprite Movement shit
    """
    # Get the pressed keys
    keys = pygame.key.get_pressed()

    # Move Player 1
    if keys[pygame.K_a]:
        P1_Collision = checkForHorizontalCollisions(P1.player_X - AOF.PLAYER_SPEED)
        if P1_Collision == False:
            P1.player_X -= AOF.PLAYER_SPEED
    if keys[pygame.K_d]:
        P1_Collision = checkForHorizontalCollisions(P1.player_X + AOF.PLAYER_SPEED)
        if P1_Collision == False:
            P1.player_X += AOF.PLAYER_SPEED
    if keys[pygame.K_w]:
        if P1.Standing == True:
            pygame.mixer.Channel(0).set_volume(0.05)
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('fight_sounds\sword-hit-in-battle.wav'))
            P1.Jumping = True
            P1.Standing = False
    
    if keys[pygame.K_LSHIFT]:
        if P1.Projectile == False:
            P1.Projectile = True
            P1_Spear_X = P1.player_X
            P1_Spear_Y = P1.player_Y
            P1_Spear = GameSprite('Projectiles\spear_LTR.png',
                                  (P1_Spear_X, P1_Spear_Y), AOF.Projectile_Smoothscale_Dimensions, False)

    # Move Player 2
    if keys[pygame.K_LEFT]:
        P2_Collision = checkForHorizontalCollisions(P2.player_X - AOF.PLAYER_SPEED)
        if P2_Collision == False:
            P2.player_X -= AOF.PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        P2_Collision = checkForHorizontalCollisions(P2.player_X + AOF.PLAYER_SPEED)
        if P2_Collision == False:
            P2.player_X += AOF.PLAYER_SPEED
    if keys[pygame.K_UP]:
        if P2.Standing == True:
            pygame.mixer.Channel(0).set_volume(0.05)
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('fight_sounds\sword-hit-in-battle.wav'))
            P2.Jumping = True
            P2.Standing = False
            
    if keys[pygame.K_RSHIFT]:
        if P2.Projectile == False:
            P2.Projectile = True
            P2_Spear_X = P2.player_X
            P2_Spear_Y = P2.player_Y
            P2_Spear = GameSprite('Projectiles\spear_RTL.png',
                                  (P2_Spear_X, P2_Spear_Y), AOF.Projectile_Smoothscale_Dimensions, False)
        

    ## "I want you to paint it, paint it, paint it black"
    screen.fill((0,0,0))

    ## Layering background image of map imagery
    screen.blit(BackGround.image, BackGround.rect)

    font = pygame.font.SysFont('Algerian',70)
    text = font.render("Art of War", 1,(255,255,255))

    screen.blit(text, (screenWidth/3,20))

    if tick % 2 == 0:
        if P1.idle_frame < P1.idle_frameCount - 1:
            P1.idle_frame += 1
        else:
            P1.idle_frame = 0

        if P2.idle_frame < P2.idle_frameCount - 1:
            P2.idle_frame += 1
        else:
            P2.idle_frame = 0


    ## Spawn player sprites
    if P1.Standing == True:
        P1_link = f'{P1.spriteObject["Action"]["Idle"]["imagePath"]}\{P1.idle_frame}.png'
        Player1 = GameSprite(P1_link, 
                             (P1.player_X, P1.player_Y), AOF.Default_Smoothscale_Dimensions, False)

    if P2.Standing == True:
        P2_link = f'{P2.spriteObject["Action"]["Idle"]["imagePath"]}\{P2.idle_frame}.png'
        Player2 = GameSprite(P2_link, 
                             (P2.player_X, P2.player_Y), AOF.Default_Smoothscale_Dimensions, True)


    ## Jumping and Descending for Player 1
    if P1.Jumping == True:
        P1_link = f'{P1.spriteObject["Action"]["Jump"]["imagePath"]}\{P1.jump_frame}.png'
        Player1 = GameSprite(P1_link, 
                             (P1.player_X, P1.player_Y), AOF.Default_Smoothscale_Dimensions, False)
        
        if P1.Descending == False:
            if P1.jump_frame < P1.jump_frameCount -1:
                P1.jump_frame += 1
            P1.player_Y -= AOF.VERTICAL_SPEED
            P1.Jump_Height += AOF.VERTICAL_SPEED

            if P1.Jump_Height == AOF.JUMP_HEIGHT:
                P1.Descending = True
        else:
            if P1.jump_frame > 0:
                P1.jump_frame -= 1
            P1.player_Y += AOF.PLAYER_SPEED
            P1.Jump_Height -= AOF.PLAYER_SPEED

            if P1.Jump_Height == 0:
                P1.Descending = False
                P1.Jumping = False
                P1.Standing = True
                P1.jump_frame = 0


    ## Jumping and Descending for Player 2
    if P2.Jumping == True:
        P2_link = f'{P2.spriteObject["Action"]["Jump"]["imagePath"]}\{P2.jump_frame}.png'
        Player2 = GameSprite(P2_link, 
                             (P2.player_X, P2.player_Y), AOF.Default_Smoothscale_Dimensions, True)

        if P2.Descending == False:
            if P2.jump_frame < P2.jump_frameCount -1:
                P2.jump_frame += 1
            P2.player_Y -= AOF.VERTICAL_SPEED
            P2.Jump_Height += AOF.VERTICAL_SPEED

            if P2.Jump_Height == AOF.JUMP_HEIGHT:
                P2.Descending = True
        else:
            if P2.jump_frame > 0:
                P2.jump_frame -= 1
            P2.player_Y += AOF.PLAYER_SPEED
            P2.Jump_Height -= AOF.PLAYER_SPEED

            if P2.Jump_Height == 0:
                P2.Descending = False
                P2.Jumping = False
                P2.Standing = True
                P2.jump_frame = 0


    ## Animation of Player 1's projectiles
    if P1.Projectile == True:
        P1_Spear_X += AOF.PROJECTILE_VELOCITY
        P1_Collision = checkForHorizontalCollisions(P1_Spear_X)
        
        if P1_Collision == False:
            P1_Spear = GameSprite('Projectiles\spear_LTR.png',
                                  (P1_Spear_X, P1_Spear_Y), AOF.Projectile_Smoothscale_Dimensions, False)
        else:
            P1_Projectile = False

    ## Animation of Player 2's projectiles
    if P2.Projectile == True:
        P2_Spear_X -= AOF.PROJECTILE_VELOCITY
        P2_Collision = checkForHorizontalCollisions(P2_Spear_X)
        
        if P2_Collision == False:
            P2_Spear = GameSprite('Projectiles\spear_RTL.png',
                                  (P2_Spear_X, P2_Spear_Y), AOF.Projectile_Smoothscale_Dimensions, False)
        else:
            P2.Projectile = False

    tick += 1

    pygame.display.update()

###################################################################################################