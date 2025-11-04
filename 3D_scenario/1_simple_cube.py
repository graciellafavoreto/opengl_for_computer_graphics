from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_axes():
    glBegin(GL_LINES)
    glColor3f(1, 0, 0) # red
    glVertex3f(0, 0, 0)
    glVertex3f(2, 0, 0)  # X
    glColor3f(0, 1, 0) # green
    glVertex3f(0, 0, 0)
    glVertex3f(0, 2, 0)  # Y
    glColor3f(0, 0, 1) # blue
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 2)  # Z
    glEnd()

def draw_cube():
    glBegin(GL_QUADS)
    # Frente
    glColor3f(1, 0, 0)
    glVertex3f(0, 0, 1)
    glVertex3f(1, 0, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(0, 1, 1)
    # Trás
    glColor3f(0, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 1, 0)
    glVertex3f(1, 1, 0)
    glVertex3f(1, 0, 0)
    # Topo
    glColor3f(0, 0, 1)
    glVertex3f(0, 1, 0)
    glVertex3f(0, 1, 1)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 1, 0)
    # Base
    glColor3f(1, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(1, 0, 0)
    glVertex3f(1, 0, 1)
    glVertex3f(0, 0, 1)
    # Direita
    glColor3f(1, 0, 1)
    glVertex3f(1, 0, 0)
    glVertex3f(1, 1, 0)
    glVertex3f(1, 1, 1)
    glVertex3f(1, 0, 1)
    # Esquerda
    glColor3f(0, 1, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 1)
    glVertex3f(0, 1, 1)
    glVertex3f(0, 1, 0)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(3, 3, 5, 0.5, 0.5, 0.5, 0, 1, 0)
    draw_axes()
    draw_cube()
    # glutWireTorus(0.1, 0.4, 12, 24)
    # glutWireTeapot(1.0)
    glutSwapBuffers()


def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0, 0, 0, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(50, 1, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Cena 3D")
    init()
    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()
