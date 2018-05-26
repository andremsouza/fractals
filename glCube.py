# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
#import math, random

class GLCube:
	size = 1
	origin = (0, 0, 0)
	color = (0, 0, 0)
	def __init__ (self, size, origin, color, multicolor):
		self.size = size
		self.origin = origin
		self.color = color
		v = self.size/2; # auxiliar variable for vector positioning

		if(multicolor): # Cuve faces with different colors
			glColor3f(color[0][0], color[0][1], color[0][2])
		else:
			glColor3f(color[0], color[1], color[2])
		# Frente
		glBegin(GL_POLYGON)
		glVertex3f(origin[0]-v,	origin[1]-v,	origin[2]-v)
		glVertex3f(origin[0]-v,	origin[1]+v,	origin[2]-v)
		glVertex3f(origin[0]+v,	origin[1]+v,	origin[2]-v)
		glVertex3f(origin[0]+v,	origin[1]-v,	origin[2]-v)
		glEnd()

		if(multicolor):
			glColor3f(color[1][0], color[1][1], color[1][2])
		# Fundo
		glBegin(GL_POLYGON)
		glVertex3f(origin[0]-v,	origin[1]-v,	origin[2]+v)
		glVertex3f(origin[0]-v,	origin[1]+v,	origin[2]+v)
		glVertex3f(origin[0]+v,	origin[1]+v,	origin[2]+v)
		glVertex3f(origin[0]+v,	origin[1]-v,	origin[2]+v)
		glEnd()

		if(multicolor):
			glColor3f(color[2][0], color[2][1], color[2][2])
		# Direita
		glBegin(GL_POLYGON)
		glVertex3f(origin[0]+v,	origin[1]-v,	origin[2]-v)
		glVertex3f(origin[0]+v,	origin[1]+v,	origin[2]-v)
		glVertex3f(origin[0]+v,	origin[1]+v,	origin[2]+v)
		glVertex3f(origin[0]+v,	origin[1]-v,	origin[2]+v)
		glEnd()

		if(multicolor):
			glColor3f(color[3][0], color[3][1], color[3][2])
		# Esquerda
		glBegin(GL_POLYGON)
		glVertex3f(origin[0]-v,	origin[1]-v,	origin[2]-v)
		glVertex3f(origin[0]-v,	origin[1]+v,	origin[2]-v)
		glVertex3f(origin[0]-v,	origin[1]+v,	origin[2]+v)
		glVertex3f(origin[0]-v,	origin[1]-v,	origin[2]+v)
		glEnd()

		if(multicolor):
			glColor3f(color[4][0], color[4][1], color[4][2])
		# Topo
		glBegin(GL_POLYGON)
		glVertex3f(origin[0]+v,	origin[1]+v,	origin[2]+v)
		glVertex3f(origin[0]+v,	origin[1]+v,	origin[2]-v)
		glVertex3f(origin[0]-v,	origin[1]+v,	origin[2]-v)
		glVertex3f(origin[0]-v,	origin[1]+v,	origin[2]+v)
		glEnd()

		if(multicolor):
			glColor3f(color[5][0], color[5][1], color[5][2])
		# Base
		glBegin(GL_POLYGON)
		glVertex3f(origin[0]+v,	origin[1]-v,	origin[2]+v)
		glVertex3f(origin[0]+v,	origin[1]-v,	origin[2]-v)
		glVertex3f(origin[0]-v,	origin[1]-v,	origin[2]-v)
		glVertex3f(origin[0]-v,	origin[1]-v,	origin[2]+v)
		glEnd()

if __name__ == '__main__':
	exit(0)