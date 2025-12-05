import pygame

class Tile(pygame.sprite.Sprite): # Element used to build larger structures
  def __init__(self, pos, size=3, colour=(0, 255, 0)): # Puts a position, size and colour 
    super().__init__() # Sprite behaviour
    self.image = pygame.Surface((size, size)) # Square surface object with size paramenters
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
    self.build(pattern, origin) # method to build the tile layout

  def build(self, pattern, offset): # changing pattern into tile objects
    ox, oy = offset # x and y coordiates for where the shape should be at
    step = self.tile_size # for the pixel distance between tiles

    for r_idx, row in enumerate(pattern): # loops each row in the pattern then provides an index
      for c_idx, cell in enumerate(row): # loops each column in the row
        if cell: # checking if pattern cell is 1
          pos = (ox + c_idx * step, oy + r_idx * step) # finds out the pixel location where the shape should appear
          tile = Tile(pos, size=step) # creation of a tile object at a location
          self.tiles.add(tile) # puts a new tile to the sprite group
