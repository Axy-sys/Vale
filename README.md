# Vale - Flower Visualization

Este proyecto visualiza flores usando datos JSON. Contiene dos implementaciones:
- **Versión Web** (Index.html): Visualización usando Canvas API de HTML5
- **Versión Python** (Flores): Visualización usando Turtle Graphics

## Contenido del Proyecto

- `Index.html` - Página web interactiva con visualización de canvas
- `Flores` - Script Python con Turtle Graphics
- `resources/sunflowers.json` - Datos de las flores en formato JSON
- `server.py` - Servidor HTTP simple para lanzar la página web

## Análisis del Código

### Index.html
Este archivo HTML contiene:
- Un canvas de 800x800 píxeles con fondo negro
- JavaScript que carga datos JSON de forma asíncrona
- Algoritmo de escalado y centrado automático para las formas
- Renderizado de regiones coloreadas usando el contexto 2D del canvas

### Flores (Python)
Este script Python utiliza:
- La librería `turtle` para gráficos
- Lectura de datos JSON con colores RGB y contornos
- Escalado y centrado similar al de la versión web
- Renderizado de formas rellenas

### resources/sunflowers.json
Archivo JSON que contiene un array de regiones, cada una con:
- `color`: Array RGB [R, G, B]
- `contour`: Array de puntos [x, y] que definen el contorno de la región

## Cómo Lanzar la Página

### Opción 1: Usando el servidor Python incluido (Recomendado)

```bash
python3 server.py
```

El servidor se iniciará en http://localhost:8000 y abrirá automáticamente el navegador.

### Opción 2: Usando Python's SimpleHTTPServer

```bash
python3 -m http.server 8000
```

Luego abre tu navegador en: http://localhost:8000/Index.html

### Opción 3: Ejecutar la versión Python con Turtle

```bash
python3 Flores
```

Esto abrirá una ventana de Turtle Graphics con la visualización.

## Requisitos

- **Para la versión web**: Un navegador moderno (Chrome, Firefox, Safari, Edge)
- **Para la versión Python**: Python 3.x con la librería `turtle` (incluida por defecto)

## Estructura de Datos

El formato JSON esperado es:

```json
[
  {
    "color": [R, G, B],
    "contour": [
      [x1, y1],
      [x2, y2],
      ...
    ]
  }
]
```

Donde:
- `color`: Valores RGB entre 0-255
- `contour`: Coordenadas de los puntos que forman el contorno de la región
