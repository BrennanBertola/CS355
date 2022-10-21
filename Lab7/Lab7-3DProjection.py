# Import a library of functions called 'pygame'
import copy

import pygame
import numpy as np
from math import pi

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Point3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

class Line3D():

    def __init__(self, start, end):
        self.start = start
        self.end = end

def loadOBJ(filename):

    vertices = []
    indices = []
    lines = []

    f = open(filename, "r")
    for line in f:
        t = str.split(line)
        if not t:
            continue
        if t[0] == "v":
            vertices.append(Point3D(float(t[1]),float(t[2]),float(t[3])))

        if t[0] == "f":
            for i in range(1,len(t) - 1):
                index1 = int(str.split(t[i],"/")[0])
                index2 = int(str.split(t[i+1],"/")[0])
                indices.append((index1,index2))

    f.close()

    #Add faces as lines
    for index_pair in indices:
        index1 = index_pair[0]
        index2 = index_pair[1]
        lines.append(Line3D(vertices[index1 - 1],vertices[index2 - 1]))

    #Find duplicates
    duplicates = []
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            line1 = lines[i]
            line2 = lines[j]

            # Case 1 -> Starts match
            if line1.start.x == line2.start.x and line1.start.y == line2.start.y and line1.start.z == line2.start.z:
                if line1.end.x == line2.end.x and line1.end.y == line2.end.y and line1.end.z == line2.end.z:
                    duplicates.append(j)
            # Case 2 -> Start matches end
            if line1.start.x == line2.end.x and line1.start.y == line2.end.y and line1.start.z == line2.end.z:
                if line1.end.x == line2.start.x and line1.end.y == line2.start.y and line1.end.z == line2.start.z:
                    duplicates.append(j)

    duplicates = list(set(duplicates))
    duplicates.sort()
    duplicates = duplicates[::-1]

    #Remove duplicates
    for j in range(len(duplicates)):
        del lines[duplicates[j]]

    return lines

def loadHouse():
    house = []
    #Floor
    house.append(Line3D(Point3D(-5, 0, -5), Point3D(5, 0, -5)))
    house.append(Line3D(Point3D(5, 0, -5), Point3D(5, 0, 5)))
    house.append(Line3D(Point3D(5, 0, 5), Point3D(-5, 0, 5)))
    house.append(Line3D(Point3D(-5, 0, 5), Point3D(-5, 0, -5)))
    #Ceiling
    house.append(Line3D(Point3D(-5, 5, -5), Point3D(5, 5, -5)))
    house.append(Line3D(Point3D(5, 5, -5), Point3D(5, 5, 5)))
    house.append(Line3D(Point3D(5, 5, 5), Point3D(-5, 5, 5)))
    house.append(Line3D(Point3D(-5, 5, 5), Point3D(-5, 5, -5)))
    #Walls
    house.append(Line3D(Point3D(-5, 0, -5), Point3D(-5, 5, -5)))
    house.append(Line3D(Point3D(5, 0, -5), Point3D(5, 5, -5)))
    house.append(Line3D(Point3D(5, 0, 5), Point3D(5, 5, 5)))
    house.append(Line3D(Point3D(-5, 0, 5), Point3D(-5, 5, 5)))
    #Door
    house.append(Line3D(Point3D(-1, 0, 5), Point3D(-1, 3, 5)))
    house.append(Line3D(Point3D(-1, 3, 5), Point3D(1, 3, 5)))
    house.append(Line3D(Point3D(1, 3, 5), Point3D(1, 0, 5)))
    #Roof
    house.append(Line3D(Point3D(-5, 5, -5), Point3D(0, 8, -5)))
    house.append(Line3D(Point3D(0, 8, -5), Point3D(5, 5, -5)))
    house.append(Line3D(Point3D(-5, 5, 5), Point3D(0, 8, 5)))
    house.append(Line3D(Point3D(0, 8, 5), Point3D(5, 5, 5)))
    house.append(Line3D(Point3D(0, 8, 5), Point3D(0, 8, -5)))

    return house

