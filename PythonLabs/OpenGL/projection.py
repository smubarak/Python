import pygame
import time
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from Triangle import Triangle

def DrawTriangle():
    glDrawArrays(GL_TRIANGLES,0,3)
    
      
def main():
      pygame.init();
      Display = (800,600)
      pygame.display.set_mode(Display,DOUBLEBUF|OPENGL)

      obj = Triangle()
     
      glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
      DrawTriangle()
      pygame.display.flip()
      
      while True:
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
      

main()
