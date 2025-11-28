import shape
import aliens
import sys
import pygame as game

# pygame setup
game.init()
screen = game.display.set_mode((800, 600))
clock = game.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False
        elif event.type == game.KEYDOWN:
            if event.key == game.K_ESCAPE or event.key == game.K_x:
                print("Exiting game...")
                running = False
            elif event.key == game.K_f:
                print("toggling fullscreen")
                game.display.toggle_fullscreen()
    

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    my_shape = shape.Shape((200, 800), tile_size=5)
    xpos, ypos = 100, 100
    my_shape.tiles.draw(screen)
    aliens_instance = aliens.Aliens(xpos, ypos)
    aliens_instance.drawAliens()

    #I will turn this into a 2d array loop later to reduce redundancy
    ufo = aliens.AlienAbility(aliens.AlienIconPattern4, xpos, 40)
    ufo.build()
    
    ufo.tiles.draw(screen)

    # update the display after all drawing is done
    game.display.flip()

    clock.tick(60)  # limits FPS to 60

game.quit()
sys.exit()
quit()
