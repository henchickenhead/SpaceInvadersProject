import pygame as game
import random


class Alien(game.sprite.Sprite): 
    def __init__(self, pos, size=40):
        super().__init__() 
        self.image = game.Surface((size, size))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect(topleft=pos) 
    
class Bullet(game.sprite.Sprite):
    def __init__(self, direction, xpos, ypos, speed=5, color=(255,255,0)):
        super().__init__()
        self.direction = direction
        self.speed = speed
        size = 7
        self.image = game.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(xpos, ypos))

    def move(self):
        dy = -self.speed if self.direction else self.speed
        self.rect.y += dy

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


class AlienAbility:
    def __init__(self, pattern, xpos, ypos):
        self.speed = 1
        self.isAlive = True
        self.direction = True
        self.isAtEdge = False
        self.tiles = game.sprite.Group() 
        self.tile_size = 3
        self.pattern = pattern
        self.xpos = xpos
        self.ypos = ypos
        self.score = 100
        self.bullet = Bullet
        self.count = 0
        

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
        if self.direction:
            dx = self.speed * 5 
        else:
            dx = -self.speed * 5
        self.xpos += dx
        for tile in self.tiles:
            tile.rect.x += dx
    
    def dropDown(self):
        self.ypos += 10 + self.tile_size * 10   
        for tile in self.tiles:
            tile.rect.y += 10 + self.tile_size * 10
        self.direction = not self.direction

    def shoot(self) -> Bullet:
        # create and return a Bullet instance positioned at this alien
        self.count += 1
        bx = int(self.xpos + (self.tile_size * len(self.pattern[0])) // 2)
        by = int(self.ypos + (self.tile_size * len(self.pattern) ) )
        return Bullet(False, bx, by)






class Aliens():
    def __init__(self ):
        self.screenDetails = game.display.Info().current_w, game.display.Info().current_h
        self.xpos = 100
        self.ypos = 100
        self.alienClass = Alien((self.xpos, self.ypos))
        self.direction = True
        self.isBorder = False
        self.canMove = True
        self.isShot = False
        # central bullets group for all alien bullets
        self.bullets = game.sprite.Group()
        self.createAliens()
        
    def borderCheck(self):
        for alienRow in self.alienArray:
            for alien in alienRow:
                if alien.xpos <= 100 or alien.xpos >= game.display.Info().current_w - 100:
                    print("Edge reached")
                    self.isBorder = True
                if alien.ypos >= game.display.Info().current_h - 175:
                    self.canMove = False
                    print("Aliens have landed!")
        if self.isBorder:
            for alienRow in self.alienArray:
                for alien in alienRow:
                    alien.dropDown()
                    alien.move()
            self.isBorder = False


    def createAliens(self):
        rows = 5
        cols = 11
        self.alienArray = []
        temp = AlienAbility(AlienIconPattern1, self.xpos, self.ypos)
        spacing = 10 + temp.tile_size * 10
        for i in range(rows):
            row = []
            if i < 1:
                for j in range(cols):
                    xpos = self.xpos + j * spacing
                    ypos = self.ypos + i * spacing
                    alien_ability = AlienAbility(AlienIconPattern1, xpos, ypos)
                    alien_ability.build()
                    row.append(alien_ability)
                self.alienArray.append(row)
            elif i >=1 and i <3:
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
        surface = game.display.get_surface()
        for alienRow in self.alienArray:
            for alien in alienRow:
                alien.tiles.draw(surface)
        for b in list(self.bullets):
            b.move()
            if b.rect.bottom < 0 or b.rect.top > surface.get_height():
                b.kill()
        self.bullets.draw(surface)

    def groupMove(self, counter=None):
        if self.canMove:
            for alienRow in self.alienArray:
                for alien in alienRow:
                    if counter is None:
                        alien.move()
                    else:
                        period = max(1, int(20 / alien.speed))
                        if counter % period == 0:
                            alien.move()
                    if random.randint(0, 1000) % 100 == 0:
                        self.shoot()
    
    def getBullets(self):
        return self.bullets

    def shoot(self):
        if len(self.bullets.sprites()) > 3:
            return
        cols = len(self.alienArray[0])
        attempts = 0
        while attempts < 10:
            col = random.randint(0, cols - 1)
            shooter = None
            for row in reversed(self.alienArray):
                a = row[col]
                if getattr(a, 'isAlive', True):
                    shooter = a
                    break
            if shooter:
                b = shooter.shoot()
                if b:
                    self.bullets.add(b)
                    return
            attempts += 1

    def getShot(self, bulletPosition):
        for alienRow in self.alienArray:
            for alien in alienRow:
                if bulletPosition.colliderect(alien.tiles.sprites()[0].rect):
                    alienRow.remove(alien)
                    print("Alien hit!")
                    self.isShot = True
                if self.isShot:
                    alien.speed += 0.2
                    self.isShot = False

# have the aliens array declared in a method here, maybe take in the parameters for the offsets


# # movement
# shooting
#disappearing when hit