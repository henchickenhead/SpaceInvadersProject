import pygame

# Sprite groups to hold bullets fired by the player and enemyy
player_bullets = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()

# Small square sprite built using the Tile class with a position, size and colour
class Tile(pygame.sprite.Sprite):
  def __init__(self, pos, size=3, colour=(0, 255, 0)):
    super().__init__()
    self.image = pygame.Surface((size, size))
    self.image.fill(colour)
    self.rect = self.image.get_rect(topleft=pos)

pattern = [ # 2D list defining the tiles for the shape
  [0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0],
  [0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
  [0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
  [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], # 1 means place a tile and 0 means keep it empty
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1],
  [1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1],
  [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
]

# Barrier shape built from the pattern above
class Shape:
  def __init__(self, origin, pattern=pattern, tile_size=3):
    self.tiles = pygame.sprite.Group()
    self.tile_size = tile_size
    self.position = origin
    self.build(pattern, origin)

  def getPosition(self):
      return self.position

  # Changes the 2D pattern into tile sprites
  def build(self, pattern, offset):
    ox, oy = offset
    step = self.tile_size

    for r_idx, row in enumerate(pattern):
      for c_idx, cell in enumerate(row):
        if cell:
          pos = (ox + c_idx * step, oy + r_idx * step)
          tile = Tile(pos, size=step)
          self.tiles.add(tile)

class ShapesManager:
  def __init__(self):
      self.barriers = [pygame.sprite.Group()]
      self.positions = [(20, 500), (243, 500), (466, 500), (689, 500)]
      for pos in self.positions:
          shape = Shape(pos)
          self.barriers.append(shape)

  def drawBarriers(self):
      surface = pygame.display.get_surface()
      for blocks in self.barriers:
        if hasattr(blocks, 'tiles'):
          blocks.tiles.draw(surface)

  def getShotAt(self, alienbullets):
    for barrier in self.barriers:
      if hasattr(barrier, 'tiles'):
        for bullet in alienbullets:
          if pygame.sprite.spritecollide(bullet, barrier.tiles, dokill=True):
              bullet.kill()
              # barrier.tiles.destroy()
    for bullet in enemy_bullets:
        if pygame.sprite.spritecollide(bullet, barrier.tiles, dokill=True):
            bullet.kill()
            # barrier.tiles.destroy()

  #     else:
  #       for shape_tiles in self.barriers:
  #           for bullet in playerbullets:
  #               if pygame.sprite.spritecollide(bullet, shape_tiles, dokill=True):
  #                   bullet.kill()
  #                   shape_tiles.kill()
        # for bullet in player_bullets:
        # bullet.rect.y -= 5
        # if bullet.rect.bottom < 0:
        #     bullet.kill()

  # for bullet in player_bullets:
  #     bullet.rect.y -= 5 # This code controls the movement of player bullets and removes the bullet when off-screen
  #     if bullet.rect.bottom < 0:
  #         bullet.kill()
