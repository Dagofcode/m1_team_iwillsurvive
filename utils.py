import math, pygame, sys

class vector2:
   # note, no data member declarations needed

   # constructor
   def __init__(self, x, y):
      # unlike C/Java, no implicit "this" pointer
      # instead, reference is passed in as first argument (self in this case)
      self.x = x
      self.y = y

   # method definitions
   def add(self, other):
      v = vector2(self.x + other.x, self.y + other.y)
      return v

   def scale(self, scalar):
      v = vector2(self.x * scalar, self.y * scalar)
      return v

   # overload return-this-as-string for printing
   def __str__(self):
      # format allows you to replace "{}" with variable values
      return "({}, {})".format(self.x, self.y)

   def subtract(self, other):
      v = vector2(self.x - other.x, self.y - other.y)
      return v

   def magnitude(self):
      p = math.sqrt(self.x * self.x + self.y * self.y)
      return p

   def normalizer(self, magnitude):
      v = vector2(self.x / magnitude, self.y / magnitude)
      return v


class sprite:

    #constructor
    def __init__(self,fname, pos, v):

        self.x = pos.x
        self.y = pos.y

        self.vx = v.x
        self.vy = v.y
        self.radi = 50
        self.img = pygame.image.load(fname).convert()


    def update(self, delta, screen):
        self.vx = self.vx + self.ax * delta
        self.vy = self.vy + self.ay * delta
        self.x = self.x + self.vx * delta
        self.y = self.y + self.vy * delta

        #get screen size
        x,y = screen.get_size()


        #bottom wall
        if self.y + 50 + self.radi >= y:
           self.vy = - self.vy
           self.ay = 0
           
        #top wall
        elif self.y <= 0:
           self.vy = - self.vy
           self.ay = 0

        #right wall
        if self.x + 50 + self.radi >= x:
           self.vx = - self.vx
           self.ax = 0
           
        #left wall
        elif self.x  <= 0:
           self.vx = - self.vx
           self.ax = 0
       
        #checking for other balls
    
    def collide(self, other):
       dist = self.position.sub(other.position)
       overlap = self.radi + other.radi - dist.magnitude()

       if overlap > 0:
          cn = dist.normalized()
          self.position = self.position.add(cn.scale(overlap/ -2) )
          other.position = other.position.add(cn.scale(overlap/ 2) )

    def dot(self, other):
       return self.x * other.x + self.y * other.y
          
    def draw(self, screen):
        color = (255,255,1)
        circle = pygame.draw.circle(screen, color, (50+int(self.x),50+int(self.y)), self.radi, 50)
        #screen.blit(self.img, (self.x, self.y))
