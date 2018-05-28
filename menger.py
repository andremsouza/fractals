# -*- coding: utf-8 -*-
# Compile and run this file using python3
#
# Comandos do teclado:
# Q = alternar visualização em wireframes
# Z/X = escala em X
# C/V = escala em Y
# W/A/S/D = translação em X/Y
# Setas = rotação em X/Y


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math, random
from glUtils import GLCube, randColor # Cube class for constructing cubes in OpenGL
# GLCUbe: def __init__ (self, size, origin, color, multicolor):

x0, y0, z0 = 0.0, 0.0, 0.0 # Origem
rX, rY = -30.0, -30.0 # Rotação
sX, sY = 1.0, 1.0 # Escala
fracDepth = 2 # Profundidade do fractal
wireframe = False # Visualização em wireframes

# Menger sponge
class Menger:
	depth = 0; size = 1; origin = (0, 0, 0); drawCubes = [] # list of cubes to be drawn
	def __init__(self, depth, size, origin):
		# Armazenar parâmetros
		self.depth = depth; self.size = size; self.origin = origin
		# Criar cubos
		self.make(self.depth, self.size, self.origin)

	# Desenha todos os cubos
	def draw(self):
		for i in self.drawCubes: i.draw() # draw each cube

	# Recursão para criar os cubos que serão ser desenhados
	def make(self, depth, size, origin):
		if(depth <= 0):
			self.drawCubes.append(GLCube(size, origin, randColor(), False))
			return
		newOrigin = [origin[0]-size/3, origin[1]-size/3, origin[2]-size/3]
		for i in range(3):
			for j in range(3):
				for k in range(3):
					if([i, j] != [1, 1] and [i, k] != [1, 1] and [j, k] != [1, 1]):
						self.make(depth-1, size/3, (origin[0]+(i-1)*size/3, \
							origin[1]+(j-1)*size/3, origin[2]+(k-1)*size/3))


def init() :
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
	glutInitWindowSize(700, 700)
	glutCreateWindow("Esponja de Menger")
	glEnable(GL_DEPTH_TEST)
	glClearColor(1, 1, 1, 1)

# Função para capturar os eventos de teclas ASCII
def keyPressEvent(key, x, y):
	global menger, sX, sY, fracDepth, x0, y0, wireframe
	if(key == b'\x1b'): exit(0)
	elif(key.upper() == b'Q'): wireframe = not wireframe
	elif(key.upper() == b'Z'): sX -= 0.1 # Scale X
	elif(key.upper() == b'X'): sX += 0.1
	elif(key.upper() == b'C'): sY -= 0.1 # Scale Y
	elif(key.upper() == b'V'): sY += 0.1
	elif(key.upper() == b'W'): y0 += 0.1
	elif(key.upper() == b'S'): y0 -= 0.1
	elif(key.upper() == b'D'): x0 += 0.1
	elif(key.upper() == b'A'): x0 -= 0.1
	elif(key.upper() == b'B'): 
		fracDepth -= 1 # Menger depth
		menger = Menger(fracDepth, 1.0, (0, 0, 0))
	elif(key.upper() == b'N'):
		fracDepth += 1
		menger = Menger(fracDepth, 1.0, (0, 0, 0))
	glutPostRedisplay()

# Função para capturar os eventos de teclas especiais
def specialPressEvent(key, x, y) :
	global rX, rY
	if(key == GLUT_KEY_RIGHT): rY += 5
	elif(key == GLUT_KEY_LEFT): rY -= 5
	elif(key == GLUT_KEY_UP): rX += 5
	elif(key == GLUT_KEY_DOWN): rX -= 5
	glutPostRedisplay()

# Display OpenGL
def display():
	global menger
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | \
		GL_ACCUM_BUFFER_BIT | GL_STENCIL_BUFFER_BIT)

	glLoadIdentity()

	glScale(sX, sY, 1)
	glRotatef(rX, 1, 0, 0)
	glRotatef(rY, 0, 1, 0)
	glTranslatef(x0, y0, 0)

	if(wireframe): glPolygonMode(GL_FRONT_AND_BACK, GL_LINE) # To show only wireframes
	else: glPolygonMode(GL_FRONT_AND_BACK, GL_FILL) # To return to normal

	menger.draw() # Draw menger sponge

	glFlush()
	glutSwapBuffers()

# "Main"
if __name__ == '__main__':
	while True:
		try:
			fracDepth = int(input("Digite a profundidade da esponja de Menger: "))
			if(fracDepth < 0): raise ValueError("O valor da profundidade não pode ser negativo.")
			break;
		except Exception as err:
			print("Input inválido. Erro: " + repr(err))
			continue;

	menger = Menger(fracDepth, 1.0, (0, 0, 0))
	glutInit()
	init()

	glutDisplayFunc(display)
	glutKeyboardFunc(keyPressEvent)
	glutSpecialFunc(specialPressEvent)

	glutMainLoop()