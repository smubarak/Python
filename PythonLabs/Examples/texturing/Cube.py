import OpenGL.GL.shaders
from pyglet.gl import *
import ctypes
import pyrr
import numpy
from PIL import Image

class Cube:

    def __init__(self,s):


        self.vertices = [
                    #       Vertex         Color      Texel     
                          -s, -s,  s,  1.0, 0.0, 0.0, 0.0, 0.0,
                           s, -s,  s,  0.0, 1.0, 0.0, 1.0, 0.0,
                           s,  s,  s,  0.0, 0.0, 1.0, 1.0, 1.0,
                          -s,  s,  s,  1.0, 1.0, 0.0, 0.0, 1.0,

                          -s, -s, -s,  1.0, 0.0, 0.0, 0.0, 0.0,
                           s, -s, -s,  0.0, 1.0, 0.0, 1.0, 0.0,
                           s,  s, -s,  0.0, 0.0, 1.0, 1.0, 1.0,
                          -s,  s, -s,  1.0, 1.0, 0.0, 0.0, 1.0,

                           s, -s, -s,  1.0, 0.0, 0.0, 0.0, 0.0,
                           s,  s, -s,  0.0, 1.0, 0.0, 1.0, 0.0,
                           s,  s,  s,  0.0, 0.0, 1.0, 1.0, 1.0,
                           s, -s,  s,  1.0, 1.0, 0.0, 0.0, 1.0,

                          -s,  s, -s,  1.0, 0.0, 0.0, 0.0, 0.0,
                          -s, -s, -s,  0.0, 1.0, 0.0, 1.0, 0.0,
                          -s, -s,  s,  0.0, 0.0, 1.0, 1.0, 1.0,
                          -s,  s,  s,  1.0, 1.0, 0.0, 0.0, 1.0,
                          
                          -s, -s, -s,  1.0, 0.0, 0.0, 0.0, 0.0,
                           s, -s, -s,  0.0, 1.0, 0.0, 1.0, 0.0,
                           s, -s,  s,  0.0, 0.0, 1.0, 1.0, 1.0,
                          -s, -s,  s,  1.0, 1.0, 0.0, 0.0, 1.0,

                           s,  s, -s,  1.0, 0.0, 0.0, 0.0, 0.0,
                          -s,  s, -s,  0.0, 1.0, 0.0, 1.0, 0.0,
                          -s,  s,  s,  0.0, 0.0, 1.0, 1.0, 1.0,
                           s,  s,  s,  1.0, 1.0, 0.0, 0.0, 1.0                       

                     ]

        self.indices = [ #  Tri0       Tri1  
                           0, 1, 2,  2, 3, 0, # Face1
                           4, 5, 6,  6, 7, 4, # Face2
                           9, 8,10, 10,11, 8, # Face3
                          12,13,14, 14,15,12, # Face4
                          16,17,18, 18,19,16, # Face5
                          20,21,22, 22,23,20  # Face6
                          ]

        self.vertex_shader = """
               #version 330

               in layout(location = 0) vec3 position;
               in layout(location = 1) vec3 color;
               in layout(location = 2) vec2 texcoord;
               out vec2 newTex;
               uniform mat4 transform;
               out vec3 newColor;

               void main() {
                  gl_Position = transform*vec4(position,1.0f);
                  newColor = color;
                  newTex = texcoord;
               }
               """

        # gvec texture(gsampler sampler​, vec texCoord​[, float bias​]);
        #   This samples the texture given by sampler​, at the location texCoord​
        self.fragment_shader = """
               #version 330
               in vec3 newColor;
               in vec2 newTex;
               uniform sampler2D samplerTexture;

               out vec4 outColor;

               void main() {
                 vec4 texel = texture(samplerTexture,newTex);
                 texel.a=0.5;
                 outColor = texel;
                 
               }
               """

        VS = OpenGL.GL.shaders.compileShader(self.vertex_shader,GL_VERTEX_SHADER)
        FS = OpenGL.GL.shaders.compileShader(self.fragment_shader,GL_FRAGMENT_SHADER)
        self.shader = OpenGL.GL.shaders.compileProgram(VS,FS)
        
        # Vertex Buffer Object  
        VBO = GLuint(0)
        glGenBuffers(1,VBO)
        glBindBuffer(GL_ARRAY_BUFFER,VBO)
        cFloatArray1 = (GLfloat * len(self.vertices))
        glBufferData(GL_ARRAY_BUFFER,(8*24+36)*4,cFloatArray1(*self.vertices),GL_STATIC_DRAW)

        # Index Buffer Object
        EBO = GLuint(0)
        glGenBuffers(1,EBO)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER,EBO)
        cFloatArray2 = (GLuint * len(self.indices))
        glBufferData(GL_ELEMENT_ARRAY_BUFFER,36*4,cFloatArray2(*self.indices),GL_STATIC_DRAW)

        TBO = GLuint(0)
        glGenTextures(1,TBO)
        #Set texture wrapping params
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S,GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T,GL_REPEAT)

        # set texture filtering params
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR)

        #Load Image
        image=Image.open("cube.jpg")
       
        img_data =  image.tobytes()      
        
        glTexImage2D(GL_TEXTURE_2D,0,GL_RGB,image.width,image.height,0,GL_RGB,GL_UNSIGNED_BYTE,img_data)
           
        # position attribute in index 0
        # shader code :- in layout(location = 0) vec3 position
        glVertexAttribPointer(0,3,GL_FLOAT,GL_FALSE,32,ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        # color attribute in index 1
        # Shader Code :- in layout(location = 1) vec3 color;
        glVertexAttribPointer(1,3,GL_FLOAT,GL_FALSE,32,ctypes.c_void_p(12))
        glEnableVertexAttribArray(1)

        # Texel
        glVertexAttribPointer(2,2,GL_FLOAT,GL_FALSE,32,ctypes.c_void_p(24))
        glEnableVertexAttribArray(2)

        glUseProgram(self.shader)


        


        
                
