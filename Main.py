import shape
import aliens
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
    my_shape.tiles.draw(screen)
    for j in range(11):
        alienLevel1 = aliens.AlienAbility(aliens.AlienIconPattern1)
        alienLevel1.build(200 + j * (10 + alienLevel1.tile_size *10),100)
        alienLevel1.tiles.draw(screen)
        alienLevel2 = aliens.AlienAbility(aliens.AlienIconPattern2)
        alienLevel2.build(200 + j * (10 + alienLevel2.tile_size *10), (100 + (10 + alienLevel2.tile_size *10)))
        alienLevel2.tiles.draw(screen)
        alienLevel3 = aliens.AlienAbility(aliens.AlienIconPattern2)
        alienLevel3.build(200 + j * (10 + alienLevel3.tile_size *10), (100 + 2*(10 + alienLevel3.tile_size *10)))
        alienLevel3.tiles.draw(screen)
        alienLevel4 = aliens.AlienAbility(aliens.AlienIconPattern3)
        alienLevel4.build(200 + j * (10 + alienLevel4.tile_size *10), (100 + 3*(10 + alienLevel4.tile_size *10)))
        alienLevel4.tiles.draw(screen)
        alienLevel5 = aliens.AlienAbility(aliens.AlienIconPattern3)
        alienLevel5.build(200 + j * (10 + alienLevel5.tile_size *10), (100 + 4*(10 + alienLevel5.tile_size *10)))
        alienLevel5.tiles.draw(screen)
    #I will turn this into a 2d array loop later to reduce redundancy
    #

    # update the display after all drawing is done
    game.display.flip()

    clock.tick(60)  # limits FPS to 60

game.quit()
sys.exit()
quit()
