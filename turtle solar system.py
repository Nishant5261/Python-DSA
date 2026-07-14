from turtle import *
from math import tan,radians
def start():
    wn=Screen()
    cur=Turtle()
    cur.reset()
def spiral(r,t):
    for i in range(r):
        circle(i,t)
def polygon(s,r=100):
    circle(r,360,s)
def star():
    for i in range(5):
        forward(100)
        right(144)
def draw_spiral(angle, length_start, length_increase, sides):
    for i in range(0,sides):
        forward(length_start+(i*length_increase))
        right(angle)
def draw_petals(length, number):
    for i in range(0, number):
        forward(length)
        right(180-(360/number)) # number divisible by 36
def drawSnowFlake(length, depth):
    if depth > 0:
        for i in range(6):
            forward(length)
            drawSnowFlake(length // 3, depth - 1)
            backward(length)
            left(60)
def tree(branchLen):

 if branchLen > 5:
     forward(branchLen)
     right(20)
     tree(branchLen-15)
     left(40)
     tree(branchLen-15)
     right(20)
     backward(branchLen)
import turtle

# Setting up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Solar System Animation")

# Creating a Turtle object for drawing the sun and planets
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(3)

# Creating a list of planets with their properties (color, distance from the sun, size, and speed)
planets = [
    {"color": "gray", "distance": 50, "size": 0.5, "speed": 1},
    {"color": "orange", "distance": 80, "size": 0.8, "speed": 0.5},
    {"color": "red", "distance": 120, "size": 0.7, "speed": 0.3},
    {"color": "blue", "distance": 160, "size": 0.6, "speed": 0.2},
    {"color": "green", "distance": 200, "size": 0.9, "speed": 0.1}
]

# Creating a Turtle object for each planet and animate their orbits
planet_turtles = []
for planet in planets:
    planet_turtle = turtle.Turtle()
    planet_turtle.shape("circle")
    planet_turtle.color(planet["color"])
    planet_turtle.shapesize(planet["size"])
    planet_turtle.penup()
    planet_turtle.goto(planet["distance"], 0)
    planet_turtle.pendown()
    planet_turtles.append(planet_turtle)

# Function to animate the planets' orbits
def animate_orbits():
    for i, planet in enumerate(planet_turtles):
        planet.speed(0)
        angle = 360 * planets[i]["speed"]
        planet.circle(planets[i]["distance"], angle)

# Animating the orbits
while True:
    animate_orbits()
    wn.update()

# Closing the program when the user clicks on the screen
wn.exitonclick()
import turtle
import datetime
import math

screen = turtle.Screen()
screen.title('Continuous Clock - PythonTurtle.Academy')
screen.bgcolor('sky blue')
screen.setup(500,500)
screen.setworldcoordinates(-100,-100,100,100)
screen.tracer(0,0)


class clock:
    def __init__(self,hour,minute,second):
        self.hour, self.minute, self.second = hour, minute, second
        self.microsecond = 0
        self.face = turtle.Turtle()
        self.hand = turtle.Turtle()
        self.face.hideturtle()
        self.hand.hideturtle()

    def draw(self):
        self.draw_face()
        self.draw_hand()
        
    def draw_face(self):
        self.face.clear()
        self.face.up()
        self.face.goto(0,-70)
        self.face.pensize(4)
        self.face.down()
        self.face.fillcolor('white')
        self.face.begin_fill()
        self.face.circle(70,steps=10)
        self.face.end_fill()
        self.face.up()
        self.face.goto(0,0)
        self.face.dot(10)
        self.face.pensize(2)
        for angle in range(0,360,6):
            self.face.up()
            self.face.goto(0,0)
            self.face.seth(90-angle)
            self.face.fd(62)
            self.face.down()
            self.face.fd(3)
            
        self.face.pensize(3)
        for angle in range(0,360,30):
            self.face.up()
            self.face.goto(0,0)
            self.face.seth(90-angle)
            self.face.fd(60)
            self.face.down()
            self.face.fd(5)
            
        self.face.pensize(4)
        for angle in range(0,360,90):
            self.face.up()
            self.face.goto(0,0)
            self.face.seth(90-angle)
            self.face.fd(58)
            self.face.down()
            self.face.fd(7)
        
    def draw_hand(self):    
        self.hand.clear()       
        self.hand.up()
        self.hand.goto(0,0)
        self.hand.seth(90-math.floor(((self.hour%12)*60*60*1000000+self.minute*60*1000000+self.second*1000000+self.microsecond)/3600000000*30))
        self.hand.down()
        self.hand.color('black')
        self.hand.pensize(6)
        self.hand.fd(30)

        self.hand.up()
        self.hand.goto(0,0)
        self.hand.seth(90-math.floor((self.minute*60*1000000+self.second*1000000+self.microsecond)/60000000*6))
        self.hand.down()
        self.hand.color('black')
        self.hand.pensize(4)
        self.hand.fd(40)

        self.hand.up()
        self.hand.color('red')
        self.hand.goto(0,0)
        self.hand.dot(5)
        self.hand.seth(90-(self.second*1000000+self.microsecond)/1000000*6)
        self.hand.down()
        self.hand.pensize(2)
        self.hand.fd(57)

def animate():
    global c
    d = datetime.datetime.now()
    c.hour, c.minute, c.second, c.microsecond = d.hour, d.minute, d.second, d.microsecond
    c.draw_hand()
    screen.update()
    screen.ontimer(animate,100)
    
d = datetime.datetime.now()
c = clock(d.hour,d.minute,d.second)
c.draw_face()
screen.update()
animate()
import turtle
import math

from collections.abc import Generator
from enum import IntEnum

TILE_RATIO = 0.025          # Ratio of tile size to screen width
CLEAR_COLOR = (0, 125, 255) # Color to clear screen (blue)
UPDATE_FREQUENCY_MS = 16    # How often to call the update function in ms
CHUNK_LENGTH = 64           # World split into chunks, length of one chunk in tiles
GENERATE_WAVELENGTH = 8     # How often a new random point is generated in noise function (every multiple of x)
GENERATE_OCTAVES = 4        # Number of layers of noise we overlay
GENERATE_AMPLITUDE = 8      # Multiplier of noise, determines steepness of terrian
WORLD_SEED = 0              # Seed of noise (same seed -> same world)
TREE_OFFSET = 158573        # Offset noise so tree generation chance at some tile doesn't correspond to world height at that tile

class Tile(IntEnum):
    AIR = 0,
    GRASS = 1,
    DIRT = 2,
    STONE = 3,
    LOG = 4,
    LEAVES = 5

# Offset by 1, since air isn't rendered
TILE_COLORS = [
    (  0, 200,   0), # Grass
    (150, 100,  50), # Dirt
    (100, 100, 100), # Stone
    (200, 150, 100), # Log
    (  0, 255,  50)  # Leaves
]

# Helper functions
def vec2_add(a : tuple, b : tuple):
    return (a[0] + b[0], a[1] + b[1])

def vec2_sub(a : tuple, b : tuple):
    return (a[0] - b[0], a[1] - b[1])

def vec2_mul(v : tuple, s : float):
    return (v[0] * s, v[1] * s)

class World:
    def __init__(self):
        # Stores chunks (lists of tiles)
        self.chunks = []
        # Stores position of that chunk in world
        self.chunk_indices = []

    def update(self, player_position : tuple[int, int]):
        # Calculate chunk player is in
        player_chunk_position = (math.floor(player_position[0] / CHUNK_LENGTH), math.floor(player_position[1] / CHUNK_LENGTH))

        new_chunks = []
        new_chunk_indices = []

        # Generate all chunks in square radius 1 of player
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                required_chunk = vec2_sub(player_chunk_position, (dx, dy))

                for i, chunk in enumerate(self.chunk_indices):
                    if chunk == required_chunk:
                        new_chunks.append(self.chunks[i])
                        new_chunk_indices.append(chunk)

                        break
                else:
                    new_chunks.append(generate_chunk(required_chunk))
                    new_chunk_indices.append(required_chunk)

        self.chunks = new_chunks
        self.chunk_indices = new_chunk_indices

# State
tile_size = None
window_width = None
window_height = None

world = World()
player_position = (0, 0)
camera_position = None
player_direction = (0, 0)

def generate_tree(tiles : list[Tile], base_position : tuple[int, int]):
    """
    Generate a tree at a given position (base position is where the stump of the tree)
    """
    TREE_LOG_HEIGHT = 3
    TREE_LEAVES_HEIGHT = 3
    TREE_LEAVES_WIDTH = 5
    TREE_LEAVES_HALFWIDTH = math.ceil((TREE_LEAVES_WIDTH - 1) / 2)
    TREE_TOTAL_HEIGHT = TREE_LOG_HEIGHT + TREE_LEAVES_HEIGHT

    # Check x within bounds
    if base_position[0] >= TREE_LEAVES_HALFWIDTH - 1 and base_position[0] < CHUNK_LENGTH - TREE_LEAVES_HALFWIDTH:
        if base_position[1] <= CHUNK_LENGTH - TREE_TOTAL_HEIGHT:
            # Build log
            for y_off in range(TREE_LOG_HEIGHT):
                y = base_position[1] + y_off

                tiles[y * CHUNK_LENGTH + base_position[0]] = Tile.LOG

            # Build leaves layers
            for y_off in range(TREE_LEAVES_HEIGHT):
                y = base_position[1] + y_off + TREE_LOG_HEIGHT

                # NOTE: Extra math to make leaves taper off at top level
                for x_off in range(-TREE_LEAVES_HALFWIDTH + (y_off == TREE_LEAVES_HEIGHT - 1), TREE_LEAVES_HALFWIDTH + 1 - (y_off == TREE_LEAVES_HEIGHT - 1)):
                    x = base_position[0] + x_off

                    tiles[y * CHUNK_LENGTH + x] = Tile.LEAVES


def generate_chunk(chunk_index : tuple[int, int]):
    """
    Generate a chunk's tiles at a given index, returning a 1D array of tiles
    """
    # Calculate tile position of bottom left of chunk
    position = vec2_mul(chunk_index, CHUNK_LENGTH)

    tiles = [Tile.AIR] * (CHUNK_LENGTH * CHUNK_LENGTH)

    # For each x slice
    for x in range(CHUNK_LENGTH):
        # Get a noise value, and calculate height we should generate up to
        sampled_noise = noise(position[0] + x, GENERATE_WAVELENGTH, GENERATE_OCTAVES) * GENERATE_AMPLITUDE
        height = math.floor(sampled_noise) - position[1]

        for y in range(CHUNK_LENGTH):
            index = x + y * CHUNK_LENGTH
            selected_tile = None

            # If we're above maximum height, stop generating any higher
            if y > height:
                break
            # If we're at maximum height, generate grass
            elif y == height:
                selected_tile = Tile.GRASS
            # Generate topsoil
            elif height - y <= 3:
                selected_tile = Tile.DIRT
            # Generate stone below maximum height
            else:
                selected_tile = Tile.STONE

            # Set the tile in tiles array
            tiles[index] = selected_tile

        # Add trees randomly
        if noise(position[0] + x + TREE_OFFSET, 1, 1) < 0.1:
            generate_tree(tiles, (x, height + 1))
            
    return tiles

def interp(a : float, b : float, t : float) -> float:
    """
    Linearly interpolate between two points given a speed (t)
    """
    return a * (1 - t) + b * t

def int_hash(x : int) -> float:
    """
    Hash integer to float
    """
    x = x ^ WORLD_SEED
    # https://stackoverflow.com/questions/664014/what-integer-hash-function-are-good-that-accepts-an-integer-hash-key
    x = ((x >> 16) ^ x) * 0x45d9f3b
    x = ((x >> 16) ^ x) * 0x45d9f3b
    x = ((x >> 16) ^ x)
    
    return x % (2 ** 32) / (2 ** 32)

def noise(x : int, wavelength : int, octaves : int) -> Generator[float, None, None]:
    """
    Generate linearly interpolated white noise at some x value
    """
    # Generate two lattice points
    lattice_0 = int_hash(x // wavelength)
    lattice_1 = int_hash(x // wavelength + 1)

    noise_sum = 0
    amplitude_sum = 0
    amplitude = 1

    for _ in range(octaves):
        amplitude_sum += amplitude
        # Linearly interpolate between lattice points, biases towards whichever side we're closer to
        noise_sum += interp(lattice_0, lattice_1, (x % wavelength) / wavelength) * amplitude
        
        amplitude *= 0.5
        wavelength *= 0.5

    return noise_sum / amplitude_sum

def draw_tile(x : float, y : float, tile : Tile) -> None:
    """
    Use turtle to draw tile at some position
    """
    if tile == Tile.AIR: return

    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(TILE_COLORS[tile - 1])
    turtle.pendown()

    turtle.begin_fill()

    # Square
    for _ in range(4):
        turtle.forward(tile_size)
        turtle.left(90)

    turtle.end_fill()

def aabb_check(min1 : tuple[float, float], max1 : tuple[float, float], min2 : tuple[float, float], max2 : tuple[float, float]):
    """
    Check if two AABBs are intersecting
    """
    return not (max1[0] <= min2[0] or max2[0] <= min1[0]) and (max1[1] <= min2[1] or max2[1] <= min1[1])

def update():
    """
    Update screen, game, player
    """
    global tile_size, window_width, window_height, camera_position, player_position, player_direction

    # Clear screen
    turtle.clear()

    # Get window dimensions
    window_width = float(turtle.window_width())
    window_height = float(turtle.window_height())
    half_window = vec2_mul((window_width, window_height), 0.5)

    # Calculate tile size
    tile_size = window_width * TILE_RATIO

    # Player movement
    player_position = vec2_add(player_position, player_direction)
    player_direction = (0, 0)

    # Update camera position
    camera_position = vec2_add(vec2_mul(player_position, tile_size), half_window)

    # Update world around player
    world.update(player_position)

    # For each loaded chunk
    for i, chunk_index in enumerate(world.chunk_indices):
        chunk = world.chunks[i]

        for y in range(CHUNK_LENGTH):
            draw_y = (y + chunk_index[1] * CHUNK_LENGTH) * tile_size - camera_position[1]

            # Bounds check y draw coordinate
            if not (draw_y >= -half_window[1] and draw_y <= half_window[1]):
                continue

            for x in range(CHUNK_LENGTH):
                tile = chunk[y * CHUNK_LENGTH + x]

                draw_x = (x + chunk_index[0] * CHUNK_LENGTH) * tile_size - camera_position[0]

                # Bounds check x draw coordinate
                if draw_x >= -half_window[0] and draw_x <= half_window[0]:
                    draw_tile(draw_x, draw_y, tile)

    turtle.update()
    turtle.ontimer(update, t=UPDATE_FREQUENCY_MS)

def add_direction(direction : tuple[int, int]):
    """
    Update moving direction of player
    """
    global player_direction
    player_direction = vec2_add(player_direction, direction)
    screen.update()

if __name__ == "__main__":
    # Make turtle fast
    turtle.speed(0)
    turtle.tracer(False)
    # Hide turtle sprite
    turtle.hideturtle()
    turtle.colormode(0xff)
    turtle.pencolor(CLEAR_COLOR)
    turtle.bgcolor(CLEAR_COLOR)

    print("Use WASD to navigate")

    screen = turtle.Screen()
    screen.onkeypress(lambda: add_direction((-1,  0)), "a")
    screen.onkeypress(lambda: add_direction(( 1,  0)), "d")
    screen.onkeypress(lambda: add_direction(( 0,  1)), "w")
    screen.onkeypress(lambda: add_direction(( 0, -1)), "s")

    turtle.listen()

    update()

    turtle.mainloop()
import time
from turtle import Screen,Turtle
from random import randint

ALIGNMENT = "center"
FONT = ("Arial",20,"normal")
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("triangle")

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
    
    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
            
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT) 

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0,270)
        self.score = 0
        self.current_score()
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.current_score()

    def current_score(self):
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over",align=ALIGNMENT,font=FONT)
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid = 0.5)
        self.color("red")
        self.speed("fastest")
        random_x = randint(-280,280)
        random_y = randint(-280,270)
        self.goto(random_x, random_y)
        self.refresh_food_location()

    def refresh_food_location(self):
        random_x = randint(-280,280)
        random_y = randint(-280,280)
        self.goto(random_x, random_y)


def Screen_setup():
    screen.setup(width=600, height=600)
    screen.bgcolor("black")

def game():
    Screen_setup()
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    score = Score()

    screen.listen()
    screen.onkey(snake.up,'Up')
    screen.onkey(snake.down,'Down')
    screen.onkey(snake.left,'Left')
    screen.onkey(snake.right,'Right')

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        #Detect the collision with food
        if snake.head.distance(food) < 15:
            food.refresh_food_location()
            score.increase_score()
            snake.extend()
            
        #Detect the collision with wall
        if snake.head.xcor() >280 or snake.head.xcor() <-280 or snake.head.ycor() > 280 or snake.head.ycor() <-280:
            game_is_on = False
            score.game_over()
            
        #Detect the collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment)<10:
                game_is_on = False
                score.game_over()

screen = Screen()
Screen_setup()

while screen.textinput("Snake Game", "Do you want to play Snake Game? y/n:").lower() == "y":
    game()
    time.sleep(2)
    screen.clearscreen()
    Screen_setup()






    
    

