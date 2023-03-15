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

## Initialize Pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()
utilities.background_music()
running = True

## Rough Dimensions of Byron's Monitor
screenWidth = 1750
screenHeight = 800

## Alternative smaller setup
# screenWidth = 1400
# screenHeight = 700

## Set the size of the window using the above dimensions
size = (screenWidth, screenHeight)
screen = pygame.display.set_mode(size)

## Setting the background image and orienting starting from (0,0) origin i.e top left corner
# BackGround = Background("Arena.jpg", [0, 0])
BackGround = Background("Arena_Night.jpg", [0, 0], (screenWidth, screenHeight))


"""
    Pseudo-random player selection, may eventually switch to player selection screen

        Grabs the # of frames for idle movement and the name of the sprite
"""
C4 = PlayerSelector()
sprites = C4.chooseSprites()
P1 = sprites[0]
P2 = sprites[1]

P1_idle_frameCount = P1["Action"]["Idle"]["frameCount"]
P1_jump_frameCount = P1["Action"]["Jump"]["frameCount"]
P1_idle_frame = 0
P1_jump_frame = 0
P1_name = P1["Screen Name"]

P2_idle_frameCount = P2["Action"]["Idle"]["frameCount"]
P2_jump_frameCount = P2["Action"]["Jump"]["frameCount"]
P2_idle_frame = 2
P2_jump_frame = 0
P2_name = P2["Screen Name"]

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(sprites)

## Get System Font Info
# pp.pprint(pygame.font.get_fonts())

## Default Player Variables to get ball rolling
## Smaller Dimension settings
# Player1_StartingPosition = (80,300)
# Player2_StartingPosition = (1100,300)
# Default_Smoothscale_Dimensions = (250,250)

## Default Player Variables to get ball rolling
Player1_StartingPosition = (350,500)
Player2_StartingPosition = (1350,500)
Default_Smoothscale_Dimensions = (250,250)
Project_Smoothscale_Dimensions = (150,50)

## Movement Variables
PLAYER_SPEED = 10
VERTICAL_SPEED = 15
JUMP_HEIGHT = 150

player1_x = Player1_StartingPosition[0]
player1_y = Player1_StartingPosition[1]
player2_x = Player2_StartingPosition[0]
player2_y = Player2_StartingPosition[1]

P1_Standing = True
P1_Jumping = False
P1_Descending = False
P1_Jump_Height = 0

P2_Standing = True
P2_Jumping = False
P2_Descending = False
P2_Projectile = False
P2_Jump_Height = 0


