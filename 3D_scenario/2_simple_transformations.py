from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

translate_x = 0.0
translate_y = 0.0
translate_z = 0.0
rotate_x = 0.0
rotate_y = 0.0
scale_factor = 1.0

def draw_text(x, y, z, text):
    glRasterPos3f(x, y, z)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

def draw_axes():
    glBegin(GL_LINES)
    glColor3f(1, 1, 1) # white 
    glVertex3f(0, 0, 0)
    glVertex3f(5, 0, 0)  # X
    glColor3f(1, 1, 1) # white
    glVertex3f(0, 0, 0)
    glVertex3f(0, 5, 0)  # Y
    glColor3f(1, 1, 1) # white
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 5)  # Z
    glEnd()

    glColor3f(1, 1, 1)
    for i in range(1, 6):
        draw_text(i, 0, 0, str(i))
    
    # Adicionar números no eixo Y
    for i in range(1, 6):
        draw_text(0, i, 0, str(i))
    
    # Adicionar números no eixo Z
    for i in range(1, 6):
        draw_text(0, 0, i, str(i))

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(5, 5, 6, 0.5, 0.5, 0.5, 0, 1, 0)

    draw_axes()

    # Aplicar transformações ao bule
    glPushMatrix()
    glTranslatef(translate_x, translate_y, translate_z)
    glRotatef(rotate_x, 1, 0, 0)
    glRotatef(rotate_y, 0, 1, 0)
    glScalef(scale_factor, scale_factor, scale_factor)
    glutWireTeapot(1.0)
    glPopMatrix()

    glutSwapBuffers()

def keyboard(key, x, y):
    global rotate_x, rotate_y, scale_factor
    
    # Rotação com W/A/S/D
    if key == b'w' or key == b'W':
        rotate_x += 5
    elif key == b's' or key == b'S':
        rotate_x -= 5
    elif key == b'a' or key == b'A':
        rotate_y -= 5
    elif key == b'd' or key == b'D':
        rotate_y += 5
    
    # Escala com +/-
    elif key == b'+' or key == b'=':
        scale_factor += 0.1
    elif key == b'-' or key == b'_':
        scale_factor = max(0.1, scale_factor - 0.1)
    
    glutPostRedisplay()

def special_keys(key, x, y):
    global translate_x, translate_y, translate_z
    
    # Translação com setas
    if key == GLUT_KEY_UP:
        translate_y += 0.1
    elif key == GLUT_KEY_DOWN:
        translate_y -= 0.1
    elif key == GLUT_KEY_LEFT:
        translate_x -= 0.1
    elif key == GLUT_KEY_RIGHT:
        translate_x += 0.1
    
    glutPostRedisplay()

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
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special_keys)
    glutMainLoop()


if __name__ == "__main__":
    main()
