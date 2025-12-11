# from select import poll
# import shape
# import aliens
# import sys
# import pygame as game

# # pygame setup
# game.init()

# screen = game.display.set_mode((800, 700))
# clock = game.time.Clock()
# running = True
# aliens_instance = aliens.Aliens()
# my_shape = shape.ShapesManager()
# counter = 0 

# while running:
#     for event in game.event.get():
#         if event.type == game.QUIT:
#             running = False
#         elif event.type == game.KEYDOWN:
#             if event.key == game.K_ESCAPE or event.key == game.K_x:
#                 print('Exiting game...')
#                 running = False
#             elif event.key == game.K_f:
#                 print("toggling fullscreen")
#                 game.display.toggle_fullscreen()
#             elif event.key == game.K_SPACE:
#                 aliens_instance.shoot()

#     screen.fill("black")
#     bullets = aliens_instance.getBullets()
#     print(bullets)
#     my_shape.drawBarriers()
#     my_shape.getShotAt(aliens_instance.getBullets())
#     aliens_instance.drawAliens()
#     aliens_instance.groupMove(counter)
#     aliens_instance.borderCheck()


#     ufo = aliens.AlienAbility(aliens.AlienIconPattern4, 100, 40)
#     ufo.build()
    
#     ufo.tiles.draw(screen)

#     game.display.flip()
#     counter += 1
#     clock.tick(60)  # limits FPS to 60

# game.quit()
# sys.exit()
# quit()











































































import pygame
pygame.init()
import random
import shape
import aliens

# Initialize game objects
aliens_instance = aliens.Aliens()
my_shape = shape.ShapesManager()
counter = 0

