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
from utilities import load_sprite, load_sprite_rotated, wrap_position
import utilities


UP = Vector2(0, -1)

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
 ███████╗██████╗  █████╗  ██████╗███████╗███████╗██╗  ██╗██╗██████╗ 
 ██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██║  ██║██║██╔══██╗
 ███████╗██████╔╝███████║██║     █████╗  ███████╗███████║██║██████╔╝
 ╚════██║██╔═══╝ ██╔══██║██║     ██╔══╝  ╚════██║██╔══██║██║██╔═══╝ 
 ███████║██║     ██║  ██║╚██████╗███████╗███████║██║  ██║██║██║     
 ╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝     
                                                                    
"""
class Spaceship:
    def __init__(self, smsc):
        self.Idle = True
        self.Thrust = False
        self.Shields = False
        self.RotateLeft = False
        self.RotateRight = False
        self.ShipSmoothscale = smsc
        self.MANEUVERABILITY = 3
        self.ACCELERATION = 0.25
        self.MAX_VELOCITY = 10
        self.ANGLE = 0
        self.direction = 90
        self.Idle_Frames = len(os.listdir("Assets\Sprites\Spaceships\Idle"))
        self.Idle_Frame = 0
        self.ImageLink = f'Assets\Sprites\Spaceships\Idle\{self.Idle_Frame}.png'
        self.ShipSpawnLocations = [(150,350),(600,600),(1000,500),(1500,500),
                                   (1600,700),(900,700),(1500,120),(150,150)]
        self.currentPosition = self.randomLocationSpawn()
        self.rect = self.ImageLink.get_rect(center=self.currentPosition)


    def calculate_new_xy(self, old_xy, speed, angle_in_degrees):
        move_vec = pygame.math.Vector2()
        move_vec.from_polar((speed, angle_in_degrees))
        return old_xy + move_vec
    
    def update(self):
        self.currentPosition = self.calculate_new_xy(self.currentPosition, 
                                                     self.MAX_VELOCITY, -self.direction)
        self.rect.center = round(self.pos[0]), round(self.pos[1])


    def rotate(self, clockwise=True):
        sign = 1 if clockwise else -1
        self.ANGLE += self.MANEUVERABILITY * sign

        if self.ANGLE > 360:
            self.ANGLE -= 360
        elif self.ANGLE < 0:
            self.ANGLE += 360

        self.update()

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
        self.Spaceship_Smoothscale = (80,80)
        self.FORWARD_ACCELEARATION = 20

    def getScreenSize(self):
        dimensions = (self.screenWidth, self.screenHeight)
        return dimensions
    
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

        ## Keys being held down
        elif event.type == pygame.KEYDOWN:
            ## Player key controls
            if event.key == pygame.K_LEFT:
                Player1_Spaceship.RotateLeft = True
            elif event.key == pygame.K_RIGHT:
                Player1_Spaceship.RotateRight = True
            elif event.key == pygame.K_UP:
                Player1_Spaceship.Thrust = True

        ## Keys being released
        elif event.type == pygame.KEYUP:
            ## Player key controls
            if event.key == pygame.K_LEFT:
                Player1_Spaceship.RotateLeft = False
            elif event.key == pygame.K_RIGHT:
                Player1_Spaceship.RotateRight = False
            elif event.key == pygame.K_UP:
                Player1_Spaceship.Thrust = False
                
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

    if Player1_Spaceship.Thrust == True:
        pass
    elif Player1_Spaceship.RotateLeft == True:
        Player1_Spaceship.rotate(clockwise=False)
    elif Player1_Spaceship.RotateRight == True:
        Player1_Spaceship.rotate(clockwise=True)

    Player1_Spaceship.draw(screen)

    if tick % 3 == 0:
        GC.updateFrames()
        Player1_Spaceship.updateFrames()

    tick += 1
    pygame.display.flip()
###################################################################################################