
from OpenGL.GL import *
import numpy as np
import math 

class SlowCube:
    def __init__(self):
        self.verts = np.asfarray([(1, -1, -1),
                                 (1, 1, -1),
                                 (-1, 1, -1),
                                 (-1, -1, -1),
                                 (1, -1, 1),
                                 (1, 1, 1),
                                 (-1, -1, 1),
                                 (-1, 1, 1)])
        self.surfaces = np.array([(0, 1, 2, 3),
                                (3, 2, 7, 6),
                                (6, 7, 5, 4),
                                (4, 5, 1, 0),
                                (1, 5, 7, 2),
                                (4, 0, 3, 6)])
        self.color = np.asfarray([0,0,1])

        self.ang = 0
        self.axis = (3, 1, 1)

    def Update(self, deltaTime):
        self.ang += 50.0 * deltaTime


    def _DrawBlock(self):
        glBegin(GL_QUADS)
        for n, surface in enumersate(self.surfaces):
            for vert in surface:
                glColor3fv(self.color)
                glVertex3fv(self.verts[vert])

    def Render(self):
       m = glGetDouble(GL_MODELVIEW_MATRIX)

       glRotate(self.ang, *self.axis)
       self._DrawBlock()

       glLoadMatrix(m)
