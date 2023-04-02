"""
    Author:   Byron Dowling, Deangelo Brown, Izzy Olaemimimo
    Class:    5443 2D Python Gaming

    Asset Credits:

        Space Environment Sprites:
            - Author: [FoozleCC]
            - https://foozlecc.itch.io/void-fleet-pack-2
            - https://foozlecc.itch.io/void-environment-pack
            - https://foozlecc.itch.io/void-main-ship 
            - https://norma-2d.itch.io/celestial-objects-pixel-art-pack

"""

import math
import pygame
import pprint
import random
import copy
import os
from PIL import Image, ImageDraw
from random import shuffle
from pygame.math import Vector2
from utilities import get_random_velocity, load_sprite, wrap_position
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
"""
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location, size):

        pygame.sprite.Sprite.__init__(self)
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
    def __init__(self, position, sprite, velocity):
        self.position = Vector2(position)
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.velocity = Vector2(velocity)

    def draw(self, surface):
        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)

    def move(self, surface):
        self.position = wrap_position(self.position + self.velocity, surface)

    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius

###################################################################################################
"""
 ███████╗██████╗  █████╗  ██████╗███████╗███████╗██╗  ██╗██╗██████╗ 
 ██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██║  ██║██║██╔══██╗
 ███████╗██████╔╝███████║██║     █████╗  ███████╗███████║██║██████╔╝
 ╚════██║██╔═══╝ ██╔══██║██║     ██╔══╝  ╚════██║██╔══██║██║██╔═══╝ 
 ███████║██║     ██║  ██║╚██████╗███████╗███████║██║  ██║██║██║     
 ╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝     
                                                                    
"""
class Spaceship(GameSprite):
    def __init__(self, smsc):
        self.Idle = True
        self.Thrust = False
        self.Shields = False
        self.ShipSmoothscale = smsc
        self.MANEUVERABILITY = 3
        self.Idle_Frames = len(os.listdir("Assets\Sprites\Spaceships\Idle"))
        self.Idle_Frame = 0
        self.ImageLink = f'Assets\Sprites\Spaceships\Idle\{self.Idle_Frame}.png'
        self.Shield_Frames = len(os.listdir("Assets\Sprites\Shields"))
        self.Shield_Frame = 0
        self.ShipSpawnLocations = [(150,350),(600,600),(1000,500),(1500,500),
                                   (1600,700),(900,700),(1500,120),(150,150)]
        self.startingPoint = self.randomLocationSpawn()
        self._Xcord = self.startingPoint[0]
        self._Ycord = self.startingPoint[1]
        self.spriteObject = load_sprite(self.ImageLink, self.ShipSmoothscale)

        GameSprite.__init__(self, self.startingPoint, self.spriteObject, Vector2(0))

    def rotate(self, clockwise=True):
        sign = 1 if clockwise else -1
        angle = self.MANEUVERABILITY * sign
        self.direction.rotate_ip(angle)

    def randomLocationSpawn(self):
        shuffle(self.ShipSpawnLocations)
        selection = []
        selection.append(self.ShipSpawnLocations[0])
        print(selection[0])
        return selection[0]
    
    def updateFrames(self):
        if self.Idle_Frame < self.Idle_Frames - 1:
            self.Idle_Frame += 1
        else:
            self.Idle_Frame = 0

    def updateSpaceship(self):
        self.ImageLink = f'Assets\Sprites\Spaceships\Idle\{self.Idle_Frame}.png'
        self.spriteObject = load_sprite(self.ImageLink, self.ShipSmoothscale)

        ## Invoking the gamesprite member variable
        self.sprite = self.spriteObject

###################################################################################################
"""
  █████╗ ███████╗████████╗███████╗██████╗  ██████╗ ██╗██████╗ 
 ██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗██╔═══██╗██║██╔══██╗
 ███████║███████╗   ██║   █████╗  ██████╔╝██║   ██║██║██║  ██║
 ██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗██║   ██║██║██║  ██║
 ██║  ██║███████║   ██║   ███████╗██║  ██║╚██████╔╝██║██████╔╝
 ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝╚═════╝ 
                                                              
