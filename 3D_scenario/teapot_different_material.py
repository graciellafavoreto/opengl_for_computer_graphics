from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Dicionário com todos os materiais da tabela
MATERIALS = {
    'emerald': {
        'ambient': [0.0215, 0.1745, 0.0215, 1.0],
        'diffuse': [0.07568, 0.61424, 0.07568, 1.0],
        'specular': [0.633, 0.727811, 0.633, 1.0],
        'shininess': 0.6 * 128
    },
    'jade': {
        'ambient': [0.135, 0.2225, 0.1575, 1.0],
        'diffuse': [0.54, 0.89, 0.63, 1.0],
        'specular': [0.316228, 0.316228, 0.316228, 1.0],
        'shininess': 0.1 * 128
    },
    'obsidian': {
        'ambient': [0.05375, 0.05, 0.06625, 1.0],
        'diffuse': [0.18275, 0.17, 0.22525, 1.0],
        'specular': [0.332741, 0.328634, 0.346435, 1.0],
        'shininess': 0.3 * 128
    },
    'pearl': {
        'ambient': [0.25, 0.20725, 0.20725, 1.0],
        'diffuse': [1.0, 0.829, 0.829, 1.0],
        'specular': [0.296648, 0.296648, 0.296648, 1.0],
        'shininess': 0.088 * 128
    },
    'ruby': {
        'ambient': [0.1745, 0.01175, 0.01175, 1.0],
        'diffuse': [0.61424, 0.04136, 0.04136, 1.0],
        'specular': [0.727811, 0.626959, 0.626959, 1.0],
        'shininess': 0.6 * 128
    },
    'turquoise': {
        'ambient': [0.1, 0.18725, 0.1745, 1.0],
        'diffuse': [0.396, 0.74151, 0.69102, 1.0],
        'specular': [0.297254, 0.30829, 0.306678, 1.0],
        'shininess': 0.1 * 128
    },
    'brass': {
        'ambient': [0.329412, 0.223529, 0.027451, 1.0],
        'diffuse': [0.780392, 0.568627, 0.113725, 1.0],
        'specular': [0.992157, 0.941176, 0.807843, 1.0],
        'shininess': 0.21794872 * 128
    },
    'bronze': {
        'ambient': [0.2125, 0.1275, 0.054, 1.0],
        'diffuse': [0.714, 0.4284, 0.18144, 1.0],
        'specular': [0.393548, 0.271906, 0.166721, 1.0],
        'shininess': 0.2 * 128
    },
    'chrome': {
        'ambient': [0.25, 0.25, 0.25, 1.0],
        'diffuse': [0.4, 0.4, 0.4, 1.0],
        'specular': [0.774597, 0.774597, 0.774597, 1.0],
        'shininess': 0.6 * 128
    },
    'copper': {
        'ambient': [0.19125, 0.0735, 0.0225, 1.0],
        'diffuse': [0.7038, 0.27048, 0.0828, 1.0],
        'specular': [0.256777, 0.137622, 0.086014, 1.0],
        'shininess': 0.1 * 128
    },
    'gold': {
        'ambient': [0.24725, 0.1995, 0.0745, 1.0],
        'diffuse': [0.75164, 0.60648, 0.22648, 1.0],
        'specular': [0.628281, 0.555802, 0.366065, 1.0],
        'shininess': 0.4 * 128
    },
    'silver': {
        'ambient': [0.19225, 0.19225, 0.19225, 1.0],
        'diffuse': [0.50754, 0.50754, 0.50754, 1.0],
        'specular': [0.508273, 0.508273, 0.508273, 1.0],
        'shininess': 0.4 * 128
    },
    'black_plastic': {
        'ambient': [0.0, 0.0, 0.0, 1.0],
        'diffuse': [0.01, 0.01, 0.01, 1.0],
        'specular': [0.50, 0.50, 0.50, 1.0],
        'shininess': 0.25 * 128
    },
    'cyan_plastic': {
        'ambient': [0.0, 0.1, 0.06, 1.0],
        'diffuse': [0.0, 0.50980392, 0.50980392, 1.0],
        'specular': [0.50196078, 0.50196078, 0.50196078, 1.0],
        'shininess': 0.25 * 128
    },
    'green_plastic': {
        'ambient': [0.0, 0.0, 0.0, 1.0],
        'diffuse': [0.1, 0.35, 0.1, 1.0],
        'specular': [0.45, 0.55, 0.45, 1.0],
        'shininess': 0.25 * 128
    },
    'red_plastic': {
        'ambient': [0.0, 0.0, 0.0, 1.0],
        'diffuse': [0.5, 0.0, 0.0, 1.0],
        'specular': [0.7, 0.6, 0.6, 1.0],
        'shininess': 0.25 * 128
    },
    'white_plastic': {
        'ambient': [0.0, 0.0, 0.0, 1.0],
        'diffuse': [0.55, 0.55, 0.55, 1.0],
        'specular': [0.70, 0.70, 0.70, 1.0],
        'shininess': 0.25 * 128
    },
    'yellow_plastic': {
        'ambient': [0.0, 0.0, 0.0, 1.0],
        'diffuse': [0.5, 0.5, 0.0, 1.0],
        'specular': [0.60, 0.60, 0.50, 1.0],
        'shininess': 0.25 * 128
    },
    'black_rubber': {
        'ambient': [0.02, 0.02, 0.02, 1.0],
        'diffuse': [0.01, 0.01, 0.01, 1.0],
        'specular': [0.4, 0.4, 0.4, 1.0],
        'shininess': 0.078125 * 128
    },
    'cyan_rubber': {
        'ambient': [0.0, 0.05, 0.05, 1.0],
        'diffuse': [0.4, 0.5, 0.5, 1.0],
        'specular': [0.04, 0.7, 0.7, 1.0],
        'shininess': 0.078125 * 128
    },
    'green_rubber': {
        'ambient': [0.0, 0.05, 0.0, 1.0],
        'diffuse': [0.4, 0.5, 0.4, 1.0],
        'specular': [0.04, 0.7, 0.04, 1.0],
        'shininess': 0.078125 * 128
    },
    'red_rubber': {
        'ambient': [0.05, 0.0, 0.0, 1.0],
        'diffuse': [0.5, 0.4, 0.4, 1.0],
        'specular': [0.7, 0.04, 0.04, 1.0],
        'shininess': 0.078125 * 128
    },
    'white_rubber': {
        'ambient': [0.05, 0.05, 0.05, 1.0],
        'diffuse': [0.5, 0.5, 0.5, 1.0],
        'specular': [0.7, 0.7, 0.7, 1.0],
        'shininess': 0.078125 * 128
    },
    'yellow_rubber': {
        'ambient': [0.05, 0.05, 0.0, 1.0],
        'diffuse': [0.5, 0.5, 0.4, 1.0],
        'specular': [0.7, 0.7, 0.04, 1.0],
        'shininess': 0.078125 * 128
    }
}

