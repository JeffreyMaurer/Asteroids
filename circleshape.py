import pygame as pg
from constants import STROKE_WIDTH

# Base class for game objects
class CircleShape(pg.sprite.Sprite):
    def __init__(self, x: int, y: int, radius: int):

        # Place reference of itself into container to be managed
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pg.Vector2(x, y)
        self.velocity = pg.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen) -> None:
        pg.draw.circle(screen, "white", self.position, self.radius, STROKE_WIDTH)

    # Default frame action is Newton's 1st law
    def update(self, dt) -> None:
        self.position += self.velocity * dt

    # Radial distance from centers
    def is_collision(self, other) -> bool:
        distance = self.position.distance_to(other.position)
        total_r = self.radius + other.radius
        return distance <= total_r