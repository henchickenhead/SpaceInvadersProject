import Aliens
import Player
import Blocks
import pygame as game

# pygame setup
game.init()
screen = game.display.set_mode((1280, 720))
clock = game.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    game.display.flip()

    clock.tick(60)  # limits FPS to 60

game.quit()