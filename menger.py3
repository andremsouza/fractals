# -*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

rX, rY = 0.0, 0.0

#class Cube:
#    def __init__(self, size, x, y):


def init() :
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    #glutInitWindowPosition(100, -500)
    glutCreateWindow("Hello World")
    glEnable(GL_DEPTH_TEST)
    glClearColor(0, 0, 0, 0)
    #gluLookAt(0, 0, 2, 0, 0, 0, 0, 1, 0)
    
# Função para capturar os eventos do teclado
def keyPressEvent(key, x, y) :
    global rX, rY
    if(key == GLUT_KEY_RIGHT):
        rY += 5
    elif(key == GLUT_KEY_LEFT):
        rY -= 5
    elif(key == GLUT_KEY_UP):
        rX += 5
    elif(key == GLUT_KEY_DOWN):
        rX -= 5
#    global increment, toggleAnimation
    elif key == b'\x1b' :
         # Sai do programa se apertar ESC
        exit(0)

    glutPostRedisplay()
#    elif key == b'.' :
#        # Aumenta o passo do incremento
#        increment += 1
#    elif key == b',' :
#        # Diminui o passo do incremento
#        increment += -1
#    elif key == b'a' :
#        # Liga ou desliga a animação
#        toggleAnimation = not toggleAnimation

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()

    glRotatef(rX, 1, 0, 0)
    glRotatef(rY, 0, 1, 0)

    # Frente
    glBegin(GL_POLYGON)
    glColor3f(1, 0, 0); glVertex3f( -0.5,    -0.5,   -0.5)
    glColor3f(0, 1, 0); glVertex3f( -0.5,     0.5,   -0.5)
    glColor3f(0, 0, 1); glVertex3f(  0.5,     0.5,   -0.5)
    glColor3f(1, 0, 1); glVertex3f(  0.5,    -0.5,   -0.5)
    glEnd()

    # Lado branco - TRASEIRA
    glBegin(GL_POLYGON)
    glColor3f(   1.0,  1.0, 1.0 )
    glVertex3f(  0.5, -0.5, 0.5 )
    glVertex3f(  0.5,  0.5, 0.5 )
    glVertex3f( -0.5,  0.5, 0.5 )
    glVertex3f( -0.5, -0.5, 0.5 )
    glEnd()
     
    # Lado roxo - DIREITA
    glBegin(GL_POLYGON)
    glColor3f(  1.0,  0.0,  1.0 )
    glVertex3f( 0.5, -0.5, -0.5 )
    glVertex3f( 0.5,  0.5, -0.5 )
    glVertex3f( 0.5,  0.5,  0.5 )
    glVertex3f( 0.5, -0.5,  0.5 )
    glEnd()
     
    # Lado verde - ESQUERDA
    glBegin(GL_POLYGON)
    glColor3f(   0.0,  1.0,  0.0 )
    glVertex3f( -0.5, -0.5,  0.5 )
    glVertex3f( -0.5,  0.5,  0.5 )
    glVertex3f( -0.5,  0.5, -0.5 )
    glVertex3f( -0.5, -0.5, -0.5 )
    glEnd()
     
    # Lado azul - TOPO
    glBegin(GL_POLYGON)
    glColor3f(   0.0,  0.0,  1.0 )
    glVertex3f(  0.5,  0.5,  0.5 )
    glVertex3f(  0.5,  0.5, -0.5 )
    glVertex3f( -0.5,  0.5, -0.5 )
    glVertex3f( -0.5,  0.5,  0.5 )
    glEnd()

    # Lado vermelho - BASE
    glBegin(GL_POLYGON)
    glColor3f(   1.0,  0.0,  0.0 )
    glVertex3f(  0.5, -0.5, -0.5 )
    glVertex3f(  0.5, -0.5,  0.5 )
    glVertex3f( -0.5, -0.5,  0.5 )
    glVertex3f( -0.5, -0.5, -0.5 )
    glEnd()

    glFlush()
    glutSwapBuffers()

if __name__ == '__main__':
    
    glutInit()
    init()

    glutDisplayFunc(display)
    glutSpecialFunc(keyPressEvent)

    glutMainLoop()