import pygame

class Tile(pygame.sprite.Sprite): # Element used to build larger structures
  def __init__(self, pos, size=3, colour=(255, 0, 0)): # Puts a position, size and colour 
    super().__init__() # Sprite behaviour
    self.image = pygame.Surface((size, size)) # Square surface object with size paramenters
    self.image.fill(colour) # Tile colour
    self.rect - self.image.get_rect(topleft=pos) # Positioning of the tile

Pattern = [ # 2D list defining the tiles for the shape
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
    self.build(pattern, origin) # method to build the tile layout

def build(self, pattern, offset):
  ox, oy = offset
  step = self.tile_size

for r_idx, row in enumerate(pattern):
  for c_idx, cell in enumerate(row):
    if cell:
      pos = (ox + c_idx * step, oy + r_idx * step)
      tile = Tile(pos, size=step)
      self.tiles.add(tile)
