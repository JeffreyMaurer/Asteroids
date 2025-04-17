import pygame as pg
import random as r
from asteroid import Asteroid
from constants import *

# Needs to inherit from Sprite to get container attribute behavior
class AsteroidField(pg.sprite.Sprite):

    edges = {
        "right": {
            "edge": DIR_RIGHT,
            "starting_point": lambda y: pg.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        },
        "left" : {
            "edge": DIR_LEFT,
            "starting_point": lambda y: pg.Vector2(SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        },
        "up" : {
            "edge" : DIR_UP,
            "starting_point": lambda x: pg.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        },
        "down" : {
            "edge" : DIR_DOWN,
            "starting_point" : lambda x: pg.Vector2(x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS),
        }
    }

    def __init__(self):
        pg.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0

    def update(self, dt) -> None:
        self.spawn_timer += dt
        if self.spawn_timer <= ASTEROID_SPAWN_RATE:
            return
        
        # Spawn a new asteroid at a random edge
        edge = r.choice(list(AsteroidField.edges.keys()))
        cardinal_speed = AsteroidField.edges[edge]["edge"] * r.randint(40, 100)
        velocity = cardinal_speed.rotate(r.randint(-30, 30)) # Magic?
        position = AsteroidField.edges[edge]["starting_point"](r.uniform(0, 1))
        kind = r.randint(1, ASTEROID_KINDS)
        Asteroid(position.x, position.y, ASTEROID_MIN_RADIUS * kind, velocity)
        self.spawn_timer = 0 # Cooldown
