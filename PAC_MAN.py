import pygame, random, math, time
from pygame.locals import *
from spritesheet_functions import SpriteSheet

class Player(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)

        self.walking_frames_l = []
        self.walking_frames_r = []
        self.walking_frames_u = []
        self.walking_frames_d = []

        sprite_sheet = SpriteSheet('pacman.png')

        self.walking_frames_r.append(sprite_sheet.get_image(456,1,13,13))
        self.walking_frames_r.append(sprite_sheet.get_image(472,1,13,13))


        for image in self.walking_frames_r:
            pygame.transform.scale(image, (1000,1000))
            self.walking_frames_l.append(pygame.transform.flip(image, True, False))
            self.walking_frames_u.append(pygame.transform.rotate(image, 90))
            self.walking_frames_d.append(pygame.transform.rotate(image, -90))

            
                                         
            
        self.x_pos = x_pos
        self.y_pos = y_pos
        
        self.image = self.walking_frames_r[0]

        self.frame = 0

        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

        self.change_x = 0
        self.change_y = 0

        self.speed = 1

        self.direction = 'right'

        self.animation_timer = 0

        self.walls = None
        self.dots = None

    def update(self, screen):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        self.animation_timer += 1

        if self.rect.left <= 0:
            self.rect.right = screen.get_width() -10 
        elif self.rect.right >= screen.get_width():
            self.rect.left = 10

        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)

        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right
            self.change_x = 0

        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, self.walls,False)

        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
                
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
            self.change_y = 0

        block_hit_list2 = pygame.sprite.spritecollide(self, self.dots, True)

        for block in block_hit_list2:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        block_hit_list2 = pygame.sprite.spritecollide(self, self.dots,True)

        for block in block_hit_list2:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

        if self.direction == 'right' and self.animation_timer % 3 == 0:
            if self.change_x == 0:
                self.frame = 0
            else:
                self.frame = (self.frame + 1) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[self.frame]
            
        if self.direction == 'left' and self.animation_timer % 3 == 0:
            if self.change_x == 0:
                self.frame = 0
            else:
                self.frame = (self.frame + 1) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[self.frame]
            
        if self.direction == 'up' and self.animation_timer % 3 == 0:
            if self.change_y == 0:
                self.frame = 0
            else:
                self.frame = (self.frame + 1) % len(self.walking_frames_u)
            self.image = self.walking_frames_u[self.frame]

        if self.direction == 'down' and self.animation_timer % 3 == 0:
            if self.change_y == 0:
                self.frame = 0
            else:
                self.frame = (self.frame + 1) % len(self.walking_frames_d)
            self.image = self.walking_frames_d[self.frame]


                
