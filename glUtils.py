# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math, random

# Returns an random tuple (R, G, B) representing an RGB color
def randColor():
	return (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))

# An cube defined with a draw function for OpenGL
class GLCube:
	size = 1
	origin = (0, 0, 0)
	color = (0, 0, 0)
	def __init__ (self, size, origin, color, multicolor):
		self.size = size # tamanho da aresta
		self.origin = origin # centro
		self.color = color # cor
		self.mcolor = multicolor # boolean. mais de uma cor ou não

	def draw(self):
		v = self.size/2; # auxiliar variable for vector positioning

		if(self.mcolor): # Cuve faces with different colors
			glColor3f(self.color[0][0], self.color[0][1], self.color[0][2])
		else:
			glColor3f(self.color[0], self.color[1], self.color[2])
		# Frente
		glBegin(GL_POLYGON)
		glVertex3f(self.origin[0]-v,	self.origin[1]-v,	self.origin[2]-v)
		glVertex3f(self.origin[0]-v,	self.origin[1]+v,	self.origin[2]-v)
		glVertex3f(self.origin[0]+v,	self.origin[1]+v,	self.origin[2]-v)
		glVertex3f(self.origin[0]+v,	self.origin[1]-v,	self.origin[2]-v)
		glEnd()

		if(self.mcolor):
			glColor3f(self.color[1][0], self.color[1][1], self.color[1][2])
		# Fundo
		glBegin(GL_POLYGON)
		glVertex3f(self.origin[0]-v,	self.origin[1]-v,	self.origin[2]+v)
		glVertex3f(self.origin[0]-v,	self.origin[1]+v,	self.origin[2]+v)
		glVertex3f(self.origin[0]+v,	self.origin[1]+v,	self.origin[2]+v)
		glVertex3f(self.origin[0]+v,	self.origin[1]-v,	self.origin[2]+v)
		glEnd()

		if(self.mcolor):
			glColor3f(self.color[2][0], self.color[2][1], self.color[2][2])
		# Direita
		glBegin(GL_POLYGON)
		glVertex3f(self.origin[0]+v,	self.origin[1]-v,	self.origin[2]-v)
		glVertex3f(self.origin[0]+v,	self.origin[1]+v,	self.origin[2]-v)
		glVertex3f(self.origin[0]+v,	self.origin[1]+v,	self.origin[2]+v)
		glVertex3f(self.origin[0]+v,	self.origin[1]-v,	self.origin[2]+v)
		glEnd()

		if(self.mcolor):
			glColor3f(self.color[3][0], self.color[3][1], self.color[3][2])
		# Esquerda
		glBegin(GL_POLYGON)
		glVertex3f(self.origin[0]-v,	self.origin[1]-v,	self.origin[2]-v)
		glVertex3f(self.origin[0]-v,	self.origin[1]+v,	self.origin[2]-v)
		glVertex3f(self.origin[0]-v,	self.origin[1]+v,	self.origin[2]+v)
		glVertex3f(self.origin[0]-v,	self.origin[1]-v,	self.origin[2]+v)
		glEnd()

		if(self.mcolor):
			glColor3f(self.color[4][0], self.color[4][1], self.color[4][2])
		# Topo
		glBegin(GL_POLYGON)
		glVertex3f(self.origin[0]+v,	self.origin[1]+v,	self.origin[2]+v)
		glVertex3f(self.origin[0]+v,	self.origin[1]+v,	self.origin[2]-v)
		glVertex3f(self.origin[0]-v,	self.origin[1]+v,	self.origin[2]-v)
		glVertex3f(self.origin[0]-v,	self.origin[1]+v,	self.origin[2]+v)
		glEnd()

		if(self.mcolor):
			glColor3f(self.color[5][0], self.color[5][1], self.color[5][2])
		# Base
		glBegin(GL_POLYGON)
		glVertex3f(self.origin[0]+v,	self.origin[1]-v,	self.origin[2]+v)
		glVertex3f(self.origin[0]+v,	self.origin[1]-v,	self.origin[2]-v)
		glVertex3f(self.origin[0]-v,	self.origin[1]-v,	self.origin[2]-v)
		glVertex3f(self.origin[0]-v,	self.origin[1]-v,	self.origin[2]+v)
		glEnd()

if __name__ == '__main__':
	exit(0)