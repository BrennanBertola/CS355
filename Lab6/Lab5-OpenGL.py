import sys
import numpy as np

try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GL import glOrtho
    from OpenGL.GLU import gluPerspective
    from OpenGL.GL import glRotated
    from OpenGL.GL import glTranslated
    from OpenGL.GL import glLoadIdentity
    from OpenGL.GL import glMatrixMode
    from OpenGL.GL import GL_MODELVIEW
    from OpenGL.GL import GL_PROJECTION
except:
    print("ERROR: PyOpenGL not installed properly. ")

DISPLAY_WIDTH = 500.0
DISPLAY_HEIGHT = 500.0
NCLIP = 1
FCLIP = 100
FOV = 70
ROTATION = 2
ORTHO = 0

CURR_X = 0.0
CURR_Y = 0.0
CURR_Z = 0.0
CURR_DEG = 0




def init(): 
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluPerspective(FOV, DISPLAY_WIDTH / DISPLAY_HEIGHT, NCLIP, FCLIP)

def drawHouse ():
    glLineWidth(2.5)
    glColor3f(1.0, 0.0, 0.0)
    #Floor
    glBegin(GL_LINES)
    glVertex3f(-5.0, 0.0, -5.0)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 0, 5)
    glVertex3f(5, 0, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 0, -5)
    #Ceiling
    glVertex3f(-5, 5, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 5, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(-5, 5, 5)
    glVertex3f(-5, 5, 5)
    glVertex3f(-5, 5, -5)
    #Walls
    glVertex3f(-5, 0, -5)
    glVertex3f(-5, 5, -5)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 0, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 5, 5)
    #Door
    glVertex3f(-1, 0, 5)
    glVertex3f(-1, 3, 5)
    glVertex3f(-1, 3, 5)
    glVertex3f(1, 3, 5)
    glVertex3f(1, 3, 5)
    glVertex3f(1, 0, 5)
    #Roof
    glVertex3f(-5, 5, -5)
    glVertex3f(0, 8, -5)
    glVertex3f(0, 8, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(-5, 5, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(0, 8, -5)
    glEnd()


def drawCar():
    glLineWidth(2.5)


    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)
    # Front Side
    glVertex3f(-3, 2, 2)
    glVertex3f(-2, 3, 2)
    glVertex3f(-2, 3, 2)
    glVertex3f(2, 3, 2)
    glVertex3f(2, 3, 2)
    glVertex3f(3, 2, 2)
    glVertex3f(3, 2, 2)
    glVertex3f(3, 1, 2)
    glVertex3f(3, 1, 2)
    glVertex3f(-3, 1, 2)
    glVertex3f(-3, 1, 2)
    glVertex3f(-3, 2, 2)
    # Back Side
    glVertex3f(-3, 2, -2)
    glVertex3f(-2, 3, -2)
    glVertex3f(-2, 3, -2)
    glVertex3f(2, 3, -2)
    glVertex3f(2, 3, -2)
    glVertex3f(3, 2, -2)
    glVertex3f(3, 2, -2)
    glVertex3f(3, 1, -2)
    glVertex3f(3, 1, -2)
    glVertex3f(-3, 1, -2)
    glVertex3f(-3, 1, -2)
    glVertex3f(-3, 2, -2)
    # Connectors
    glVertex3f(-3, 2, 2)
    glVertex3f(-3, 2, -2)
    glVertex3f(-2, 3, 2)
    glVertex3f(-2, 3, -2)
    glVertex3f(2, 3, 2)
    glVertex3f(2, 3, -2)
    glVertex3f(3, 2, 2)
    glVertex3f(3, 2, -2)
    glVertex3f(3, 1, 2)
    glVertex3f(3, 1, -2)
    glVertex3f(-3, 1, 2)
    glVertex3f(-3, 1, -2)
    glEnd()


def drawTire():
    glLineWidth(2.5)


    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINES)
    # Front Side
    glVertex3f(-1, .5, .5)
    glVertex3f(-.5, 1, .5)
    glVertex3f(-.5, 1, .5)
    glVertex3f(.5, 1, .5)
    glVertex3f(.5, 1, .5)
    glVertex3f(1, .5, .5)
    glVertex3f(1, .5, .5)
    glVertex3f(1, -.5, .5)
    glVertex3f(1, -.5, .5)
    glVertex3f(.5, -1, .5)
    glVertex3f(.5, -1, .5)
    glVertex3f(-.5, -1, .5)
    glVertex3f(-.5, -1, .5)
    glVertex3f(-1, -.5, .5)
    glVertex3f(-1, -.5, .5)
    glVertex3f(-1, .5, .5)
    # Back Side
    glVertex3f(-1, .5, -.5)
    glVertex3f(-.5, 1, -.5)
    glVertex3f(-.5, 1, -.5)
    glVertex3f(.5, 1, -.5)
    glVertex3f(.5, 1, -.5)
    glVertex3f(1, .5, -.5)
    glVertex3f(1, .5, -.5)
    glVertex3f(1, -.5, -.5)
    glVertex3f(1, -.5, -.5)
    glVertex3f(.5, -1, -.5)
    glVertex3f(.5, -1, -.5)
    glVertex3f(-.5, -1, -.5)
    glVertex3f(-.5, -1, -.5)
    glVertex3f(-1, -.5, -.5)
    glVertex3f(-1, -.5, -.5)
    glVertex3f(-1, .5, -.5)
    # Connectors
    glVertex3f(-1, .5, .5)
    glVertex3f(-1, .5, -.5)
    glVertex3f(-.5, 1, .5)
    glVertex3f(-.5, 1, -.5)
    glVertex3f(.5, 1, .5)
    glVertex3f(.5, 1, -.5)
    glVertex3f(1, .5, .5)
    glVertex3f(1, .5, -.5)
    glVertex3f(1, -.5, .5)
    glVertex3f(1, -.5, -.5)
    glVertex3f(.5, -1, .5)
    glVertex3f(.5, -1, -.5)
    glVertex3f(-.5, -1, .5)
    glVertex3f(-.5, -1, -.5)
    glVertex3f(-1, -.5, .5)
    glVertex3f(-1, -.5, -.5)
    glEnd()

