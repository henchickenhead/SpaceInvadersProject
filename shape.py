import pygame


player_bullets = pygame.sprite.Group() # Sprite Group to hold bullets fired by the player
enemy_bullets = pygame.sprite.Group() # Sprite Group to hold bullets fired by the enemy

class Tile(pygame.sprite.Sprite): # Element used to build larger structures
  def __init__(self, pos, size=3, colour=(0, 255, 0)): # Puts a position, size and colour 
    super().__init__() # Sprite behaviour
    self.image = pygame.Surface((size, size)) # Square surface object with size parameters
    self.image.fill(colour) # Tile colour
    self.rect = self.image.get_rect(topleft=pos) # Positioning of the tile

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

class Shape: # class based on a pattern
  def __init__(self, origin, pattern=pattern, tile_size=3): # creates a shape using the pattern and tile size
    self.tiles = pygame.sprite.Group() # groups all the tiles that make the shape
    self.tile_size = tile_size # used to calculate tile spacing
    self.position = origin # position of the shape
    self.build(pattern, origin) # method to build the tile layout

  def getPosition(self):
      return self.position

  def build(self, pattern, offset): # changing pattern into tile objects
    ox, oy = offset # x and y coordiates for where the shape should be at
    step = self.tile_size # for the pixel distance between tiles

    for r_idx, row in enumerate(pattern): # loops each row in the pattern then provides an index
      for c_idx, cell in enumerate(row): # loops each column in the row
        if cell: # checking if pattern cell is 1
          pos = (ox + c_idx * step, oy + r_idx * step) # finds out the pixel location where the shape should appear
          tile = Tile(pos, size=step) # creation of a tile object at a location
          self.tiles.add(tile) # puts a new tile to the sprite group

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