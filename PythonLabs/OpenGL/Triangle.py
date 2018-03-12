import OpenGL.GL.shaders
from pyglet.gl import *
import ctypes

class Triangle:

    def __init__(self):
        self.triangle = [
                          -0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
                           0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
                           0.0,  0.5, 0.0, 0.0, 0.0, 1.0]

        self.vertex_shader = """
               #version 330

               in layout(location = 0) vec3 position;
               in layout(location = 1) vec3 color;
               
               out vec3 newColor;

               void main() {
                  gl_Position = vec4(position,1.0f);
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
        shader = OpenGL.GL.shaders.compileProgram(VS,FS)
        glUseProgram(shader)

        vbo = GLuint(0)
        glGenBuffers(1,vbo)
        glBindBuffer(GL_ARRAY_BUFFER,vbo)
        cFloatArray = (GLfloat * len(self.triangle))
 
        glBufferData(GL_ARRAY_BUFFER,18*4,cFloatArray(*self.triangle),GL_STATIC_DRAW)


        # position attribute in index 0
        # shader code :- in layout(location = 0) vec3 position
        glVertexAttribPointer(0,3,GL_FLOAT,GL_FALSE,24,ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        # color attribute in index 1
        # Shader Code :- in layout(location = 1) vec3 color;
        glVertexAttribPointer(1,3,GL_FLOAT,GL_FALSE,24,ctypes.c_void_p(12))
        glEnableVertexAttribArray(1)
            