def loadCar():
    car = []
    #Front Side
    car.append(Line3D(Point3D(-3, 2, 2), Point3D(-2, 3, 2)))
    car.append(Line3D(Point3D(-2, 3, 2), Point3D(2, 3, 2)))
    car.append(Line3D(Point3D(2, 3, 2), Point3D(3, 2, 2)))
    car.append(Line3D(Point3D(3, 2, 2), Point3D(3, 1, 2)))
    car.append(Line3D(Point3D(3, 1, 2), Point3D(-3, 1, 2)))
    car.append(Line3D(Point3D(-3, 1, 2), Point3D(-3, 2, 2)))

    #Back Side
    car.append(Line3D(Point3D(-3, 2, -2), Point3D(-2, 3, -2)))
    car.append(Line3D(Point3D(-2, 3, -2), Point3D(2, 3, -2)))
    car.append(Line3D(Point3D(2, 3, -2), Point3D(3, 2, -2)))
    car.append(Line3D(Point3D(3, 2, -2), Point3D(3, 1, -2)))
    car.append(Line3D(Point3D(3, 1, -2), Point3D(-3, 1, -2)))
    car.append(Line3D(Point3D(-3, 1, -2), Point3D(-3, 2, -2)))
    
    #Connectors
    car.append(Line3D(Point3D(-3, 2, 2), Point3D(-3, 2, -2)))
    car.append(Line3D(Point3D(-2, 3, 2), Point3D(-2, 3, -2)))
    car.append(Line3D(Point3D(2, 3, 2), Point3D(2, 3, -2)))
    car.append(Line3D(Point3D(3, 2, 2), Point3D(3, 2, -2)))
    car.append(Line3D(Point3D(3, 1, 2), Point3D(3, 1, -2)))
    car.append(Line3D(Point3D(-3, 1, 2), Point3D(-3, 1, -2)))

    return car

def loadTire():
    tire = []
    #Front Side
    tire.append(Line3D(Point3D(-1, .5, .5), Point3D(-.5, 1, .5)))
    tire.append(Line3D(Point3D(-.5, 1, .5), Point3D(.5, 1, .5)))
    tire.append(Line3D(Point3D(.5, 1, .5), Point3D(1, .5, .5)))
    tire.append(Line3D(Point3D(1, .5, .5), Point3D(1, -.5, .5)))
    tire.append(Line3D(Point3D(1, -.5, .5), Point3D(.5, -1, .5)))
    tire.append(Line3D(Point3D(.5, -1, .5), Point3D(-.5, -1, .5)))
    tire.append(Line3D(Point3D(-.5, -1, .5), Point3D(-1, -.5, .5)))
    tire.append(Line3D(Point3D(-1, -.5, .5), Point3D(-1, .5, .5)))

    #Back Side
    tire.append(Line3D(Point3D(-1, .5, -.5), Point3D(-.5, 1, -.5)))
    tire.append(Line3D(Point3D(-.5, 1, -.5), Point3D(.5, 1, -.5)))
    tire.append(Line3D(Point3D(.5, 1, -.5), Point3D(1, .5, -.5)))
    tire.append(Line3D(Point3D(1, .5, -.5), Point3D(1, -.5, -.5)))
    tire.append(Line3D(Point3D(1, -.5, -.5), Point3D(.5, -1, -.5)))
    tire.append(Line3D(Point3D(.5, -1, -.5), Point3D(-.5, -1, -.5)))
    tire.append(Line3D(Point3D(-.5, -1, -.5), Point3D(-1, -.5, -.5)))
    tire.append(Line3D(Point3D(-1, -.5, -.5), Point3D(-1, .5, -.5)))

    #Connectors
    tire.append(Line3D(Point3D(-1, .5, .5), Point3D(-1, .5, -.5)))
    tire.append(Line3D(Point3D(-.5, 1, .5), Point3D(-.5, 1, -.5)))
    tire.append(Line3D(Point3D(.5, 1, .5), Point3D(.5, 1, -.5)))
    tire.append(Line3D(Point3D(1, .5, .5), Point3D(1, .5, -.5)))
    tire.append(Line3D(Point3D(1, -.5, .5), Point3D(1, -.5, -.5)))
    tire.append(Line3D(Point3D(.5, -1, .5), Point3D(.5, -1, -.5)))
    tire.append(Line3D(Point3D(-.5, -1, .5), Point3D(-.5, -1, -.5)))
    tire.append(Line3D(Point3D(-1, -.5, .5), Point3D(-1, -.5, -.5)))
    
    return tire




# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

# Set the height and width of the screen
size = [512, 512]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Shape Drawing")
 
#Set needed variables
done = False
clock = pygame.time.Clock()
start = Point(0.0,0.0)
end = Point(0.0,0.0)
houseLines = loadHouse()
carLines = loadCar()
tireLines = loadTire()

NCLIP = 1
FCLIP = 500
FOV = 70
FOV_RAD = FOV * (np.pi/180)
ROTATION = 1
MOVE = .3

CURR_X = 0.0
CURR_Y = 0.0
CURR_Z = 0.0
CURR_DEG = 0