class Blinky(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)

        self.walking_frames_u = []
        self.walking_frames_d = []
        self.walking_frames_l = []
        self.walking_frames_r = []

        sprite_sheet = SpriteSheet('pacman.png')

        self.walking_frames_r.append(sprite_sheet.get_image(457,64,16,17))
        self.walking_frames_r.append(sprite_sheet.get_image(472,64,16,17))

        for image in self.walking_frames_r:
            self.walking_frames_l.append(pygame.transform.flip(image, True, False))

        self.walking_frames_u.append(sprite_sheet.get_image(520,64,16,16))
        self.walking_frames_u.append(sprite_sheet.get_image(536,65,16,16))

        self.walking_frames_d.append(sprite_sheet.get_image(552,64,16,17))
        self.walking_frames_d.append(sprite_sheet.get_image(568,63,16,17))

        self.animation_timer = 0
        
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.image = pygame.Surface([20,20])
        self.image.fill(Color('pink'))

        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

        self.change_x = 0
        self.change_y = -1

        self.direction = 'right'
        self.speed = 1
        
        self.walls = None
        self.dots = None


        self.choose_direction = False

    
    def update(self, screen):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        self.animation_timer += 1
        if self.direction == 'right' and self.animation_timer % 3 == 0:
            if self.change_x == 0:
                self.frame = 0
            else:
                self.frame = (self.frame + 1) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[self.frame]
            
        if self.direction == 'left' and self.animation_timer % 3 == 0:
            if self.change_x == 0:
                self.frame = 0
            else:
                self.frame = (self.frame + 1) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[self.frame]
            
        if self.direction == 'up' and self.animation_timer % 3 == 0:
            if self.change_y == 0:
                self.frame = 0
            else:
                self.frame = (self.frame + 1) % len(self.walking_frames_u)
            self.image = self.walking_frames_u[self.frame]

        if self.direction == 'down' and self.animation_timer % 3 == 0:
            if self.change_y == 0:
                self.frame = 0
            else:
                self.frame = (self.frame + 1) % len(self.walking_frames_d)
            self.image = self.walking_frames_d[self.frame]

        if self.rect.left <= 0:
            self.rect.right = screen.get_width() -10 
        elif self.rect.right >= screen.get_width():
            self.rect.left = 10
            
            

        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)

        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right
            self.change_x = 0

        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, self.walls,False)

        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
                
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
                
            self.change_y = 0
            
        self.directions = ['right','left','up','down',]

        if self.rect.x % 20 == 0 and self.rect.y % 20 == 0:
            intersection_list = pygame.sprite.spritecollide(self, self.ints, False)
            if intersection_list:

                self.rect.y += 10 # move down
                block_hit_list1 = pygame.sprite.spritecollide(self, self.walls, False)
                self.rect.y -= 10 # move right

                self.rect.y -= 10
                block_hit_list2 = pygame.sprite.spritecollide(self, self.walls, False)
                self.rect.y += 10
                
                self.rect.x += 10
                block_hit_list3 = pygame.sprite.spritecollide(self, self.walls, False)
                self.rect.x -= 10

                self.rect.x -= 10
                block_hit_list4 = pygame.sprite.spritecollide(self, self.walls, False)
                self.rect.x += 10
                if self.change_x > 0:
                    self.directions.remove('left')
                if self.change_x < 0:
                    self.directions.remove('right')
                if self.change_y > 0:
                    self.directions.remove('up')
                if self.change_y < 0:
                    self.directions.remove('down')
                if block_hit_list1:
                    self.directions.remove('down')
                if block_hit_list2:
                    self.directions.remove('up')
                if block_hit_list3:
                    self.directions.remove('right')
                if block_hit_list4:
                    self.directions.remove('left')
                #print self.directions
                while self.choose_direction == False:
                    self.choose_direction = True
                    self.direction = random.choice(self.directions)
                    #print self.direction
                if self.direction == 'right':
                    self.change_x = self.speed
                    self.change_y = 0
                    
                elif self.direction == 'left':
                    self.change_x = -self.speed
                    self.change_y = 0
                    
                elif self.direction == 'up':
                    self.change_y = -self.speed
                    self.change_x = 0
                    
                elif self.direction == 'down':
                    self.change_y = self.speed
                    self.change_x = 0
                    
                self.choose_direction = False

