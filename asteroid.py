from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # self.position and self.velocity are inherited from Circleshap
    
    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius)

    
    def update(self, dt):
        self.position += (self.velocity * dt)

    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        random_angle = random.uniform(20, 50)
        one = self.velocity.rotate(random_angle)
        two = self.velocity.rotate(-random_angle)
        smaller_radius = self.radius - ASTEROID_MIN_RADIUS
        ast1 = Asteroid(self.position.x, self.position.y, smaller_radius)
        ast2 = Asteroid(self.position.x, self.position.y, smaller_radius)
        ast1.velocity = one * 1.2
        ast2.velocity = two * 1.2
    