CAR_X = -15
CAR_Y = 0
CAR_Z = 15

TIRE_X = 2
TIRE_Y = -.25
TIRE_Z = 1.5

ZOOM = 1/np.tan(FOV_RAD/2)
TRANSITION_MAT = np.array([[1.0, 0.0, 0.0, 0.0],
                    [0.0, 1.0, 0.0, 0.0],
                    [0.0, 0.0, 1.0, 0.0],
                    [0.0, 0.0, 0.0, 1.0]])
ROTATION_MAT = np.array([[1.0, 0.0, 0.0, 0.0],
                    [0.0, 1.0, 0.0, 0.0],
                    [0.0, 0.0, 1.0, 0.0],
                    [0.0, 0.0, 0.0, 1.0]])
CAM_MAT = ROTATION_MAT@TRANSITION_MAT
CLIP_MAT = np.array([[ZOOM,0,0,0],
                     [0,ZOOM,0,0],
                     [0,0,(FCLIP + NCLIP)/(FCLIP - NCLIP), (-2*NCLIP*FCLIP)/(FCLIP-NCLIP)],
                     [0,0,1,0]])
VIEW_MAT = np.array([[512/2,0,512/2],
                     [0,-512/2, 512/2],
                     [0,0,1]])

T_LIST = []
R_LIST = []
def movement(x, z):
    rad = CURR_DEG * (np.pi/180)
    xMove = x*np.cos(rad) + z*-np.sin(rad)
    zMove = x*np.sin(rad) + z*np.cos(rad)
    return xMove, zMove

def translate(x,y,z):
    global CAM_MAT
    TRANSITION_MAT[0, 3] = TRANSITION_MAT[0, 3] + x
    TRANSITION_MAT[1, 3] = TRANSITION_MAT[1, 3] + y
    TRANSITION_MAT[2, 3] = TRANSITION_MAT[2, 3] + z

def rotate(deg):
    rad = (CURR_DEG+deg) * (np.pi/180)
    ROTATION_MAT[0,0] = np.cos(rad)
    ROTATION_MAT[0,2] = np.sin(rad)
    ROTATION_MAT[2,0] = -np.sin(rad)
    ROTATION_MAT[2,2] = np.cos(rad)

def rotateObj(deg, lines):
    rad = deg * (np.pi / 180)
    newLines = copy.deepcopy(lines)
    for s in newLines:
        sX = np.cos(rad)*s.start.x + np.sin(rad)*s.start.z
        eX = np.cos(rad)*s.end.x + np.sin(rad)*s.end.z
        sZ = -np.sin(rad)*s.start.x + np.cos(rad)*s.start.z
        eZ = -np.sin(rad)*s.end.x + np.cos(rad)*s.end.z

        s.start.x = sX
        s.start.z = sZ
        s.end.x = eX
        s.end.z = eZ
    return newLines

def push():
    T_LIST.append(np.copy(TRANSITION_MAT))
    R_LIST.append(np.copy(ROTATION_MAT))

def pop():
    global TRANSITION_MAT
    global ROTATION_MAT
    TRANSITION_MAT = np.copy(T_LIST[-1])
    T_LIST.pop(-1)
    ROTATION_MAT = np.copy(R_LIST[-1])
    R_LIST.pop(-1)

def drawLines(lines, color):
    global CAM_MAT

    for s in lines:
        #convert ot homogenouse
        end = np.array([s.end.x, s.end.y, s.end.z, 1])
        start = np.array([s.start.x, s.start.y, s.start.z, 1])

        #convert to cam coordinates
        CAM_MAT = ROTATION_MAT @ TRANSITION_MAT
        end = CAM_MAT @ end
        start = CAM_MAT @ start

        #apply clip matrix
        end = CLIP_MAT@end
        start = CLIP_MAT@start

        #Cliping Tests
        accept = True

        start = start/start[3]
        end = end/end[3]

        if (start[0] < -start[3] and end[0] < -end[3]):
            accept = False
        elif(start[0] > start[3] and end[0] > end[3]):
            accept = False
        elif(start[1] < -start[3] and end[1] < -end[3]):
            accept = False
        elif(start[1] > start[3] and end[1] > end[3]):
            accept = False
        elif(start[2] < -start[3] or end[2] < -end[3]):
            accept = False
        elif(start[2] > start[3] or end[2] > end[3]):
            accept = False

        if(not accept):
            continue
        #to canonical space
        end = np.array([end[0]/end[3], end[1]/end[3], 1])
        start = np.array([start[0]/start[3], start[1]/start[3], 1])

        #to screen space
        end = VIEW_MAT@end
        start = VIEW_MAT@start

        pygame.draw.line(screen, color, (start[0],start[1]), (end[0],end[1]))