#------------------------These are the classes for the gun platform and bullets (by Tris)----------
# The Gun Platform object will be added to a sprite group called gun_platform_sprites.
# The gun platform will create bullet sprites  when the gun is fired and add them to the
# bullet_sprites group.
#
# The gun platform will detect if it has collided with a sprite in the bomb_sprites group and explode
# if it has. It will remove bomb from the group when this happens.
#
# The gun platform will detect if it has collided with a sprite in the spaceinvader_sprites group and
# explode if it has. This will end the game. This should all take place in a method called Update()
#
# The bullets will be removed from the bullet_sprites group if they go off the top of the screen
#
####################################################################################################
class Life(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # You have to initialise the super class first
        super().__init__()
        # Set the sprite's image (this returns a surface for the sprite stored in self.image attribute)
        self.image = pygame.image.load('Images/GunPlatform_g.png')
        # Get a Rectangle that locates the size and position of the surface. Defaults location to 0,0
        self.rect = self.image.get_rect()
        # Set X and Y co-ordinates
        self.rect.x = x
        self.rect.y = y

class GameOver(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # You have to initialise the super class first
        super().__init__()
        # Set the sprite's image (this returns a surface for the sprite stored in self.image attribute)
        self.image = pygame.image.load('Images/GameOver.png')
        # Get a Rectangle that locates the size and position of the surface. Defaults location to 0,0
        self.rect = self.image.get_rect()
        # Set X and Y co-ordinates
        self.rect.x = x
        self.rect.y = y

#Class to represent Gun Platform
# Takes to integer arguments for X and Y co-ordinates
class GunPlatform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        #You have to initialise the super class first
        super().__init__()
        # Set the sprite's image (this returns a surface for the sprite stored in self.image attribute)
        self.image = pygame.image.load('Images/GunPlatform_g.png')
        # Get a Rectangle that locates the size and position of the surface. Defaults location to 0,0
        self.rect = self.image.get_rect()
        #Set X and Y co-ordinates
        self.start_x = x
        self.start_y = y
        self.rect.x = x
        self.rect.y = y
        self.alive = True
        self.animation_timer = 0
        self.num_lives = 3
    def isAlive(self):
        return self.alive
    def livesLeft(self):
        return self.num_lives
    def resurrectPlatform(self):
        self.alive = True
        self.image = pygame.image.load('Images/GunPlatform_g.png')
        self.rect.x = self.start_x
        self.rect.y = self.start_y
        self.animation_timer = 0
    def moveRight(self, pixels):
        if self.rect.x < 765:
            self.rect.x += pixels
    def moveLeft(self, pixels):
        if self.rect.x > 5:
            self.rect.x -= pixels
    def shootBullet(self):
        b = Bullet(self.rect.x + 16, self.rect.y + 16)
        bullet_sprites.add(b)
    def animateExplosion(self):
        self.image = pygame.image.load('Images/Explode1.png')
        self.alive = False
    def update(self):
        if self.alive == True:
            bomb_list = pygame.sprite.spritecollide(self, bomb_sprites, False)
            if bomb_list:
                bomb_list[0].kill()
                self.animateExplosion()
        else:
            if self.animation_timer >= 1000:
                match self.num_lives:
                    case 3:
                        Life2.kill()
                        self.num_lives -= 1
                        self.resurrectPlatform()
                    case 2:
                        Life1.kill()
                        self.num_lives -= 1
                        self.resurrectPlatform()
                    case 1:
                        self.num_lives -= 1
            elif 60 <= self.animation_timer < 1000:
                self.image = pygame.image.load('Images/Explode3.png')
                self.animation_timer += 10
            elif 30 <= self.animation_timer < 60:
                self.image = pygame.image.load('Images/Explode2.png')
                self.animation_timer += 10
            elif 0 <= self.animation_timer < 30:
                self.image = pygame.image.load('Images/Explode1.png')
                self.animation_timer += 10

#Class to represent A bullet
# Takes to integer arguments for X and Y co-ordinates
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        #You have to initialise the super class first
        super().__init__()
        # Set the sprite's image (this returns a surface for the sprite stored in self.image attribute)
        self.image = pygame.image.load('Images/bullet_gs1.png')
        # Get a Rectangle that locates the size and position of the surface. Defaults location to 0,0
        self.rect = self.image.get_rect()
        #Set X and Y co-ordinates
        self.rect.x = x
        self.rect.y = y
        self.bulletspeed = 5
    def moveUp(self):
        self.rect.y -= self.bulletspeed
        if self.rect.y < 0:
            self.kill()
    def update(self):
        killed_alien_list = []
        killed_alien_list.append(aliens_instance.getShot(self))
        if killed_alien_list != [None]: 
            self.kill()
        else:
            self.moveUp()


## #------------------------These are the classes for the Barrier  (by Dylan)----------
# The barrier objects must be added to a sprite group called barrier_sprites
# The barrier objects must detect if they have collided with any sprites in the following groups:
#  bullet_spites
#  bomb_sprites
#  spaceinvader_sprites
# and disintegrate if they have. This should all take place in a method called Update()
#
# ####################################################################################################--------
#-------------------------------End of classes ------------------------------------
#
#


# Initialise the game - all the stuff we do once at the start
# Open a new window and set up the screen for display
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)
SI_Start_x = 30
SI_Start_y = 30

screen_size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen_surface = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Space Invaders")

# Create sprite groups
gun_platform_sprites = pygame.sprite.Group()
bullet_sprites = pygame.sprite.Group()
spaceinvader_sprites = aliens_instance.alienArray
bomb_sprites = aliens_instance.getBullets()
life_sprites = pygame.sprite.Group()
game_over_sprites = pygame.sprite.Group()

# Henry needs to create space invaders here and add then to the spaceinvader_sprites group


# Tris creates Gun Platform and add it to the gun_platform_sprites group
gun_platform = GunPlatform(SCREEN_WIDTH-250, SCREEN_HEIGHT-80)
gun_platform_sprites.add(gun_platform)

# Dylan has to create the shield objects and add them to the barrier_sprites group
# Dylan's code for this goes here



#Tris Create the player lives
num_lives = 2
Life1 = Life(20, SCREEN_HEIGHT-40)
Life2 = Life(70, SCREEN_HEIGHT - 40)
life_sprites.add(Life1)
life_sprites.add(Life2)

#Tris Create the game over sprite
game_over = GameOver(SCREEN_WIDTH/2-30, SCREEN_HEIGHT/2-30)
game_over_sprites.add(game_over)

# The clock will be used to control how fast the screen updates in fps
clock = pygame.time.Clock()

#-------------------------------End of game initialisation------------------------------

#Create the game Loop to check for events
running = True
while running:
    #Draw the screen
    #First draw the background using an image file
    background = pygame.image.load("Images/StarField.png")
    screen_surface.blit(pygame.transform.scale(background,screen_size), (0, 0))
    #Then draw the baseline and player lives
    pygame.draw.line(screen_surface,GREEN,(0,SCREEN_HEIGHT-40),(SCREEN_WIDTH,SCREEN_HEIGHT-40))

    # Tris's code as only the gun platform interacts wit the user
    # Now check for events (QUIT or fire button pressed)
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                running = False
            case pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_x:
                    print('Exiting game...')
                    running = False
                match event.key:
                    # Fire button
                    case pygame.K_SPACE:
                        if gun_platform.isAlive():
                            gun_platform.shootBullet()


    bullets = aliens_instance.getBullets()
    # print(bullets)
    # RENDER YOUR GAME HERE
    my_shape.drawBarriers()
    my_shape.getShotAt(aliens_instance.getBullets())
    my_shape.getShotAt(bullet_sprites)
    aliens_instance.drawAliens()
    aliens_instance.groupMove(counter)
    aliens_instance.borderCheck()
    # aliens_instance.getShot(bullet_sprites  )
    counter+=1
    # Tris's code
    # Check if the gun platform is being moved (L or R arrow keys are being pressed)
    keys_pressed = pygame.key.get_pressed()
    if gun_platform.isAlive():
        if keys_pressed[pygame.K_LEFT]:
            gun_platform.moveLeft(5)
        if keys_pressed[pygame.K_RIGHT]:
            gun_platform.moveRight(5)
    # Check if no lives left
    if gun_platform.livesLeft() == 0 or aliens_instance.getGameOver():
        screen_surface.blit(pygame.transform.scale(background,screen_size), (0, 0))
        game_over_sprites.draw(screen_surface)
        pygame.display.update()
    else:
        # Update sprites
        bullet_sprites.update()
        gun_platform.update()
        bomb_sprites.update()

        # Draw all sprites
        gun_platform_sprites.draw(screen_surface)
        bullet_sprites.draw(screen_surface)
        bomb_sprites.draw(screen_surface)
        life_sprites.draw(screen_surface)
        pygame.display.update()

        clock.tick(60)

pygame.quit()
quit()