class Pinky(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)

        self.walking_frames_u = []
        self.walking_frames_d = []
        self.walking_frames_l = []
        self.walking_frames_r = []

        sprite_sheet = SpriteSheet('pacman.png')

        self.walking_frames_r.append(sprite_sheet.get_image(456,80,16,17))
        self.walking_frames_r.append(sprite_sheet.get_image(472,80,16,17))

        for image in self.walking_frames_r:
            self.walking_frames_l.append(pygame.transform.flip(image, True, False))

        self.walking_frames_u.append(sprite_sheet.get_image(520,80,16,16))
        self.walking_frames_u.append(sprite_sheet.get_image(536,80,16,16))

        self.walking_frames_d.append(sprite_sheet.get_image(552,80,16,17))
        self.walking_frames_d.append(sprite_sheet.get_image(568,80,16,17))

        self.animation_timer = 0
        
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.image = pygame.Surface([20,20])
        self.image.fill(Color('pink'))

        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

        self.change_x = 0
        self.change_y = -1

        self.direction = 'right'
        self.speed = 1
        
        self.walls = None
        self.dots = None


        self.choose_direction = False

    
    def update(self, screen):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        self.animation_timer += 1
        if self.direction == 'right' and self.animation_timer % 3 == 0:
            if self.change_x == 0:
                self.frame = 0
            else:
                self.frame = (self.frame + 1) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[self.frame]
            
        if self.direction == 'left' and self.animation_timer % 3 == 0:
            if self.change_x == 0:
                self.frame = 0
            else:
                self.frame = (self.frame + 1) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[self.frame]
            
        if self.direction == 'up' and self.animation_timer % 3 == 0:
            if self.change_y == 0:
                self.frame = 0
            else:
                self.frame = (self.frame + 1) % len(self.walking_frames_u)
            self.image = self.walking_frames_u[self.frame]

        if self.direction == 'down' and self.animation_timer % 3 == 0:
            if self.change_y == 0:
                self.frame = 0
            else:
                self.frame = (self.frame + 1) % len(self.walking_frames_d)
            self.image = self.walking_frames_d[self.frame]

        if self.rect.left <= 0:
            self.rect.right = screen.get_width() -10 
        elif self.rect.right >= screen.get_width():
            self.rect.left = 10
            
            

        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)

        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right
            self.change_x = 0

        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, self.walls,False)

        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
                
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
                
            self.change_y = 0
            
        self.directions = ['right','left','up','down',]

        if self.rect.x % 20 == 0 and self.rect.y % 20 == 0:
            intersection_list = pygame.sprite.spritecollide(self, self.ints, False)
            if intersection_list:

                self.rect.y += 10 # move down
                block_hit_list1 = pygame.sprite.spritecollide(self, self.walls, False)
                self.rect.y -= 10 # move right

                self.rect.y -= 10
                block_hit_list2 = pygame.sprite.spritecollide(self, self.walls, False)
                self.rect.y += 10
                
                self.rect.x += 10
                block_hit_list3 = pygame.sprite.spritecollide(self, self.walls, False)
                self.rect.x -= 10

                self.rect.x -= 10
                block_hit_list4 = pygame.sprite.spritecollide(self, self.walls, False)
                self.rect.x += 10
                if self.change_x > 0:
                    self.directions.remove('left')
                if self.change_x < 0:
                    self.directions.remove('right')
                if self.change_y > 0:
                    self.directions.remove('up')
                if self.change_y < 0:
                    self.directions.remove('down')
                if block_hit_list1:
                    self.directions.remove('down')
                if block_hit_list2:
                    self.directions.remove('up')
                if block_hit_list3:
                    self.directions.remove('right')
                if block_hit_list4:
                    self.directions.remove('left')
                #print self.directions
                while self.choose_direction == False:
                    self.choose_direction = True
                    self.direction = random.choice(self.directions)
                    #print self.direction
                if self.direction == 'right':
                    self.change_x = self.speed
                    self.change_y = 0
                    
                elif self.direction == 'left':
                    self.change_x = -self.speed
                    self.change_y = 0
                    
                elif self.direction == 'up':
                    self.change_y = -self.speed
                    self.change_x = 0
                    
                elif self.direction == 'down':
                    self.change_y = self.speed
                    self.change_x = 0
                    
                self.choose_direction = False