def display():
    glClear (GL_COLOR_BUFFER_BIT)
    glColor3f (1.0, 1.0, 1.0)
    # viewing transformation 


    #House 1
    glPushMatrix()
    glTranslate(0,0,-30)
    drawHouse()
    glPopMatrix()

    #House 2
    glPushMatrix()
    glTranslate(15,0,-30)
    drawHouse()
    glPopMatrix()

    #House 3
    glPushMatrix()
    glTranslate(-15,0,-30)
    drawHouse()
    glPopMatrix()

    #House 4
    glPushMatrix()
    glTranslate(-30,0,-15)
    glRotate(90,0,1,0)
    drawHouse()
    glPopMatrix()

    #House 5
    glPushMatrix()
    glTranslate(-30,0, 0)
    glRotate(90,0,1,0)
    drawHouse()
    glPopMatrix()

    #House 6
    glPushMatrix()
    glTranslate(-30,0, 15)
    glRotate(90,0,1,0)
    drawHouse()
    glPopMatrix()

    #House 7
    glPushMatrix()
    glTranslate(0,0,30)
    glRotate(180,0,1,0)
    drawHouse()
    glPopMatrix()

    #House 8
    glPushMatrix()
    glTranslate(15,0,30)
    glRotate(180,0,1,0)
    drawHouse()
    glPopMatrix()

    #House 9
    glPushMatrix()
    glTranslate(-15,0,30)
    glRotate(180,0,1,0)
    drawHouse()
    glPopMatrix()

    
    glFlush()
    

def movement(x, z):
    rad = CURR_DEG * (np.pi/180)
    xMove = x*np.cos(rad) + z*-np.sin(rad)
    zMove = x*np.sin(rad) + z*np.cos(rad)
    return xMove, zMove

def keyboard(key, x, y):
    global CURR_X
    global CURR_Y
    global CURR_Z
    global CURR_DEG
    global ORTHO
    
    if key == chr(27):
        import sys
        sys.exit(0)

    # basic testing not movement not based off of camera direction

    if key == b'w':
        print("W, move forward")
        x, z = movement(0,1)
        CURR_Z += z
        CURR_X += x
        glTranslate(x,0,z)
    elif key == b'a':
        print("A, move left")
        x, z = movement(1, 0)
        CURR_X += x
        CURR_Z += z
        glTranslate(x, 0, z)
    elif key == b's':
        print("S, move back")
        x, z = movement(0, -1)
        CURR_Z += z
        CURR_X += x
        glTranslate(x, 0, z)
    elif key == b'd':
        print("D, move right")
        x, z = movement(-1, 0)
        CURR_Z += z
        CURR_X += x
        glTranslate(x, 0, z)
    elif key == b'q':
        print("Q, turn left")
        CURR_DEG -= ROTATION

        glTranslate(-CURR_X, -CURR_Y, -CURR_Z)
        glRotate(-ROTATION,0,1,0)
        glTranslate(CURR_X, CURR_Y, CURR_Z)

    elif key == b'e':
        print("E, turn right")
        CURR_DEG += ROTATION

        glTranslate(-CURR_X, -CURR_Y, -CURR_Z)
        glRotate(ROTATION,0,1,0)
        glTranslate(CURR_X, CURR_Y, CURR_Z)

    elif key == b'r':
        print("R, move up")
        CURR_Y -= 1
        glTranslate(0, -1, 0)
    elif key == b'f':
        print("F, move down")
        CURR_Y += 1
        glTranslate(0, 1, 0)
    elif key == b'h':
        print("H, return home")

        glLoadIdentity()
        if(ORTHO):
            glOrtho(-10,10,-10,10, NCLIP, FCLIP)
        else:
            gluPerspective(FOV, DISPLAY_WIDTH / DISPLAY_HEIGHT, NCLIP, FCLIP)
        glTranslate(0, 0, 0)

        CURR_X = 0
        CURR_Y = 0
        CURR_Z = 0
        CURR_DEG = 0

    elif key == b'o':
        print("O, orthographic projection")
        ORTHO = 1

        glLoadIdentity()
        glOrtho(-10,10,-10,10, NCLIP, FCLIP)
        glRotate(CURR_DEG, 0, 1, 0)
        glTranslate(CURR_X, CURR_Y, CURR_Z)
    elif key == b'p':
        print("P, perspective projection")
        ORTHO = 0
        glLoadIdentity()
        gluPerspective(FOV, DISPLAY_WIDTH / DISPLAY_HEIGHT, NCLIP, FCLIP)
        glRotate(CURR_DEG, 0, 1, 0)
        glTranslate(CURR_X, CURR_Y, CURR_Z)
  
    #Your Code Here
  
    glutPostRedisplay()


glutInit(sys.argv)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize (int(DISPLAY_WIDTH), int(DISPLAY_HEIGHT))
glutInitWindowPosition (100, 100)
glutCreateWindow (b'OpenGL Lab')
init ()
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutMainLoop()
