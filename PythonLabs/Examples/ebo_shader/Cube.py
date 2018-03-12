import OpenGL.GL.shaders
from pyglet.gl import *
import ctypes
import pyrr
import numpy

class Cube:

    def __init__(self):
##        self.vertices = [
##                          -0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
##                           0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
##                           0.5,  0.5, 0.0, 0.0, 0.0, 1.0,
##                          -0.5,  0.5, 0.0, 1.0, 1.0, 0.0
##                          ]
##
##        self.indices = [0,1,2,
##                        2,3,0]

        self.vertices = [
                      
                     -0.5, -0.5, 0.5, 1.0, 0.0, 0.0,
                      0.5, -0.5, 0.5, 0.0, 1.0, 0.0,
                      0.5,  0.5, 0.5, 0.0, 0.0, 1.0,
                     -0.5,  0.5, 0.5, 1.0, 1.0, 0.0,

                     -0.5, -0.5, -0.5, 1.0, 0.0, 0.0,
                      0.5, -0.5, -0.5, 0.0, 1.0, 0.0,
                      0.5,  0.5, -0.5, 0.0, 0.0, 1.0,
                     -0.5,  0.5, -0.5, 1.0, 1.0, 0.0
                     ]

        self.indices = [
                          0,1,2,2,3,0,
                          4,5,6,6,7,4,
                          4,5,1,1,0,4,
                          6,7,3,3,2,6,
                          5,6,2,2,1,5,
                          7,4,0,0,3,7
                          ]

        self.vertex_shader = """
               #version 330

               in layout(location = 0) vec3 position;
               in layout(location = 1) vec3 color;
               uniform mat4 transform;
               out vec3 newColor;

               void main() {
                  gl_Position = transform*vec4(position,1.0f);
                  newColor = color;                
               }
               """

        self.fragment_shader = """
               #version 330
               in vec3 newColor;

               out vec4 outColor;

               void main() {
                 outColor = vec4(newColor,1.0f);
               }
               """

        VS = OpenGL.GL.shaders.compileShader(self.vertex_shader,GL_VERTEX_SHADER)
        FS = OpenGL.GL.shaders.compileShader(self.fragment_shader,GL_FRAGMENT_SHADER)
        self.shader = OpenGL.GL.shaders.compileProgram(VS,FS)
        glUseProgram(self.shader)

        VBO = GLuint(0)
        glGenBuffers(1,VBO)
        glBindBuffer(GL_ARRAY_BUFFER,VBO)
        cFloatArray1 = (GLfloat * len(self.vertices))
        glBufferData(GL_ARRAY_BUFFER,(48+36)*4,cFloatArray1(*self.vertices),GL_STATIC_DRAW)

        EBO = GLuint(0)
        glGenBuffers(1,EBO)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER,EBO)
        cFloatArray2 = (GLuint * len(self.indices))
        glBufferData(GL_ELEMENT_ARRAY_BUFFER,36*4,cFloatArray2(*self.indices),GL_STATIC_DRAW)

        
        

        # position attribute in index 0
        # shader code :- in layout(location = 0) vec3 position
        glVertexAttribPointer(0,3,GL_FLOAT,GL_FALSE,24,ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        # color attribute in index 1
        # Shader Code :- in layout(location = 1) vec3 color;
        glVertexAttribPointer(1,3,GL_FLOAT,GL_FALSE,24,ctypes.c_void_p(12))
        glEnableVertexAttribArray(1)


        
                