#Loop until the user clicks the close button.
while not done:
 
    # This limits the while loop to a max of 100 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(100)

    # Clear the screen and set the screen background
    screen.fill(BLACK)

    #Controller Code#
    #####################################################################

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If user clicked close
            done=True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        print("w is pressed")
        x,z = movement(0, -MOVE)
        CURR_Z += z
        CURR_X += x
        translate(x, 0, z)
    elif pressed[pygame.K_a]:
        print("a is pressed")
        x, z = movement(MOVE, 0)
        CURR_X += x
        CURR_Z += z
        translate(x, 0, z)
    elif pressed[pygame.K_s]:
        print("s is pressed")
        x, z = movement(0, MOVE)
        CURR_Z += z
        CURR_X += x
        translate(x, 0, z)
    elif pressed[pygame.K_d]:
        print("d is pressed")
        x, z = movement(-MOVE, 0)
        CURR_Z += z
        CURR_X += x
        translate(x, 0, z)
    elif pressed[pygame.K_q]:
        print("q is pressed")
        CURR_DEG += ROTATION

        translate(-CURR_X, -CURR_Y, -CURR_Z)
        rotate(ROTATION)
        translate(CURR_X, CURR_Y, CURR_Z)
    elif pressed[pygame.K_e]:
        print("e is pressed")
        CURR_DEG -= ROTATION

        translate(-CURR_X, -CURR_Y, -CURR_Z)
        rotate(ROTATION)
        translate(CURR_X, CURR_Y, CURR_Z)
    elif pressed[pygame.K_r]:
        print("r is pressed")
        CURR_Y -= 1
        translate(0, -MOVE, 0)
    elif pressed[pygame.K_f]:
        print("f is pressed")
        CURR_Y += 1
        translate(0, MOVE, 0)
    elif pressed[pygame.K_h]:
        print("h is pressed")
        CURR_X = 0
        CURR_Y = 0
        CURR_Z = 0
        CURR_DEG = 0
        CAR_X = -15
        CAR_Y = 0
        CAR_Z = 15

        TRANSITION_MAT = np.array([[1.0, 0.0, 0.0, 0.0],
                                   [0.0, 1.0, 0.0, 0.0],
                                   [0.0, 0.0, 1.0, 0.0],
                                   [0.0, 0.0, 0.0, 1.0]])
        ROTATION_MAT = np.array([[1.0, 0.0, 0.0, 0.0],
                                 [0.0, 1.0, 0.0, 0.0],
                                 [0.0, 0.0, 1.0, 0.0],
                                 [0.0, 0.0, 0.0, 1.0]])

    #Viewer Code#
    #####################################################################
    push()
    translate(0,0,-30)
    drawLines(houseLines, RED)
    pop()

    push()
    translate(15,0,-30)
    drawLines(houseLines, RED)
    pop()

    push()
    translate(-15,0,-30)
    drawLines(houseLines, RED)
    pop()

    push()
    translate(-30,0,15)
    newLines = rotateObj(90, houseLines)
    drawLines(newLines, RED)
    pop()

    push()
    translate(-30,0,0)
    newLines = rotateObj(90, houseLines)
    drawLines(newLines, RED)
    pop()

    push()
    translate(-30,0,-15)
    newLines = rotateObj(90, houseLines)
    drawLines(newLines, RED)
    pop()

    push()
    translate(0,0,30)
    newLines = rotateObj(180, houseLines)
    drawLines(newLines, RED)
    pop()

    push()
    translate(15,0,30)
    newLines = rotateObj(180, houseLines)
    drawLines(newLines, RED)
    pop()

    push()
    translate(-15,0,30)
    newLines = rotateObj(180, houseLines)
    drawLines(newLines, RED)
    pop()

    push()
    translate(CAR_X, CAR_Y, CAR_Z)
    drawLines(carLines, BLUE)

    push()
    translate(TIRE_X, TIRE_Y, TIRE_Z)
    drawLines(tireLines, GREEN)
    pop()

    push()
    translate(-TIRE_X, TIRE_Y, TIRE_Z)
    drawLines(tireLines, GREEN)
    pop()

    push()
    translate(TIRE_X, TIRE_Y, -TIRE_Z)
    drawLines(tireLines, GREEN)
    pop()

    push()
    translate(-TIRE_X, TIRE_Y, -TIRE_Z)
    drawLines(tireLines, GREEN)
    pop()
    pop()


    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()