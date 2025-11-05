from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Intensidades das luzes
luz_difusa = 1.0
luz_especular = 1.0

# Posição da luz (fonte de luz, representando o "sol")
light_pos = [5.0, 5.0, 2.0, 1.0]  # (x, y, z, w)

def update_lighting():
    """Atualiza as componentes de iluminação e a posição da luz"""
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [luz_difusa]*3 + [1.0])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [luz_especular]*3 + [1.0])
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)

def draw_light_source():
    """Desenha uma esfera amarela representando a fonte de luz"""
    glDisable(GL_LIGHTING)
    glPushMatrix()
    glTranslatef(light_pos[0], light_pos[1], light_pos[2])
    glColor3f(1.0, 1.0, 0.0)
    glutSolidSphere(0.1, 20, 20)
    glPopMatrix()
    glEnable(GL_LIGHTING)

def draw_scene():
    # Teapot ambiente
    glPushMatrix()
    glTranslatef(-2, 0.5, 0)
    glMaterialfv(GL_FRONT, GL_AMBIENT, [1.0, 0.0, 0.0, 1.0])
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.0, 0.0, 0.0, 1.0])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [0.0, 0.0, 0.0, 1.0])
    # glutSolidSphere(0.3, 30, 30)
    glutSolidTeapot(0.5)
    glPopMatrix()

    # Teapot difusa
    glPushMatrix()
    glTranslatef(0, 0.5, 0)
    glMaterialfv(GL_FRONT, GL_AMBIENT, [1.0, 0.0, 0.0, 1.0])
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [0.0, 0.0, 0.0, 1.0])
    glutSolidTeapot(0.5)
    glPopMatrix()

    # Teapot especular
    glPushMatrix()
    glTranslatef(2, 0.5, 0)
    glMaterialfv(GL_FRONT, GL_AMBIENT, [1.0, 0.0, 0.0, 1.0])
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.0, 0.0, 0.0, 1.0])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    glMaterialf(GL_FRONT, GL_SHININESS, 128.0)
    # glutSolidSphere(0.3, 30, 30)
    glutSolidTeapot(0.5)
    glPopMatrix()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(7, 7, 8, 0, 0.5, 0, 0, 1, 0)

    draw_light_source()
    draw_scene()

    # Texto informativo
    glDisable(GL_LIGHTING)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, 600, 0, 600)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glColor3f(1, 1, 1)
    glRasterPos2f(10, 580)
    for c in f"Luz Difusa (Q/A): {luz_difusa:.1f}": glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(c))
    glRasterPos2f(10, 560)
    for c in f"Luz Especular (W/S): {luz_especular:.1f}": glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(c))
    glRasterPos2f(10, 540)
    for c in f"Posicao da Luz: ({light_pos[0]:.1f}, {light_pos[1]:.1f}, {light_pos[2]:.1f})":
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(c))

    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_LIGHTING)

    glutSwapBuffers()

def keyboard(key, x, y):
    global luz_difusa, luz_especular

    if key in [b'q', b'Q']:
        luz_difusa = min(1.0, luz_difusa + 0.1)
    elif key in [b'a', b'A']:
        luz_difusa = max(0.0, luz_difusa - 0.1)
    elif key in [b'w', b'W']:
        luz_especular = min(1.0, luz_especular + 0.1)
    elif key in [b's', b'S']:
        luz_especular = max(0.0, luz_especular - 0.1)

    update_lighting()
    glutPostRedisplay()

def special_keys(key, x, y):
    """Captura setas do teclado"""
    global light_pos

    if key == GLUT_KEY_UP:
        light_pos[1] += 0.2
    elif key == GLUT_KEY_DOWN:
        light_pos[1] -= 0.2
    elif key == GLUT_KEY_LEFT:
        light_pos[0] -= 0.2
    elif key == GLUT_KEY_RIGHT:
        light_pos[0] += 0.2

    update_lighting()
    glutPostRedisplay()

def init():
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.3, 0.3, 0.3, 1.0])
    update_lighting()

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, 1.0, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Iluminacao OpenGL - Luz Ajustavel")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special_keys)  # <== Adicionado!
    
    print("="*60)
    print("DEMONSTRAÇÃO DE ILUMINAÇÃO:")
    print("  Esquerda : Luz ambiente")
    print("  Centro   : Luz difusa")
    print("  Direita  : Luz especular")
    print()
    print("CONTROLES:")
    print("  Q/A -> Aumentar/Diminuir luz difusa")
    print("  W/S -> Aumentar/Diminuir luz especular")
    print("  ↑ ↓ ← → -> Mover a fonte de luz amarela")
    print("="*60)

    glutMainLoop()

if __name__ == "__main__":
    main()