"""
class Asteroid(GameSprite):
    def __init__(self, location, smsc_dimensions):
        self.IdleImageLink = r"Assets\Sprites\Asteroids\Explosion\0.png"
        self.Explosion_Frames = len(os.listdir("Assets\Sprites\Asteroids\Explosion"))
        self.Explosion_Frame = 0
        self.InOrbit = True
        self.Smoothscale=smsc_dimensions

        self.spriteObject = load_sprite(self.IdleImageLink, self.Smoothscale)

        GameSprite.__init__(self, location, self.spriteObject, Vector2(0))

    def drawAsteroid(self, screen):
        GameSprite.draw(self, screen)

    def destroy(self):
        pass


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

## Keeps sprites from going too far off screen
def checkForHorizontalCollisions(currentX):
    if currentX <= 50:
        return True
    elif currentX >= (screenWidth - 225):
        return True
    else:
        return False

## Mask Collision Detection between Sprites and Projectiles
def checkForAsteroidCollision(sprite, projectile):
    result = pygame.sprite.collide_mask(sprite.playerMain, projectile.playerMain)
    if result != None:
        return True
    else:
        return False
    
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
        self.screen = pygame.display.set_mode((screenWidth, screenHeight))
        self.BG_Frames = len(os.listdir("Assets/Background/Stars"))
        self.BG_Frame = 0
        self.RS_Frames = len(os.listdir("Assets/Background/RotaryStar"))
        self.RS_Frame = 0
        self.BH_Frames = len(os.listdir("Assets/Background/BH"))
        self.BH_Frame = 0
        self.Default_Smoothscale_Dimensions = (200,200)
        self.Asteroid_Smoothscale = (150,150)
        self.Spaceship_Smoothscale = (80,80)
        self.FORWARD_ACCELEARATION = 20
        self.MIN_ASTEROID_DISTANCE = 250

        self.Locations = [(100,150),(300,300),(800,400),(1300,200),
                                   (1100,600),(700,700),(1500,620),(650,450),
                                   (1700,850),(800,800),(100,620),(150,450),
                                   (1700,100),(100,800),(1100,120),(150,1000)]
        self.AsteroidCount = 8
        self.Asteroids = []

        shuffle(self.Locations)

        for i in range(self.AsteroidCount):
            position = self.Locations[i]
            temp = Asteroid(position, self.Asteroid_Smoothscale)
            self.Asteroids.append(temp)


    def getScreenSize(self):
        dimensions = (self.screenWidth, self.screenHeight)
        return dimensions
    
    def drawAsteroids(self):
        for AST in self.Asteroids:
            AST.drawAsteroid(self.screen)
    
    def updateFrames(self):
        if self.BG_Frame < self.BG_Frames - 1:
            self.BG_Frame += 1
        else:
            self.BG_Frame = 0

        if self.RS_Frame < self.RS_Frames - 1:
            self.RS_Frame += 1
        else:
            self.RS_Frame = 0

        if self.BH_Frame < self.BH_Frames - 1:
            self.BH_Frame += 1
        else:
            self.BH_Frame = 0
        
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

## Rough Dimensions of Byron's Monitor
screenWidth = 1750
screenHeight = 900

GC = GameController(screenWidth, screenHeight)
screen = pygame.display.set_mode((GC.screenWidth, GC.screenHeight))

tick = 0

Player1_Spaceship = Spaceship((85,85))

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
while GC.Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GC.Running = False

    keys = pygame.key.get_pressed()

    ## Player key controls
    if keys[pygame.K_LEFT]:
        pass
    if keys[pygame.K_RIGHT]:
        pass
    if keys[pygame.K_UP]:
        Player1_Spaceship.Thrust = True
        Player1_Spaceship._Ycord -= 20
    if keys[pygame.K_DOWN]:
        Player1_Spaceship._Ycord += 20
    if keys[pygame.K_RSHIFT]:
        if Player1_Spaceship.Shields==False:
            Player1_Spaceship.Shields=True

    screen.fill((0,0,0))

    ## Background shit
    StarryBackground = Background(f"Assets/Background/Stars/{GC.BG_Frame}.png", [0, 0], (screenWidth, screenHeight))
    GC.screen.blit(StarryBackground.image, StarryBackground.rect)

    RotaryStar1 = Background(f'Assets/Background/RotaryStar/{GC.RS_Frame}.png', [210,500], (100,100))
    GC.screen.blit(RotaryStar1.image, RotaryStar1.rect)

    RotaryStar2 = Background(f'Assets/Background/RotaryStar/{GC.RS_Frame}.png', [1610,110], (100,100))
    GC.screen.blit(RotaryStar2.image, RotaryStar2.rect)

    Blackhole = Background(f'Assets/Background/BH/{GC.BH_Frame}.png', [815,350], (150,150))
    GC.screen.blit(Blackhole.image, Blackhole.rect)

    
    Player1_Spaceship.draw(screen)
    GC.drawAsteroids()

    """
        Notes:

            Need to make a Shield object along with the engine object and make them
            parameters of the spaceship class. We will use the main loop to call the 
            update frames methods and then call the draw method for the ship and engine
            and then the shield if the key is held down.
    """

    # if Player1.Thrust == True:
    #     Ship_Effect = GameSprite(fr"Assets\Sprites\Spaceships\Idle\0.png", [Player1._Xcord,Player1._Ycord + 40], (25,10))
    #     Ship.draw()
    #     Ship_Effect.draw()

    # else:
    #     if Player1.Shields == True:
    #         Ship_Effect = GameSprite(f"Assets\Sprites\Spaceships\Idle\{Player1.Engine_Idle_Frame}.png", [Player1._Xcord,Player1._Ycord + 40], (25,10))
    #         Shield = GameSprite(f"Assets\Sprites\Shields\{Player1.Shield_Frame}.png", [Player1._Xcord,Player1._Ycord], (115,115))
    #         Ship.draw()
    #         Ship_Effect.draw()
    #         Shield.draw()

    #     else:
    #         Ship_Effect = GameSprite(f"Assets\Sprites\Spaceships\Idle\{Player1.Engine_Idle_Frame}.png", [Player1._Xcord,Player1._Ycord + 40], (25,10))
    #         Ship.draw()
    #         Ship_Effect.draw()

    if tick % 3 == 0:
        GC.updateFrames()
        Player1_Spaceship.updateFrames()
        Player1_Spaceship.updateSpaceship()

    # if tick % 4 == 0:
    #     Player1.updateFrames()


    ## Reset thrusters and shields so the key must be held down
    # Player1.Thrust = False
    # Player1.Shields = False
    tick += 1
    pygame.display.flip()
###################################################################################################