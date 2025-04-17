import pygame as pg
from random import uniform

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, SPLIT_MIN_ANGLE, SPLIT_MAX_ANGLE, SPLIT_ACCELERATION

class Asteroid(CircleShape):
    def __init__(self, x: int, y: int, radius: int, velocity: pg.Vector2):
        super().__init__(x, y, radius)
        self.velocity = velocity
    
    def split(self) -> None:
        self.kill() # Remove self from group
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = uniform(SPLIT_MIN_ANGLE, SPLIT_MAX_ANGLE)
        velocity1 = self.velocity.rotate(angle) * SPLIT_ACCELERATION
        velocity2 = self.velocity.rotate(-angle) * SPLIT_ACCELERATION
        new_r = self.radius - ASTEROID_MIN_RADIUS
        Asteroid(self.position.x, self.position.y, new_r, velocity1)
        Asteroid(self.position.x, self.position.y, new_r, velocity2)
