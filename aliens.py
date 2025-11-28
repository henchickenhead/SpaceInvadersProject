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
    def __init__(self, pattern, xpos, ypos):
        self.speed = 1
        self.isAtBottom = False
        self.tiles = game.sprite.Group() 
        self.tile_size = 3
        self.pattern = pattern
        self.bullet = AlienBulletPattern
        self.xpos = xpos
        self.ypos = ypos
        

    def build(self):
        ox, oy = self.xpos, self.ypos
        step = self.tile_size

        for r_idx, row in enumerate(self.pattern):
            for c_idx, cell in enumerate(row):
                if cell:
                    pos = (ox + c_idx * step, oy + r_idx * step)
                    tile = Alien(pos, size=step)
                    self.tiles.add(tile)

    def move(self):
        pass

class Aliens():
    def __init__(self, xpos =int , ypos = int ):
        self.xpos = xpos
        self.ypos = ypos
        self.alienClass = Alien((xpos, ypos))
        self.direction = True
        self.isBorderLeft = False
        self.isBorderRight = False
        self.createAliens()

    def createAliens(self):
        # create a 2D list (rows x cols) of AlienAbility instances
        rows = 5
        cols = 11
        self.alienArray = []
        temp = AlienAbility(AlienIconPattern1, self.xpos, self.ypos)
        spacing = 10 + temp.tile_size * 10
        for i in range(rows):
            row = []
            if i <= 2:
                for j in range(cols):
                    xpos = self.xpos + j * spacing
                    ypos = self.ypos + i * spacing
                    alien_ability = AlienAbility(AlienIconPattern1, xpos, ypos)
                    alien_ability.build()
                    row.append(alien_ability)
                self.alienArray.append(row)
            elif i >2 or i <=4:
                for j in range(cols):
                    xpos = self.xpos + j * spacing
                    ypos = self.ypos + i * spacing
                    alien_ability = AlienAbility(AlienIconPattern2, xpos, ypos)
                    alien_ability.build()
                    row.append(alien_ability)
                self.alienArray.append(row)
            else:
                for j in range(cols):
                    xpos = self.xpos + j * spacing
                    ypos = self.ypos + i * spacing
                    alien_ability = AlienAbility(AlienIconPattern3, xpos, ypos)
                    alien_ability.build()
                    row.append(alien_ability)
                self.alienArray.append(row)
        return self.alienArray
    
    def drawAliens(self):
        for alienRow in self.alienArray:
            for alien in alienRow:
                alien.build()
                alien.tiles.draw(game.display.get_surface())

    def shoot(self):
        pass

    def getShot(self):
        pass    
# next steps
# have the aliens array declared in a method here, maybe take in the parameters for the offsets

# # movement
# shooting
#disappearing when hit