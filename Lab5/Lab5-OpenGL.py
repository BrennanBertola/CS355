import sys

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

CURR_X = 0
CURR_Y = -4
CURR_Z = -15
CURR_DEG = 0

def init(): 
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)

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

def display():
    glClear (GL_COLOR_BUFFER_BIT)
    glColor3f (1.0, 1.0, 1.0)
    # viewing transformation 

    
    #Your Code Here

    glLoadIdentity()
    gluPerspective(90, DISPLAY_WIDTH / DISPLAY_HEIGHT, 0, 1)
    glRotated(CURR_DEG, 0, 1, 0)
    glTranslated(CURR_X, CURR_Y, CURR_Z)

    drawHouse()

    
    glFlush()
    

def keyboard(key, x, y):
    global CURR_X
    global CURR_Y
    global CURR_Z
    global CURR_DEG
    
    if key == chr(27):
        import sys
        sys.exit(0)

    # basic testing not movement not based off of camera direction

    if key == b'w':
        print("W, move forward")
        CURR_Z += 1
    elif key == b'a':
        print("A, move left")
        CURR_X += 1
    elif key == b's':
        print("S, move back")
        CURR_Z -= 1
    elif key == b'd':
        print("D, move right")
        CURR_X -= 1
    elif key == b'q':
        print("Q, turn left")
        CURR_DEG -= 1
    elif key == b'e':
        print("E, turn right")
        CURR_DEG += 1
    elif key == b'r':
        print("R, move up")
        CURR_Y -= 1
    elif key == b'f':
        print("F, move down")
        CURR_Y += 1
    elif key == b'h':
        print("H, return home")
        CURR_X = 0
        CURR_Y = -4
        CURR_Z = -15
        CURR_DEG = 0
    elif key == b'o':
        print("O, orthographic projection")
    elif key == b'p':
        print("P, perspective projection")
  
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
