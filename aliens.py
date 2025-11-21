import pygame as game

class Alien(game.sprite.Sprite): 
    def __init__(self, pos, size=40):
        super().__init__() 
        self.image = game.Surface((size, size))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect(topleft=pos) 
    
AlienIconPattern1 = [
    [0,0,1,0,0,0,0,1,0,0],
    [0,1,0,1,0,0,1,0,1,0],
    [0,1,0,0,1,1,0,0,1,0],
    [0,1,0,0,1,1,0,0,1,0],
    [0,1,0,0,1,1,0,0,1,0],
    [0,1,1,1,1,1,1,1,1,0],
    [1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,1,1,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1],
    [0,1,1,1,0,0,1,1,1,0]
]

AlienIconPattern2 = [
    [0,1,0,0,0,0,0,0,1,0],
    [0,1,1,0,0,0,0,1,1,0],
    [0,1,0,1,0,0,1,0,1,0],
    [0,1,0,0,1,1,0,0,1,0],
    [0,1,0,0,0,0,0,0,1,0],
    [0,1,1,1,1,1,1,1,1,0],
    [0,1,0,0,0,0,0,0,1,0],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

AlienIconPattern3 = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,1,0,0,1,0,0,0],
    [0,0,1,0,1,1,0,1,0,0],
    [0,1,0,0,0,0,0,0,1,0],
    [0,1,0,0,0,0,0,0,1,0],
    [0,1,1,1,1,1,1,1,1,0],
    [1,1,1,1,1,1,1,1,1,1],
    [0,0,0,0,1,1,0,0,0,0],
    [0,0,0,0,1,1,0,0,0,0],
    [0,0,0,1,1,1,1,0,0,0]
]

AlienIconPattern4 = [
    [0,0,0,1,1,1,1,0,0,0],
    [0,0,1,0,0,0,0,1,0,0],
    [0,0,1,0,1,1,0,1,0,0],
    [0,1,0,0,0,0,0,0,1,0],
    [1,1,1,1,1,1,1,1,1,1],
    [0,1,1,1,1,1,1,1,1,0],
    [1,0,1,0,1,1,0,1,0,1]
]

AlienBulletPattern = [
    [0,1,0],
    [0,1,0],
    [0,1,0]
]

class AlienAbility:
    def __init__(self, pattern):
        self.speed = 1
        self.direction = True
        self.isBorderLeft = False
        self.isBorderRight = False
        self.isAtBottom = False
        self.tiles = game.sprite.Group() 
        # increase tile size so the alien icon is visible on screen
        self.tile_size = 6
        self.pattern = pattern
        self.bullet = AlienBulletPattern
        

    def build(self, offsetX: int, offsetY: int):
        ox, oy = offsetX, offsetY
        step = self.tile_size

        for r_idx, row in enumerate(self.pattern):
            for c_idx, cell in enumerate(row):
                if cell:
                    pos = (ox + c_idx * step, oy + r_idx * step)
                    tile = Alien(pos, size=step)
                    self.tiles.add(tile)

    
# next steps
# movement
# shooting
#disappearing when hit