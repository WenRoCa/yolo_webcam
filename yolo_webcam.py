from ultralytics import YOLO
import cv2
import time

# CONFIGURACIÓN
modelo = YOLO("yolov8n.pt")  # modelo ligero

cap = cv2.VideoCapture(0)  # 0 = webcam

# Video de salida
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('deteccion.avi', fourcc, 20.0, (640, 480))

prev_time = 0

# LOOP PRINCIPAL
while True:
    ret, frame = cap.read()
    if not ret:
        print("No se pudo acceder a la cámara")
        break

    # DETECCIÓN
    resultados = modelo(frame, stream=True)

    for r in resultados:
        boxes = r.boxes

        for box in boxes:
            # Coordenadas
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Confianza
            conf = float(box.conf[0])

            # Clase
            cls = int(box.cls[0])
            nombre = modelo.names[cls]

            # Dibujar rectángulo
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Texto
            texto = f"{nombre} {conf:.2f}"
            cv2.putText(frame, texto, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

    # FPS
    current_time = time.time()
    fps = 1 / (current_time - prev_time) if prev_time != 0 else 0
    prev_time = current_time

    cv2.putText(frame, f"FPS: {int(fps)}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)

    # MOSTRAR
    cv2.imshow("YOLO Deteccion en Tiempo Real", frame)

    # Guardar video
    out.write(frame)

    # Salir con ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

# LIBERAR RECURSOS

cap.release()
out.release()
cv2.destroyAllWindows()

print(" Programa finalizado")