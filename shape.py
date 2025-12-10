import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

# Sprite Groups that hold bullets fired by the player and the enemy
player_bullets = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()

# Tile class used to build the barrier shapes
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

# Tile shape build from the 2D pattern above
class Shape:
  def __init__(self, origin, pattern=pattern, tile_size=3):
    self.tiles = pygame.sprite.Group()
    self.tile_size = tile_size
    self.build(pattern, origin)

  def build(self, pattern, offset):
    ox, oy = offset
    step = self.tile_size

    for r_idx, row in enumerate(pattern):
      for c_idx, cell in enumerate(row):
        if cell:
          pos = (ox + c_idx * step, oy + r_idx * step)
          tile = Tile(pos, size=step)
          self.tiles.add(tile)
          
# Generates four barriers near the bottom of the screen with different positions
barriers = pygame.sprite.Group()
positions = [(20, 500), (243, 500), (466, 500), (689, 500)]

for pos in positions:
    shape = Shape(pos)
    barriers.add(*shape.tiles)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
          
    screen.fill((0, 0, 0))    
    barriers.draw(screen)

    # Bullet barrier collisions handling
    for bullet in player_bullets:
        if pygame.sprite.spritecollide(bullet, barriers, dokill=True):
            bullet.kill()

  def getShotAt(self, alienbullets):
    for barrier in self.barriers:
      if hasattr(barrier, 'tiles'):
        for bullet in alienbullets:
          if pygame.sprite.spritecollide(bullet, barrier.tiles, dokill=True):
              bullet.kill()
              # barrier.tiles.destroy()
    for bullet in enemy_bullets:
        if pygame.sprite.spritecollide(bullet, barriers, dokill=True):
            bullet.kill()
          
    # Movement of bullets and deletion when off-screen 
    for bullet in player_bullets:
        bullet.rect.y -= 5
        if bullet.rect.bottom < 0:
            bullet.kill()

    for bullet in enemy_bullets:
        bullet.rect.y += 5
        if bullet.rect.top > 600:
            bullet.kill()
          
    pygame.display.update()
