import pygame
import time
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import OpenGL.GL.shaders
from Cube import Cube
import pyrr
import numpy

clock = pygame.time.Clock()
FPS=30
def DrawTriangle():
    #glDrawArrays(GL_TRIANGLES,0,3)
    #glDrawElements(GL_TRIANGLES,6,GL_UNSIGNED_INT,None)
    glDrawElements(GL_TRIANGLES,36,GL_UNSIGNED_INT,None)
    
      
def main():
      pygame.init();
      Display = (800,600)
      pygame.display.set_mode(Display,DOUBLEBUF|OPENGL)
      glEnable(GL_DEPTH_TEST)
      
      obj = Cube(0.5)
      #glPolygonMode( GL_FRONT_AND_BACK, GL_LINE )
      x,y=0,0

      while True:
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()


            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

            glClearColor(0.2,0.2,0.3,1.0)

            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            
            rot_x = pyrr.Matrix44.from_x_rotation(x)
            rot_y = pyrr.Matrix44.from_y_rotation(y)
            transformLoc = glGetUniformLocation(obj.shader,"transform")
            glUniformMatrix4fv(transformLoc,1,GL_FALSE,rot_x*rot_y)


            DrawTriangle()



            pygame.display.flip()
            clock.tick(FPS)
            x+=0.01
            y+=0.01
 
      

main()