class Inky(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)

        self.walking_frames_u = []
        self.walking_frames_d = []
        self.walking_frames_l = []
        self.walking_frames_r = []

        sprite_sheet = SpriteSheet('pacman.png')

        self.walking_frames_r.append(sprite_sheet.get_image(457,96,16,17))
        self.walking_frames_r.append(sprite_sheet.get_image(472,96,16,17))

        for image in self.walking_frames_r:
            self.walking_frames_l.append(pygame.transform.flip(image, True, False))

        self.walking_frames_u.append(sprite_sheet.get_image(520,96,16,16))
        self.walking_frames_u.append(sprite_sheet.get_image(536,96,16,16))

        self.walking_frames_d.append(sprite_sheet.get_image(552,96,16,17))
        self.walking_frames_d.append(sprite_sheet.get_image(568,96,16,17))

        self.animation_timer = 0
        
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.image = pygame.Surface([20,20])
        self.image.fill(Color('pink'))

        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

        self.change_x = 0
        self.change_y = -1

        self.direction = 'right'
        self.speed = 1
        
        self.walls = None
        self.dots = None


        self.choose_direction = False

    
    def update(self, screen):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        self.animation_timer += 1
        if self.direction == 'right' and self.animation_timer % 3 == 0:
            if self.change_x == 0:
                self.frame = 0
            else:
                self.frame = (self.frame + 1) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[self.frame]
            
        if self.direction == 'left' and self.animation_timer % 3 == 0:
            if self.change_x == 0:
                self.frame = 0
            else:
                self.frame = (self.frame + 1) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[self.frame]
            
        if self.direction == 'up' and self.animation_timer % 3 == 0:
            if self.change_y == 0:
                self.frame = 0
            else:
                self.frame = (self.frame + 1) % len(self.walking_frames_u)
            self.image = self.walking_frames_u[self.frame]

        if self.direction == 'down' and self.animation_timer % 3 == 0:
            if self.change_y == 0:
                self.frame = 0
            else:
                self.frame = (self.frame + 1) % len(self.walking_frames_d)
            self.image = self.walking_frames_d[self.frame]

        if self.rect.left <= 0:
            self.rect.right = screen.get_width() -10 
        elif self.rect.right >= screen.get_width():
            self.rect.left = 10
            
            

        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)

        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right
            self.change_x = 0

        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, self.walls,False)

        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
                
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
                
            self.change_y = 0
            
        self.directions = ['right','left','up','down',]

        if self.rect.x % 20 == 0 and self.rect.y % 20 == 0:
            intersection_list = pygame.sprite.spritecollide(self, self.ints, False)
            if intersection_list:

                self.rect.y += 10 # move down
                block_hit_list1 = pygame.sprite.spritecollide(self, self.walls, False)
                self.rect.y -= 10 # move right

                self.rect.y -= 10
                block_hit_list2 = pygame.sprite.spritecollide(self, self.walls, False)
                self.rect.y += 10
                
                self.rect.x += 10
                block_hit_list3 = pygame.sprite.spritecollide(self, self.walls, False)
                self.rect.x -= 10

                self.rect.x -= 10
                block_hit_list4 = pygame.sprite.spritecollide(self, self.walls, False)
                self.rect.x += 10
                if self.change_x > 0:
                    self.directions.remove('left')
                if self.change_x < 0:
                    self.directions.remove('right')
                if self.change_y > 0:
                    self.directions.remove('up')
                if self.change_y < 0:
                    self.directions.remove('down')
                if block_hit_list1:
                    self.directions.remove('down')
                if block_hit_list2:
                    self.directions.remove('up')
                if block_hit_list3:
                    self.directions.remove('right')
                if block_hit_list4:
                    self.directions.remove('left')
                #print self.directions
                while self.choose_direction == False:
                    self.choose_direction = True
                    self.direction = random.choice(self.directions)
                    #print self.direction
                if self.direction == 'right':
                    self.change_x = self.speed
                    self.change_y = 0
                    
                elif self.direction == 'left':
                    self.change_x = -self.speed
                    self.change_y = 0
                    
                elif self.direction == 'up':
                    self.change_y = -self.speed
                    self.change_x = 0
                    
                elif self.direction == 'down':
                    self.change_y = self.speed
                    self.change_x = 0
                    
                self.choose_direction = False

