import pygame

class Sprite:
  def __init__(self, up_anim: list, down_anim: list, right_anim: list, left_anim: list, x: int, y: int, width: int, height: int, screen, animation_images = []):
    self.screen = screen
    self.x = x
    self.y = y
    self.image_index = 0
    self.image_cooldown = 0
    
    self.up_anim = [pygame.transform.scale(pygame.image.load(img), (width, height)) for img in up_anim]
    self.down_anim = [pygame.transform.scale(pygame.image.load(img), (width, height)) for img in down_anim]
    self.right_anim = [pygame.transform.scale(pygame.image.load(img), (width, height)) for img in right_anim]
    self.left_anim = [pygame.transform.scale(pygame.image.load(img), (width, height)) for img in left_anim]
    
    self.animation_images = self.down_anim if down_anim is not None else animation_images
    self.image = self.animation_images[self.image_index]
    self.rect = pygame.Rect((self.x, self.y, width-75, height-75))

  # display the sprite onto the screen
  def display(self):
    self.screen.blit(self.image, (self.x, self.y))

  # move the sprite
  def move(self, x, y):
    self.x += x
    self.y += y

    if x > 0:
      self.animation_images = self.right_anim
    elif x < 0:
      self.animation_images = self.left_anim
    elif y < 0:
      self.animation_images = self.up_anim
    elif y > 0:
      self.animation_images = self.down_anim
      
def animate(self):
  self.image_cooldown += 20
    if self.image_cooldown > 100:
      self.image_index += 1
      self.image_cooldown = 0
    if self.image_index > len(self.animation_images)-1:
      self.image_index = 0
      
    self.image = self.animation_images[self.image_index]

  
    
    
