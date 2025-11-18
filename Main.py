import shape
import sys
import pygame as game

# pygame setup
game.init()
screen = game.display.set_mode((1920, 1080))
clock = game.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False

    if event.type == game.KEYDOWN:
        if event.key == game.K_ESCAPE or event.key == game.K_x:
            print("Exiting game...")
            game.display.quit()
            running = False
        elif event.key == game.K_f:
            game.display.toggle_fullscreen()
    

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    my_shape = shape.Shape((100, 100), tile_size=5)
    my_shape.tiles.draw(screen)


    # flip() the display to put your work on screen
    game.display.flip()

    clock.tick(60)  # limits FPS to 60

game.quit()
sys.exit()
quit()
