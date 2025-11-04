from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

translate_x = 0.0
translate_y = 0.0
translate_z = 0.0
rotate_x = 0.0
rotate_y = 0.0
scale_factor = 1.0

projection_mode = 'perspective'  # 'perspective' or 'orthographic'

def projection_setup(width, height):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    aspect_ratio = width / height if height > 0 else 1
    if projection_mode == 'perspective':
        gluPerspective(50, aspect_ratio, 0.1, 50.0)
        # glFrustum(-aspect_ratio, aspect_ratio, -1.0, 1.0, 2.0, 50.0)
    elif projection_mode == 'orthographic':
        if aspect_ratio >= 1:
            glOrtho(-5 * aspect_ratio, 5 * aspect_ratio, -5, 5, 0.1, 50.0)
        else:
            glOrtho(-5, 5, -5 / aspect_ratio, 5 / aspect_ratio, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

def draw_text(x, y, z, text):
    glRasterPos3f(x, y, z)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

def draw_axes():
    glBegin(GL_LINES)
    glColor3f(1, 1, 1)  
    glVertex3f(0, 0, 0)
    glVertex3f(5, 0, 0)
    glColor3f(1, 1, 1)  
    glVertex3f(0, 0, 0)
    glVertex3f(0, 5, 0)
    glColor3f(1, 1, 1) 
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 5)
    glEnd()

    glColor3f(1, 1, 1)
    for i in range(1, 6):
        draw_text(i, 0, 0, str(i))
    
    for i in range(1, 6):
        draw_text(0, i, 0, str(i))
    
    for i in range(1, 6):
        draw_text(0, 0, i, str(i))

def draw_grid():
    """Desenha um chão quadriculado para visualizar melhor as projeções"""
    glColor3f(0.3, 0.3, 0.3)  # Cinza escuro
    glBegin(GL_LINES)
    
    # Linhas paralelas ao eixo X
    for z in range(-10, 11):
        glVertex3f(-10, 0, z)
        glVertex3f(10, 0, z)
    
    # Linhas paralelas ao eixo Z
    for x in range(-10, 11):
        glVertex3f(x, 0, -10)
        glVertex3f(x, 0, 10)
    
    glEnd()

def draw_scene():
    glPushMatrix()
    glTranslatef(-1.5, 0.5, 0)  # Elevado do chão
    glColor3f(1, 0, 0)
    glutSolidCube(0.5)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0, 0.5, 0)  # Elevado do chão
    glColor3f(0, 1, 1)
    glutSolidCube(0.5)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(1.5, 0.5, 0)  # Elevado do chão
    glRotatef(90, 1, 0, 0)
    glColor3f(1, 1, 0)
    glutSolidCube(0.5)
    glPopMatrix() 

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(5, 5, 6, 0.5, 0.5, 0.5, 0, 1, 0)

    # Desenhar chão quadriculado (sem transformações)
    draw_grid()
    
    draw_axes()

    # Aplicar transformações na cena
    glPushMatrix()
    glTranslatef(translate_x, translate_y, translate_z)
    glRotatef(rotate_x, 1, 0, 0)
    glRotatef(rotate_y, 0, 1, 0)
    glScalef(scale_factor, scale_factor, scale_factor)
    draw_scene()
    glPopMatrix()

    # Mostrar modo de projeção na tela
    glColor3f(1, 1, 1)
    glRasterPos3f(-4, 4, 0)
    text = f"Projecao: {projection_mode.upper()} (tecla P)"
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

    glutSwapBuffers()

def keyboard(key, x, y):
    global rotate_x, rotate_y, scale_factor, projection_mode  
    
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

    # Alternar projeção com P
    elif key == b'p' or key == b'P':
        projection_mode = 'orthographic' if projection_mode == 'perspective' else 'perspective'
        projection_setup(600, 600)
        print(f"Projecao alterada para: {projection_mode}")  # Debug
    
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
    projection_setup(600, 600)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Cena 3D - Projecoes")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(projection_setup)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special_keys)
    
    print("="*60)
    print("CONTROLES:")
    print("  P           : Alternar Projecao (Perspectiva/Ortografica)")
    print("  W/S         : Rotacionar X")
    print("  A/D         : Rotacionar Y")
    print("  Setas       : Transladar X/Y")
    print("  +/-         : Escala")
    print("="*60)
    
    glutMainLoop()

if __name__ == "__main__":
    main()