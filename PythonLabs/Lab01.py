import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

FOV = 45 # Field Of view in degree

def init():  
    glClearColor(0.0,0.4,0.4,1.0)
    # Which part of the 3d scene to be rendered on the 2d screen
    glMatrixMode(GL_PROJECTION)
    # Clear Matrix    
    glLoadIdentity()
    # Set Matrix
    gluPerspective(FOV,640.0/480.0,1.0,500.0)

    # Set the matrix back to modelview
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_BLEND)
    # Final Color = (A*SRC) + (B*DST)
    # Here , B = 1-A
    glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_DEPTH_TEST)
    
def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    glBegin(GL_TRIANGLES)
    glColor(0.0,1.0,0.0,1.0) # 0% Transparant
    glVertex3f(0.0,2.0,-5.0)
    glVertex3f(-2.0,-2.0,-6.0)
    glVertex3f(2.0,-2.0,-5.0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor(1.0,0.0,0.0,0.5) # 0% Transparant
    glVertex3f(-2.0,1.0,-5.0)
    glVertex3f(2.0,1.0,-6.0)
    glVertex3f(2.0,-1.0,-6.0)
    glVertex3f(-2.0,-1.0,-5.0)
    glEnd()
    glutSwapBuffers()
    
def reshape(w,h):
    if w>h:
        glViewport(int((w-h)/2),0,h,h)
    else:
        glViewport(0,int((h-w)/2),w,w)
        
if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(640,480)
    glutCreateWindow(b"Lab01")
    glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    init()
    glutMainLoop()
    
