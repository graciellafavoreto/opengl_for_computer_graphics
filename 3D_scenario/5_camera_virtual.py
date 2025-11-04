from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Parâmetros da câmera
camera_x = 10.0
camera_y = 5.0
camera_z = 12.0
camera_rotation_h = -35  # Rotação horizontal (Y)
camera_rotation_v = 0.0  # Rotação vertical (X)
camera_zoom = 1.0

projection_mode = 'perspective'  # 'perspective' or 'orthographic'

def projection_setup(width, height):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    aspect_ratio = width / height if height > 0 else 1
    if projection_mode == 'perspective':
        gluPerspective(50, aspect_ratio, 0.1, 50.0)
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
    
    # Aplicar transformações da câmera
    glScalef(camera_zoom, camera_zoom, camera_zoom)  # Zoom (escala)
    glRotatef(camera_rotation_v, 1, 0, 0)  # Rotação vertical
    glRotatef(camera_rotation_h, 0, 1, 0)  # Rotação horizontal
    glTranslatef(-camera_x, -camera_y, -camera_z)  # Posição da câmera
    
    # Desenhar elementos da cena
    draw_grid()
    draw_axes()
    draw_scene()

    # Mostrar informações na tela
    glLoadIdentity()
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, 600, 0, 600)
    glMatrixMode(GL_MODELVIEW)
    
    glColor3f(1, 1, 1)
    glRasterPos2f(10, 580)
    text = f"Projecao: {projection_mode.upper()} (tecla P)"
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
    
    glRasterPos2f(10, 560)
    text = f"Camera: X={camera_x:.1f} Y={camera_y:.1f} Z={camera_z:.1f}"
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
    
    glRasterPos2f(10, 540)
    text = f"Rotacao: H={camera_rotation_h:.1f} V={camera_rotation_v:.1f}"
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
    
    glRasterPos2f(10, 520)
    text = f"Zoom: {camera_zoom:.1f}x"
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
    
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

    glutSwapBuffers()

def keyboard(key, x, y):
    global camera_rotation_h, camera_rotation_v, camera_zoom, projection_mode  
    
    # Rotação com W/A/S/D
    if key == b'w' or key == b'W':
        camera_rotation_v += 5
    elif key == b's' or key == b'S':
        camera_rotation_v -= 5
    elif key == b'a' or key == b'A':
        camera_rotation_h += 5
    elif key == b'd' or key == b'D':
        camera_rotation_h -= 5
    
    # Zoom com +/-
    elif key == b'+' or key == b'=':
        camera_zoom += 0.1
    elif key == b'-' or key == b'_':
        camera_zoom = max(0.1, camera_zoom - 0.1)

    # Alternar projeção com P
    elif key == b'p' or key == b'P':
        projection_mode = 'orthographic' if projection_mode == 'perspective' else 'perspective'
        projection_setup(600, 600)
        print(f"Projecao alterada para: {projection_mode}")
    
    glutPostRedisplay()

def special_keys(key, x, y):
    global camera_x, camera_y, camera_z
    
    # Translação da câmera com setas
    if key == GLUT_KEY_UP:
        camera_z -= 0.1  # Mover câmera para frente
    elif key == GLUT_KEY_DOWN:
        camera_z += 0.1  # Mover câmera para trás
    elif key == GLUT_KEY_LEFT:
        camera_x -= 0.1  # Mover câmera para esquerda
    elif key == GLUT_KEY_RIGHT:
        camera_x += 0.1  # Mover câmera para direita
    
    glutPostRedisplay()

def init():
    glClearColor(0, 0, 0, 1)
    projection_setup(600, 600)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Cena 3D - Controle de Camera")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(projection_setup)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special_keys)
    
    print("="*60)
    print("CONTROLES DA CAMERA:")
    print("  P           : Alternar Projecao (Perspectiva/Ortografica)")
    print("  W/S         : Rotacionar Verticalmente (5°)")
    print("  A/D         : Rotacionar Horizontalmente (5°)")
    print("  Setas ↑/↓   : Transladar Z - Frente/Tras (0.1)")
    print("  Setas ←/→   : Transladar X - Esquerda/Direita (0.1)")
    print("  +/-         : Zoom In/Out (10%)")
    print("="*60)
    
    glutMainLoop()

if __name__ == "__main__":
    main()