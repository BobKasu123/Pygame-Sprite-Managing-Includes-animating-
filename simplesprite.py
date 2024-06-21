import pygame

class SimpleSprite:
  def __init__(self, x, y, animation_images, width, height, screen):
    self.screen = screen
    self.image_index = 0
    self.image_cooldown = 0
    self.flip = False
    self.x = x
    self.y = y
    self.animation_images = [pygame.transform.scale(pygame.image.load(img), (width, height)) for img in animation_images]
    self.image = self.animation_images[self.image_index]

  # display the sprite in the screen
  def display(self):
    self.screen.blit(pygame.transform.flip(self.image, self.flip, False), (self.x, self.y))

  # move the sprite
  def move(self, x, y):
    self.x += x
    self.y += y

    if x < 0:
      self.flip = True
    else:
      self.flip = False

  # animating using the animation_images list
  def animate(self):
    self.image_cooldown += 20
    if self.image_cooldown > 100:
      self.image_index += 1
      self.image_cooldown = 0
    if self.image_index > len(self.animation_images)-1:
      self.image_index = 0

    self.image = self.animation_images[self.image_index]