current_material = 'gold'

# aplica material selecionado
def apply_material(material_name):
    if material_name in MATERIALS:
        mat = MATERIALS[material_name]
        glMaterialfv(GL_FRONT, GL_AMBIENT, mat['ambient'])
        glMaterialfv(GL_FRONT, GL_DIFFUSE, mat['diffuse'])
        glMaterialfv(GL_FRONT, GL_SPECULAR, mat['specular'])
        glMaterialf(GL_FRONT, GL_SHININESS, mat['shininess'])

# configura iluminação básica
def setup_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_NORMALIZE)
    
    # COMPONENTE AMBIENTE
    # Luz que "está no ar", ilumina tudo uniformemente
    # [R, G, B, Alpha]
    # 0.2 = 20% de intensidade (luz fraca ambiente)
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])
    
    # COMPONENTE DIFUSA
    # Luz direcional principal, cria sombreamento
    # [1.0, 1.0, 1.0] = luz branca 100% (revela cores reais dos materiais)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
    
    # COMPONENTE ESPECULAR
    # Cria reflexos brilhantes (highlights)
    # [1.0, 1.0, 1.0] = reflexos brancos brilhantes
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])
    
    # POSIÇÃO DA LUZ
    # [x, y, z, w]
    # w = 1.0: Luz PONTUAL (como uma lâmpada) na posição (5, 5, 5)
    # w = 0.0: Luz DIRECIONAL (como o sol) vindo da direção (5, 5, 5)
    glLightfv(GL_LIGHT0, GL_POSITION, [5.0, 5.0, 5.0, 1.0])

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(3, 3, 5, 0, 0, 0, 0, 1, 0)
    
    # Aplicar material selecionado
    apply_material(current_material)
    
    # Desenhar objeto
    glutSolidTeapot(1.0)
    
    # Mostrar nome do material
    glDisable(GL_LIGHTING)
    glColor3f(1, 1, 1)
    glRasterPos3f(-2, 2, 0)
    text = f"Material: {current_material} (use 1-9 para mudar)"
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))
    glEnable(GL_LIGHTING)
    
    glutSwapBuffers()

def keyboard(key, x, y):
    global current_material
    
    # Mudar material com teclas numéricas
    materials_list = list(MATERIALS.keys())
    
    if key == b'1':
        current_material = materials_list[0] if len(materials_list) > 0 else current_material
    elif key == b'2':
        current_material = materials_list[1] if len(materials_list) > 1 else current_material
    elif key == b'3':
        current_material = materials_list[2] if len(materials_list) > 2 else current_material
    elif key == b'4':
        current_material = materials_list[3] if len(materials_list) > 3 else current_material
    elif key == b'5':
        current_material = materials_list[4] if len(materials_list) > 4 else current_material
    elif key == b'6':
        current_material = materials_list[5] if len(materials_list) > 5 else current_material
    elif key == b'7':
        current_material = materials_list[6] if len(materials_list) > 6 else current_material
    elif key == b'8':
        current_material = materials_list[7] if len(materials_list) > 7 else current_material
    elif key == b'9':
        current_material = materials_list[8] if len(materials_list) > 8 else current_material
    elif key == b'n':  # Next material
        idx = materials_list.index(current_material)
        current_material = materials_list[(idx + 1) % len(materials_list)]
    elif key == b'p':  # Previous material
        idx = materials_list.index(current_material)
        current_material = materials_list[(idx - 1) % len(materials_list)]
    
    print(f"Material atual: {current_material}")
    glutPostRedisplay()

def init():
    glClearColor(0.1, 0.1, 0.15, 1.0)
    setup_lighting()
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, 1, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"OpenGL Materials Demo")
    init()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    
    print("="*60)
    print("MATERIAIS DISPONIVEIS:")
    for i, name in enumerate(list(MATERIALS.keys())[:9]):
        print(f"  {i+1}: {name}")
    print("\n  N: Proximo material")
    print("  P: Material anterior")
    print("="*60)
    
    glutMainLoop()

if __name__ == "__main__":
    main()