class Clyde(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)

        self.walking_frames_u = []
        self.walking_frames_d = []
        self.walking_frames_l = []
        self.walking_frames_r = []

        sprite_sheet = SpriteSheet('pacman.png')

        self.walking_frames_r.append(sprite_sheet.get_image(457,113,16,17))
        self.walking_frames_r.append(sprite_sheet.get_image(472,113,16,17))

        for image in self.walking_frames_r:
            self.walking_frames_l.append(pygame.transform.flip(image, True, False))

        self.walking_frames_u.append(sprite_sheet.get_image(520,113,16,16))
        self.walking_frames_u.append(sprite_sheet.get_image(536,113,16,16))

        self.walking_frames_d.append(sprite_sheet.get_image(552,113,16,17))
        self.walking_frames_d.append(sprite_sheet.get_image(568,113,16,17))

        self.animation_timer = 0
        
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.image = pygame.Surface([20,20])
        self.image.fill(Color('pink'))

        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

        self.change_x = 0
        self.change_y = -1

        self.direction = 'right'
        self.speed = 1
        
        self.walls = None
        self.dots = None


        self.choose_direction = False

    
    def update(self, screen):
        self.rect.x += self.change_x
        self.rect.y += self.change_y

        self.animation_timer += 1
        if self.direction == 'right' and self.animation_timer % 3 == 0:
            if self.change_x == 0:
                self.frame = 0
            else:
                self.frame = (self.frame + 1) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[self.frame]
            
        if self.direction == 'left' and self.animation_timer % 3 == 0:
            if self.change_x == 0:
                self.frame = 0
            else:
                self.frame = (self.frame + 1) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[self.frame]
            
        if self.direction == 'up' and self.animation_timer % 3 == 0:
            if self.change_y == 0:
                self.frame = 0
            else:
                self.frame = (self.frame + 1) % len(self.walking_frames_u)
            self.image = self.walking_frames_u[self.frame]

        if self.direction == 'down' and self.animation_timer % 3 == 0:
            if self.change_y == 0:
                self.frame = 0
            else:
                self.frame = (self.frame + 1) % len(self.walking_frames_d)
            self.image = self.walking_frames_d[self.frame]

        if self.rect.left <= 0:
            self.rect.right = screen.get_width() -10 
        elif self.rect.right >= screen.get_width():
            self.rect.left = 10
            
            

        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)

        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                self.rect.left = block.rect.right
            self.change_x = 0

        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, self.walls,False)

        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
                
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom
                
            self.change_y = 0
            
        self.directions = ['right','left','up','down',]

        if self.rect.x % 20 == 0 and self.rect.y % 20 == 0:
            intersection_list = pygame.sprite.spritecollide(self, self.ints, False)
            if intersection_list:

                self.rect.y += 10 # move down
                block_hit_list1 = pygame.sprite.spritecollide(self, self.walls, False)
                self.rect.y -= 10 # move right

                self.rect.y -= 10
                block_hit_list2 = pygame.sprite.spritecollide(self, self.walls, False)
                self.rect.y += 10
                
                self.rect.x += 10
                block_hit_list3 = pygame.sprite.spritecollide(self, self.walls, False)
                self.rect.x -= 10

                self.rect.x -= 10
                block_hit_list4 = pygame.sprite.spritecollide(self, self.walls, False)
                self.rect.x += 10
                if self.change_x > 0:
                    self.directions.remove('left')
                if self.change_x < 0:
                    self.directions.remove('right')
                if self.change_y > 0:
                    self.directions.remove('up')
                if self.change_y < 0:
                    self.directions.remove('down')
                if block_hit_list1:
                    self.directions.remove('down')
                if block_hit_list2:
                    self.directions.remove('up')
                if block_hit_list3:
                    self.directions.remove('right')
                if block_hit_list4:
                    self.directions.remove('left')
                #print self.directions
                while self.choose_direction == False:
                    self.choose_direction = True
                    self.direction = random.choice(self.directions)
                    #print self.direction
                if self.direction == 'right':
                    self.change_x = self.speed
                    self.change_y = 0
                    
                elif self.direction == 'left':
                    self.change_x = -self.speed
                    self.change_y = 0
                    
                elif self.direction == 'up':
                    self.change_y = -self.speed
                    self.change_x = 0
                    
                elif self.direction == 'down':
                    self.change_y = self.speed
                    self.change_x = 0
                    
                self.choose_direction = False
          
