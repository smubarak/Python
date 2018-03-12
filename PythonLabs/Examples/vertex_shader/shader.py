from pyglet.gl import *
from Triangle import Triangle

class MyWindow(pyglet.window.Window):
    def __init__(self,*arg,**kwargs):
        super().__init__(*arg,**kwargs)
        self.set_minimum_size(400,300)
        glClearColor(0.2,0.3,0.2,1)
        self.triangle = Triangle()
        

    def on_draw(self):
        self.clear()
        glDrawArrays(GL_TRIANGLES,0,3)
        

    def on_resize(self,width,height):
        glViewport(0,0,width,height)


if __name__ == '__main__':
    window = MyWindow(1280,720,"My Shader",resizable=True)
    pyglet.app.run()
        
        
