from constants import LINE_WIDTH, PLAYER_RADIUS, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius) 

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        new_rotation = random.uniform(20, 50)
        spawn_1 = self.velocity.rotate(new_rotation)
        spawn_2 = self.velocity.rotate(-new_rotation)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid_spawn_1 = Asteroid(self.position.x, self.position.y, new_radius)
        Asteroid_spawn_2 = Asteroid(self.position.x, self.position.y, new_radius)

        Asteroid_spawn_1.velocity = spawn_1 * 1.2
        Asteroid_spawn_2.velocity = spawn_2 * 1.2