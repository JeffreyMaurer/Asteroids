import pygame as pg

# Pixels
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# These cardinal directions might be easier to use if named explicitly
DIR_UP = pg.Vector2(0,1)
DIR_DOWN = pg.Vector2(0,-1)
DIR_RIGHT = pg.Vector2(1,0)
DIR_LEFT = pg.Vector2(-1,0)

# All objects are polygons, so their line width needs to be defined
STROKE_WIDTH = 2 # mm?

ASTEROID_MIN_RADIUS = 20 # Pixels
ASTEROID_KINDS = 3 # Big, Medium, Small
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS # Pixels
SPLIT_ACCELERATION = 1.2 # Constant

SHOT_RADIUS = 5 # Pixels
PLAYER_SHOOT_SPEED = 500 # Pixels/s?
PLAYER_SHOOT_COOLDOWN = 0.3 # Seconds
SPLIT_MIN_ANGLE = 20 # Degrees
SPLIT_MAX_ANGLE = 50 # Degrees

PLAYER_RADIUS = 20 # Pixels
PLAYER_TURN_SPEED = 300 # Degrees/s
PLAYER_SPEED = 200 # Pixels