from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

"""
Tecla 'f' - Flat Shading
Tecla 's' - Smooth Shading (Gouraud)
"""

use_smooth = True  # Começa com smooth shading
angle = 0.0

def draw_sphere_comparison():
    """Desenha duas esferas lado a lado para comparação"""
    
    # Esfera esquerda - com o shading model atual
    glPushMatrix()
    glTranslatef(-2.5, 0, 0)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.8, 0.2, 0.2, 1.0])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    glMaterialfv(GL_FRONT, GL_SHININESS, [100.0])
    
    # Desenha esfera com poucas subdivisões para ver a diferença
    glutSolidSphere(1.0, 10, 10)  # 10 slices, 10 stacks
    glPopMatrix()
    
    # Esfera direita - com muitas subdivisões
    glPushMatrix()
    glTranslatef(2.5, 0, 0)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.2, 0.2, 0.8, 1.0])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    glMaterialfv(GL_FRONT, GL_SHININESS, [100.0])
    
    # Mais subdivisões = diferença menos perceptível
    glutSolidSphere(1.0, 30, 30)  # 30 slices, 30 stacks
    glPopMatrix()

def draw_custom_sphere_flat():
    """
    Desenha uma esfera personalizada para demonstrar FLAT shading
    Cada face tem uma cor uniforme
    """
    import math
    
    glPushMatrix()
    glTranslatef(0, -3, 0)
    
    slices = 8
    stacks = 8
    radius = 1.0
    
    for i in range(stacks):
        lat0 = math.pi * (-0.5 + float(i) / stacks)
        z0 = radius * math.sin(lat0)
        zr0 = radius * math.cos(lat0)
        
        lat1 = math.pi * (-0.5 + float(i + 1) / stacks)
        z1 = radius * math.sin(lat1)
        zr1 = radius * math.cos(lat1)
        
        glBegin(GL_QUAD_STRIP)
        for j in range(slices + 1):
            lng = 2 * math.pi * float(j) / slices
            x = math.cos(lng)
            y = math.sin(lng)
            
            # Normal para o vértice (para smooth) ou face (para flat)
            glNormal3f(x * zr0, y * zr0, z0)
            glVertex3f(x * zr0, y * zr0, z0)
            
            glNormal3f(x * zr1, y * zr1, z1)
            glVertex3f(x * zr1, y * zr1, z1)
        glEnd()
    
    glPopMatrix()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    # Câmera
    gluLookAt(0, 2, 10,
              0, 0, 0,
              0, 1, 0)
    
    # Configura o modelo de tonalização
    if use_smooth:
        glShadeModel(GL_SMOOTH)  # Gouraud Shading (interpolação de cores)
    else:
        glShadeModel(GL_FLAT)    # Flat Shading (cor uniforme por face)
    
    # Luz posicionada
    light_pos = [5.0, 5.0, 5.0, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
    
    # Desenha as esferas
    draw_sphere_comparison()
    
    # Desenha esfera customizada
    glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.2, 0.8, 0.2, 1.0])
    draw_custom_sphere_flat()
    
    # Informações na tela
    glDisable(GL_LIGHTING)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, 800, 0, 600)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    
    glColor3f(1, 1, 1)
    
    # Título
    mode_text = "SMOOTH SHADING (Gouraud)" if use_smooth else "FLAT SHADING"
    glRasterPos2i(250, 580)
    for char in mode_text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
    
    # Descrições
    y = 550
    descriptions = [
        "Esquerda: Poucos poligonos (10x10)",
        "Direita: Muitos poligonos (30x30)",
        "Baixo: Esfera customizada (8x8)",
        "",
        "[F] Flat Shading",
        "[S] Smooth Shading",
    ]
    
    for text in descriptions:
        glRasterPos2i(10, y)
        for char in text:
            glutBitmapCharacter(GLUT_BITMAP_9_BY_15, ord(char))
        y -= 20
    
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_LIGHTING)
    
    glutSwapBuffers()

def keyboard(key, x, y):
    """Controles"""
    global use_smooth
    
    if key == b's' or key == b'S':
        use_smooth = True
        print("Mudou para SMOOTH SHADING (Gouraud)")
    elif key == b'f' or key == b'F':
        use_smooth = False
        print("Mudou para FLAT SHADING")
    elif key == b'\x1b':
        exit()
    
    glutPostRedisplay()

def init():
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glEnable(GL_DEPTH_TEST)
    
    # Iluminação
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, 800.0/600.0, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    
    print("\nControles:")
    print("  F - Flat Shading")
    print("  S - Smooth Shading")
    print("  ESC - Sair\n")

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Modelos de Tonalizacao")
    
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMainLoop()

if __name__ == "__main__":
    main()
