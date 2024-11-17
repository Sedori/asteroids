import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            self.kill()
            random_angle = random.uniform(20, 50)
            new_vel1 = self.velocity.rotate(random_angle)
            new_vel2 = self.velocity.rotate(-random_angle)
            new_asteroid1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            new_asteroid1.velocity = new_vel1 * 1.2
            new_asteroid2.velocity = new_vel2 * 1.2
            for group in self.groups():
                group.add(new_asteroid1)
                group.add(new_asteroid2)

