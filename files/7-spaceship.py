# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0.5


class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):
        #canvas.draw_circle(self.pos, self.radius, 1, "White", "White")
        if self.thrust:
            canvas.draw_image(ship_image, [self.image_center[0] + 90, self.image_center[1]], self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(ship_image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
            
        
    def update(self):
        #position update
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        self.angle += self.angle_vel
        forward = angle_to_vector(self.angle)
        
        #friction update
        self.vel[0] *= (1 - 0.02)
        self.vel[1] *= (1 - 0.02)
        
        if self.thrust:
            #self.vel = angle_to_vector(self.angle)
            self.vel[0] += forward[0] * 0.1
            self.vel[1] += forward[1] * 0.1
            ship_thrust_sound.play()
        else:
            #self.vel[0] -= self.vel[0]
            #self.vel[1] -= self.vel[1]
            ship_thrust_sound.rewind()
            
    
    def shoot(self):
        global a_missile
        missile = angle_to_vector(self.angle)
        missile_pos = [missile[0] * self.radius, missile[1] * self.radius]
        canon_pos = [missile_pos[0] + self.pos[0], missile_pos[1] + self.pos[1]]
        missile_vel = [0, 0]
        missile_vel[0] += self.vel[0] + (missile[0] * 3)
        missile_vel[1] += self.vel[1] + (missile[1] * 3)
        missile_angle = self.angle
        missile_angle_vel = self.angle_vel
        
        a_missile = Sprite(canon_pos , [missile_vel[0], missile_vel[1]], missile_angle, missile_angle_vel, missile_image, missile_info , missile_sound)

    # keys for ship
    
    def keydown_thrust(self):
        self.thrust = True
        #self.vel[0] += 0.9 
        #self.vel[1] += 0.9 
        
    def keyup_thrust(self):
        self.thrust = False
        #self.vel[0] -= 0.9
        #self.vel[1] -= 0.9      
    
    def keydown_left(self):
        self.angle_vel -= 0.05
        
    def keydown_right(self):    
        self.angle_vel += 0.05
            
    def keyup_left(self):
        self.angle_vel += 0.05
        
    def keyup_right(self):    
        self.angle_vel -= 0.05
        
       
    
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        #canvas.draw_circle(self.pos, self.radius, 1, "Red", "Red")
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
        
    def update(self):
        self.angle += self.angle_vel
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        

# Key Handlers for ship
def keydown_handler(key):
    if simplegui.KEY_MAP["up"] == key:
        my_ship.keydown_thrust()
        
    if simplegui.KEY_MAP["space"] == key:
        my_ship.shoot()
    
    elif simplegui.KEY_MAP["left"] == key:
        my_ship.keydown_left()
    elif simplegui.KEY_MAP["right"] == key:
        my_ship.keydown_right()

        
def keyup_handler(key):
    if simplegui.KEY_MAP["up"] == key:
        my_ship.keyup_thrust()
    
    if simplegui.KEY_MAP["left"] == key:
        my_ship.keyup_left()
    elif simplegui.KEY_MAP["right"] == key:
        my_ship.keyup_right()

                  
def draw(canvas):
    global time, lives, score
    
    # animiate background
    time += 1
    center = debris_info.get_center()
    size = debris_info.get_size()
    wtime = (time / 8) % center[0]
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, [center[0] - wtime, center[1]], [size[0] - 2 * wtime, size[1]], 
                                [WIDTH / 2 + 1.25 * wtime, HEIGHT / 2], [WIDTH - 2.5 * wtime, HEIGHT])
    canvas.draw_image(debris_image, [size[0] - wtime, center[1]], [2 * wtime, size[1]], 
                                [1.25 * wtime, HEIGHT / 2], [2.5 * wtime, HEIGHT])
    # Lives and Score
    vidas = "Lives = " + str(lives)
    puntos = "Score = " + str(score)
    canvas.draw_text(vidas, [50, 50], 30, "White")
    canvas.draw_text(puntos, [630, 50], 30, "White")
    
    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    a_missile.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    a_rock.update()
    a_missile.update()
            
# timer handler that spawns a rock    
def rock_spawner():
    global a_rock
    random_pos = [random.randrange(1, WIDTH - 1), random.randrange(1, HEIGHT - 1)]
    random_vel = [random.random() * 1.1, random.random() * 1.1]
    random_ang = random.random() * 0.09
    random_fac = random.choice([1, -1])
 
    a_rock = Sprite(random_pos, [random_vel[0] * random_fac, random_vel[1] * random_fac], 0, random_ang * random_fac, asteroid_image, asteroid_info)

  
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [0, 0], 0, 0.02, asteroid_image, asteroid_info)
#a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, asteroid_image, asteroid_info, missile_sound)
a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown_handler)
frame.set_keyup_handler(keyup_handler)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
