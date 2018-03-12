import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

#-----------------------------------------
# Global Variables
#-----------------------------------------
g_Width          = 600
g_Height         = 600 

g_fViewDistance  = 9.
g_nearPlane      = 1.
g_farPlane       = 1000.
zoom             = 60.

xTrans           = 0.
yTrans           = 0.

xRotate          = 0.
yRotate          = 0.
zRotate          = 0.

xStart           = 0.
yStart           = 0.

action           = ""


#-----------------------------------------
# Initial State of Graphics pipeline
#-----------------------------------------
def StateInit():
    glEnable(GL_NORMALIZE)
    glLightfv(GL_LIGHT0,GL_POSITION,[ .0, 10.0, 10., 0. ] )
    glLightfv(GL_LIGHT0,GL_AMBIENT,[ 1.0, .0, .0, 1.0 ])
    glLightfv(GL_LIGHT0,GL_DIFFUSE,[ 1.0, 1.0, 1.0, 1.0 ])
    glLightfv(GL_LIGHT0,GL_SPECULAR,[ 1.0, 1.0, 1.0, 1.0 ])
    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)
    glShadeModel(GL_SMOOTH)
    
#-----------------------------------------
# Draw Object
#-----------------------------------------
def scenemodel():
    glRotate(90,0.,0.,1.)
    glutSolidTeapot(1.)
    
#-----------------------------------------
# Reshape
#-----------------------------------------
def reshape(width,height):
    global g_Width, g_Height
    g_Width  = width
    g_Height = height
    glViewport(0, 0, g_Width, g_Height)

#-----------------------------------------
# polarView   
#-----------------------------------------
def polarView():
    glTranslatef(yTrans/100., 0.0, 0.0 )
    glTranslatef(0.0, -xTrans/100., 0.0 )
    glRotatef( -zRotate, 0.0, 0.0, 1.0)
    glRotatef( -xRotate, 1.0, 0.0, 0.0)
    glRotatef( -yRotate, .0, 1.0, 0.0)
#-----------------------------------------
# mouse 
#-----------------------------------------
def mouse(button,state,x,y):
    global action,xStart,yStart

    if(button == GLUT_MIDDLE_BUTTON):
        action = "TRANS"
    Xstart = x
    yStart = y
    print(x,y)

#-----------------------------------------
# motion 
#-----------------------------------------
def motion(x,y):
    global zoom,xStart,yStart,xTrans,yTrans
    
    if(action == "TRANS"):
        xTrans =  x 
        yTrans =  y 
        
    Xstart = x
    yStart = y
    glutPostRedisplay()
    
#-----------------------------------------
# Draw 
#-----------------------------------------
def display():
    # Clear Frame buffer and Depth buffer
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    # Setup Viewing transformation, Looking z axis
    glLoadIdentity()
    gluLookAt(0,0,-g_fViewDistance, 0,0,0 , -.1,0,0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(zoom,float(g_Width)/float(g_Height), g_nearPlane, g_farPlane)
    glMatrixMode(GL_MODELVIEW)
    polarView()
    scenemodel()
    glutSwapBuffers()    
    

if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode (GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
    glutInitWindowSize(g_Width,g_Height)
    #glutInitWindowPosition (0 + 4, int(g_Height / 4))
    glutCreateWindow(b"Camera01")

    # Initialise openGL Graphics State
    StateInit()

    # Register Callback Functions
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutMouseFunc(mouse)
    glutMotionFunc(motion)
    glutMainLoop()
    
