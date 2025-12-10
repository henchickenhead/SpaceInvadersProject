import shape
import aliens
import sys
import pygame as game

# pygame setup
game.init()

screen = game.display.set_mode((800, 700))
clock = game.time.Clock()
running = True
aliens_instance = aliens.Aliens()
my_shape = shape.ShapesManager()
counter = 0 

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False
        elif event.type == game.KEYDOWN:
            if event.key == game.K_ESCAPE or event.key == game.K_x:
                print('Exiting game...')
                running = False
            elif event.key == game.K_f:
                print("toggling fullscreen")
                game.display.toggle_fullscreen()
            elif event.key == game.K_SPACE:
                aliens_instance.shoot()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    bullets = aliens_instance.getBullets()
    # print(bullets)
    # RENDER YOUR GAME HERE
    my_shape.drawBarriers()
    my_shape.getShotAt(aliens_instance.getBullets())
    aliens_instance.drawAliens()
    aliens_instance.groupMove(counter)
    aliens_instance.borderCheck()


    ufo = aliens.AlienAbility(aliens.AlienIconPattern4, 100, 40)
    ufo.build()
    
    ufo.tiles.draw(screen)

    # update the display after all drawing is done
    game.display.flip()
    counter += 1
    clock.tick(60)  # limits FPS to 60

game.quit()
sys.exit()
quit()