class Grid:
    def __init__(self, rows, columns):

        # Create an empty list of lists.
        self.grid = []
        for i in range(rows):
            row = []
            for j in range(columns):
                row.append('x')
            self.grid.append(row)
        self.grid = ['wwwwwwwwwwwwwwwwwwwwwwwwwwwww',
                     'wi....i.....iwwi.....i....iw',
                     'w.wwww.wwwww.ww.wwwww.wwww.w',
                     'w.wwww.wwwww.ww.wwwww.wwww.w',
                     'wi....i..i..i..i..i..i....iw',
                     'w.wwww.ww.wwwwwwww.ww.wwww.w',
                     'w.wwww.ww.wwwwwwww.ww.wwww.w',
                     'wi....iwwi..iwwi..iwwi....iw',
                     'wwwwww.wwwww.ww.wwwww.wwwwwww',
                     '     w.wwwww.ww.wwwww.w     ',
                     '     w.wwi  i ti  iww.w     ',
                     '     w.ww www  www ww.w     ',
                     'wwwwww.ww w      w ww.wwwwww',
                     '      i  iw      wi  i      ',
                     'wwwwww.ww w      w ww.wwwwww',
                     '     w.ww wwwwwwww ww.w     ',
                     '     w.wwi        iww.w     ',
                     '     w.ww wwwwwwww ww.w     ',
                     'wwwwww.ww wwwwwwww ww.wwwwww',
                     'wi....i..i..iwwi..i..i....iw',
                     'w.wwww.wwwww.ww.wwwww.wwww.w',
                     'w.wwww.wwwww.ww.wwwww.wwww.w',
                     'wi.iwwi..i..i..i..i..iwwi.iw',
                     'www.ww.ww.wwwwwwww.ww.ww.www',
                     'www.ww.ww.wwwwwwww.ww.ww.www',
                     'wi.i..iwwi..iwwi..iwwi..i.iw',
                     'w.wwwwwwwwww.ww.wwwwwwwwww.w',
                     'w.wwwwwwwwww.ww.wwwwwwwwww.w',
                     'wi..........i..i..........iw',
                     'wwwwwwwwwwwwwwwwwwwwwwwwwwww']
                     

        
        self.grid_group = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.dots = pygame.sprite.Group()
        self.ints = pygame.sprite.Group()
        start_x = 0
        start_y = 0
        for row in self.grid:
            for cell in row:
                if cell == 'w':
                    new_wall = Wall(start_x, start_y)
                    self.grid_group.add(new_wall)
                    self.walls.add(new_wall)
                    start_x += 20
                    
                if cell =='.':
                    new_dot = Dot(start_x, start_y)
                    self.grid_group.add(new_dot)
                    self.dots.add(new_dot)
                    start_x += 20
                    
                if cell ==' ':
                    self.grid_group.add(Space(start_x, start_y))
                    start_x += 20
                if cell =='i':
                    new_int = Intersection(start_x, start_y)
                    new_dot = Dot(start_x, start_y)
                    self.grid_group.add(new_int)
                    self.grid_group.add(new_dot)
                    self.dots.add(new_dot)
                    self.ints.add(new_int)
                    start_x += 20

                if cell =='t':
                    temp_int = Temp_Intersection(start_x, start_y, self)
                    self.grid_group.add(temp_int)
                    self.ints.add(temp_int)
                    start_x += 20
                
            start_x = 0
            start_y += 20

        
        print self

    def __str__(self):
        print_grid = ''
        for row in self.grid:
            for cell in row:
                print_grid += cell + ' '
            print_grid += '\n'
        return print_grid


class Wall(pygame.sprite.Sprite):

    def __init__(self,x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,20]) 
        self.image.fill(Color('blue')) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.filled = False
        
class Dot(pygame.sprite.Sprite):
    def __init__(self,x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill(Color('yellow'))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.filled = False
class Intersection(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,20])
        self.image.fill(Color('black'))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.filled = False
class Temp_Intersection(pygame.sprite.Sprite):
    def __init__(self,x,y,grid):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,20])
        self.image.fill(Color('red'))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.filled = False
        self.timer = time.time()
        self.grid = grid
    def update(self): #create a timer
        if time.time() - self.timer > 10:
            self.kill()
        
        
        
        

        

