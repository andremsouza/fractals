# -*- coding: utf-8 -*-
# Compile and run this file using python3

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math, random
from glCube import GLCube # Cube class for constructing cubes in OpenGL

rX, rY, fracDepth = 0.0, 0.0, 1

class Menger:
	depth = 1
	size = 1
	origin = (0, 0, 0)
	def __init__(self, depth, size, origin):
		self.depth = depth
		self.size = size
		self.origin = origin



def init() :
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize(700, 700)
	glutCreateWindow("Hello World")
	glEnable(GL_DEPTH_TEST)
	glClearColor(0.75, 0.75, 0.75, 0.75)
	

# Função para capturar os eventos de teclas ASCII
def keyPressEvent(key, x, y):
	if(key == b'\x1b'):
		exit(0)

# Função para capturar os eventos de teclas especiais
def specialPressEvent(key, x, y) :
	global rX, rY
	if(key == GLUT_KEY_RIGHT):
		rY += 5
	elif(key == GLUT_KEY_LEFT):
		rY -= 5
	elif(key == GLUT_KEY_UP):
		rX += 5
	elif(key == GLUT_KEY_DOWN):
		rX -= 5

	glutPostRedisplay()
#	elif key == b'.' :
#		# Aumenta o passo do incremento
#		increment += 1
#	elif key == b',' :
#		# Diminui o passo do incremento
#		increment += -1
#	elif key == b'a' :
#		# Liga ou desliga a animação
#		toggleAnimation = not toggleAnimation

def display():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	glLoadIdentity()

	glRotatef(rX, 1, 0, 0)
	glRotatef(rY, 0, 1, 0)

	#glPolygonMode(GL_FRONT_AND_BACK, GL_LINE) # To show only wireframes
	#glPolygonMode(GL_FRONT_AND_BACK, GL_FILL) # To return to normal
	
	# Drawing a cube
	cColors = (
			(0, 0, 0),
			(0, 0, 1),
			(0, 1, 0),
			(0, 1, 1),
			(1, 0, 0),
			(1, 0, 1)
		)
	GLCube(1, (0, 0, 0), cColors, 1)

	glFlush()
	glutSwapBuffers()

if __name__ == '__main__':
	
	glutInit()
	init()

	glutDisplayFunc(display)
	glutKeyboardFunc(keyPressEvent)
	glutSpecialFunc(specialPressEvent)

	glutMainLoop()