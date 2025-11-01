from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def draw_triangle():
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)  # Red
    glVertex2f(-0.5, -0.5)
    glColor3f(0.0, 1.0, 0.0)  # Green
    glVertex2f(0.5, -0.5)
    glColor3f(0.0, 0.0, 1.0)  # Blue
    glVertex2f(0.0, 0.5)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_triangle()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutCreateWindow(b"Colored Triangle")
    glutDisplayFunc(display)
    glClearColor(1.0, 1.0, 1.0, 1.0)  # White background
    glutMainLoop()

if __name__ == "__main__":
    main()