# OpenGL Materials for Computer Graphics

Complement material of OpenGL for Computer Graphics course.

**Teaching Assistant:** Graciella S. Favoreto

**Teacher and Supervisor:** Profa. Dra. Agma J. M. Traina  
**Institution:** University of São Paulo

---

## 📋 Pre-requisites

### Installing PyOpenGL
```bash
pip install PyOpenGL PyOpenGL-accelerate
```

### For Linux (Ubuntu/Debian) systems:

```bash
sudo apt-get install freeglut3-dev
```

### For macOS systems:

```bash
brew install freeglut
```

## 🎯 Covered Concepts

### 1. **Window Setup**

* GLUT initialization
* Window creation
* Coordinate system

### 2. **Projection System**

OpenGL uses a normalized coordinate system from -1 to 1 on each axis. The `gluOrtho2D()` function defines the visible area:

python
gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Defines the visible area from -1 to 1 on X and Y


### 3. **Basic Primitives**

* `GL_POINTS` - Points
* `GL_LINES` - Lines
* `GL_TRIANGLES` - Triangles
* `GL_POLYGON` - Polygons

### 4. **Geometric Transformations**

* **Translation**: Moves an object in space
* **Rotation**: Rotates an object around an axis
* **Scaling**: Changes the size of an object

### 5. **Interactions**

* Keyboard (normal and special keys)
* Mouse (clicks and movement)

## 💡 Important Tips

1. **Coordinate System**: By default, OpenGL uses coordinates from -1 to 1
2. **Vertex Order**: For triangles, use counter-clockwise order
3. **Colors**: RGB values should be between 0.0 and 1.0
4. **Performance**: Use `GL_TRIANGLES` for complex objects instead of `GL_POLYGON`

## 👥 PAE Monitor

* **Graciella Favoreto**: [graciellafavoreto@usp.br](mailto:graciellafavoreto@usp.br)

**Office hours**: 18:00 to 20:00 - Room 1-116 (GBDI Lab)

---

**Profa** Dra. Agma Juci Machado Traina

**Course**: Computer Graphics - ICMC/USP