import pygame as pg
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting Asteroids!")
    print(f"Screen size: {SCREEN_HEIGHT} x {SCREEN_WIDTH}")

    # Pygame initialize, boilerplate
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pg.time.Clock()
    dt = 0

    # I don't recall this pygame feature....
    # These are unorder lists of sprites. Interesting.
    # While this abstraction does reduce the amount of code, it also produces hidden control flow
    # It's not fully hidden since the initializer does use "self.container" in its Sprite super initializer, 
    #   but this is not visible from the outside for the reader to follow
    # I believe that this represents the... listener/observer pattern?
    updatable = pg.sprite.Group() # Vectorized operation
    drawables = pg.sprite.Group()  
    asteroids = pg.sprite.Group() 
    shots = pg.sprite.Group() 

    Player.containers = (updatable, drawables)
    Asteroid.containers = (asteroids, updatable, drawables)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawables)

    # While not explicitly used, 'asteroid_field' implicitly manages the asteroids as an updatable object
    asteroid_field = AsteroidField()

    # Put player in center of window
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:

        # Get all input, handle it in player.update()
        for _ in pg.event.get(): pass
        
        # Logic and Player input for upcoming frame
        updatable.update(dt) 

        # Check for collisions
        for asteroid in asteroids:
            if asteroid.is_collision(player):
                print("Game over!")
                # TODO: Wait for confirmation, ask for rematch?
                sys.exit()
            for bullet in shots:
                if bullet.is_collision(asteroid):
                    # TODO: Points to player?
                    asteroid.split()
                    bullet.kill()
        
        # View
        pg.Surface.fill(screen, "black")
        for drawable in drawables:
            drawable.draw(screen)
        pg.display.flip()

        # Seconds since last frame
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()