## Set the title of the window
banner = f'Get Ready for Deadliest Warrior! {P1_name} vs {P2_name}'
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
                                                                   
  ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗                          
 ██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝                          
 ██║     ███████║█████╗  ██║     █████╔╝                           
 ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗                           
 ╚██████╗██║  ██║███████╗╚██████╗██║  ██╗                          
  ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝                          
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

    # Move the players
    if keys[pygame.K_a]:
        P1_Collision = checkForHorizontalCollisions(player1_x - PLAYER_SPEED)
        if P1_Collision == False:
            player1_x -= PLAYER_SPEED
    if keys[pygame.K_d]:
        P1_Collision = checkForHorizontalCollisions(player1_x + PLAYER_SPEED)
        if P1_Collision == False:
            player1_x += PLAYER_SPEED
    if keys[pygame.K_w]:
        if P1_Standing == True:
            pygame.mixer.Channel(0).set_volume(0.05)
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('fight_sounds\sword-hit-in-battle.wav'))
            P1_Jumping = True
            P1_Standing = False
    
    if keys[pygame.K_s]:
        pass
        # player1_y += PLAYER_SPEED

    if keys[pygame.K_LEFT]:
        P2_Collision = checkForHorizontalCollisions(player2_x - PLAYER_SPEED)
        if P2_Collision == False:
            player2_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        P2_Collision = checkForHorizontalCollisions(player2_x + PLAYER_SPEED)
        if P2_Collision == False:
            player2_x += PLAYER_SPEED
    if keys[pygame.K_UP]:
        if P2_Standing == True:
            pygame.mixer.Channel(0).set_volume(0.05)
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('fight_sounds\sword-hit-in-battle.wav'))
            P2_Jumping = True
            P2_Standing = False
            
    if keys[pygame.K_DOWN]:
        if P2_Projectile == False:
            P2_Projectile = True
            P2_Spear_X = player2_x
            P2_Spear_Y = player2_y
            P2_Spear = GameSprite('Projectiles\spear_RTL.png', (P2_Spear_X, P2_Spear_Y), Project_Smoothscale_Dimensions, False)
        

    ## "I want you to paint it, paint it, paint it black"
    screen.fill((0,0,0))

    ## Layering background image of map imagery
    screen.blit(BackGround.image, BackGround.rect)

    font = pygame.font.SysFont('Algerian',70)
    text = font.render("Art of War", 1,(255,255,255))

    screen.blit(text, (500,20))

    if tick % 4 == 0:
        if P1_idle_frame < P1_idle_frameCount - 1:
            P1_idle_frame += 1
        else:
            P1_idle_frame = 0

        if P2_idle_frame < P2_idle_frameCount - 1:
            P2_idle_frame += 1
        else:
            P2_idle_frame = 0


    ## Spawn player sprites
    if P1_Standing == True:
        P1_link = f'{P1["Action"]["Idle"]["imagePath"]}\{P1_idle_frame}.png'
        Player1 = GameSprite(P1_link, (player1_x, player1_y), Default_Smoothscale_Dimensions, False)

    if P2_Standing == True:
        P2_link = f'{P2["Action"]["Idle"]["imagePath"]}\{P2_idle_frame}.png'
        Player2 = GameSprite(P2_link, (player2_x, player2_y), Default_Smoothscale_Dimensions, True)


    ## Jumping and Descending for Player 1
    if P1_Jumping == True:
        P1_link = f'{P1["Action"]["Jump"]["imagePath"]}\{P1_jump_frame}.png'
        Player1 = GameSprite(P1_link, (player1_x, player1_y), Default_Smoothscale_Dimensions, False)
        
        if P1_Descending == False:
            if P1_jump_frame < P1_jump_frameCount -1:
                P1_jump_frame += 1
            player1_y -= VERTICAL_SPEED
            P1_Jump_Height += VERTICAL_SPEED

            if P1_Jump_Height == JUMP_HEIGHT:
                P1_Descending = True
        else:
            if P1_jump_frame > 0:
                P1_jump_frame -= 1
            player1_y += PLAYER_SPEED
            P1_Jump_Height -= PLAYER_SPEED

            if P1_Jump_Height == 0:
                P1_Descending = False
                P1_Jumping = False
                P1_Standing = True
                P1_jump_frame = 0


    ## Jumping and Descending for Player 2
    if P2_Jumping == True:
        P2_link = f'{P2["Action"]["Jump"]["imagePath"]}\{P2_jump_frame}.png'
        Player2 = GameSprite(P2_link, (player2_x, player2_y), Default_Smoothscale_Dimensions, True)

        if P2_Descending == False:
            if P2_jump_frame < P2_jump_frameCount -1:
                P2_jump_frame += 1
            player2_y -= VERTICAL_SPEED
            P2_Jump_Height += VERTICAL_SPEED

            if P2_Jump_Height == JUMP_HEIGHT:
                P2_Descending = True
        else:
            if P2_jump_frame > 0:
                P2_jump_frame -= 1
            player2_y += PLAYER_SPEED
            P2_Jump_Height -= PLAYER_SPEED

            if P2_Jump_Height == 0:
                P2_Descending = False
                P2_Jumping = False
                P2_Standing = True
                P2_jump_frame = 0


    ## Animation of Player 2's projectiles
    if P2_Projectile == True:
        P2_Spear_X -= PROJECTILE_VELOCITY
        P2_Collision = checkForHorizontalCollisions(P2_Spear_X)
        
        if P2_Collision == False:
            P2_Spear = GameSprite('Projectiles\spear_RTL.png', (P2_Spear_X, P2_Spear_Y), Project_Smoothscale_Dimensions, False)
        else:
            P2_Projectile = False

    tick += 1

    pygame.display.update()

###################################################################################################