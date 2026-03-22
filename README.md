# 🎥 Detección de Objetos en Tiempo Real con YOLOv8

Este proyecto implementa un sistema de **detección de objetos en tiempo real** utilizando el modelo **YOLOv8** y la cámara web.

---

## 🚀 ¿Qué hace este proyecto?

- Detecta objetos en tiempo real usando la webcam
- Muestra **bounding boxes**, etiquetas y confianza
- Calcula **FPS (frames por segundo)**
- Permite **grabar el video procesado**

---

## 📁 Estructura del proyecto


yolo_webcam/
│
├── yolo_webcam.py
├── deteccion.avi (salida generada)


---

## ⚙️ Instalación

Instala las dependencias:

```bash
python -m pip install ultralytics opencv-python
▶️ Uso

Ejecuta el programa:

python yolo_webcam.py

👉 Se abrirá la cámara y comenzará la detección en tiempo real.

⌨️ Controles
ESC → Salir del programa
🧠 ¿Cómo funciona?
Se utiliza el modelo pre-entrenado YOLOv8n (ligero y rápido)
Cada frame del video es procesado en tiempo real
Se detectan múltiples objetos simultáneamente
Se dibujan cajas delimitadoras y etiquetas
📊 Resultados
Detección en tiempo real con buena precisión
FPS aproximado en CPU: 7–15 FPS
Soporta múltiples objetos en escena
⚠️ Problemas comunes
❌ No abre la cámara

Intenta cambiar:

cv2.VideoCapture(0)

por:

cv2.VideoCapture(1)
❌ Va lento
Es normal en CPU
Solución: usar GPU o modelo más pequeño
💡 Mejoras posibles
Usar GPU para mayor rendimiento
Implementar interfaz gráfica (GUI)
Guardar capturas de detecciones
Entrenar YOLO con dataset propio
🧪 Tecnologías utilizadas
Python
YOLOv8 (Ultralytics)
OpenCV
👩‍💻 Autor

NWRC - Wen Rocha