class Space(pygame.sprite.Sprite):
    def __init__(self,x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20,20]) #[20,15]
        self.image.fill(Color('black'))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.filled = False
    
        
        

class GameMain():
    done = False
    color_bg = Color('black')
    game_start = False

    def __init__(self, width= 565 ,height= 600):
        pygame.init()

        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        self.player = Player(30,self.height/2-40)
        self.enemy = Blinky(280,270)#(self.height/2, self.width/2)
        self.enemy2 = Pinky(280,270)
        self.enemy3 = Inky(280,270)
        self.enemy4 = Clyde(280,270)
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.player)
        self.sprites.add(self.enemy)
        self.sprites.add(self.enemy2)
        self.sprites.add(self.enemy3)
        self.sprites.add(self.enemy4)


        self.my_grid = Grid(20, 10)
        self.player.walls = self.my_grid.walls
        self.player.dots = self.my_grid.dots
        self.player.ints = self.my_grid.ints

        self.enemy.walls = self.my_grid.walls
        self.enemy.ints = self.my_grid.ints
        self.enemy2.walls = self.my_grid.walls
        self.enemy2.ints = self.my_grid.ints
        self.enemy3.walls = self.my_grid.walls
        self.enemy3.ints = self.my_grid.ints
        self.enemy4.walls = self.my_grid.walls
        self.enemy4.ints = self.my_grid.ints

        self.chomp_sound = pygame.mixer.Sound('pacman_chomp.wav')
        self.title_sound = pygame.mixer.Sound('pacman_beginning')


        self.mousex = 0
        self.mousey = 0
##
##        self.font = pygame.font.Font('freesansbold.ttf',32)
##        self.text_obj = self.font.render('score:', True, Color('white'))
##        self.text.rect = self.text_obj.get_rect()
##        self.text_rect.center = (self.centerx, self.centery-self.radius + 30)

        self.current_screen = 'title'

        
    def draw_title(self):
        self.screen.fill(Color('black'))
        title_screen = pygame.image.load('start_screen.png')
        self.screen.blit(title_screen, (0,0))
        pygame.display.flip()


    def handle_title(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == KEYDOWN:
                if event.key == K_a:
                    self.title_sound.play()
                    self.current_screen = 'game'
                    print 'a'
                    print self.current_screen
                    self.game_start = True
                    print self.game_start
                    
                    
        
    
    def main_loop(self):
        while not self.done:
            if self.current_screen == 'game':
                self.handle_events()
                self.player.update(self.screen)
                self.enemy.update(self.screen)
                self.enemy2.update(self.screen)
                self.enemy3.update(self.screen)
                self.enemy4.update(self.screen)
                self.my_grid.grid_group.update()
                self.draw()
                self.clock.tick(60)
            elif self.current_screen == 'title':
                
                self.draw_title()
                self.handle_title()
                
                
                
        pygame.quit()

           

    def draw(self):
        
        self.screen.fill(self.color_bg)
        self.my_grid.grid_group.draw(self.screen)
        self.sprites.draw(self.screen)
        pygame.display.flip()

    def handle_events(self):
        SPEED = 1
        events = pygame.event.get()
        self.sprites.draw(self.screen)
        # keystates
        keys = pygame.key.get_pressed()

        # events
        for event in events:
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.done = True
                elif event.key == K_a:
                    self.player.change_x = -SPEED
                    self.player.change_y = 0
                    self.player.direction = 'left'
                elif event.key == K_d:
                    self.player.change_x = SPEED
                    self.player.change_y = 0
                    self.player.direction = 'right'
                elif event.key == K_w:
                    self.player.change_y = -SPEED * .5
                    self.player.change_x = 0
                    self.player.direction = 'up'
                elif event.key == K_s:
                    self.player.change_y = SPEED 
                    self.player.change_x = 0
                    self.player.direction = 'down'
            elif event.type == MOUSEMOTION:
                self.mousex, self.mousey = event.pos
                print self.mousex, self.mousey
                   
                

if __name__ == "__main__":
    game = GameMain()
    game.main_loop()
