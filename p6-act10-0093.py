import cv2
import numpy as np

# VISION ARTIFICIAL ACT.10 NC=0093

# 1. Carga e impresión de la imagen en escala de grises
img_corvette = cv2.imread("Corvette.jpg", cv2.IMREAD_GRAYSCALE)

if img_corvette is not None:
    cv2.imshow("Corvette 0093", img_corvette)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: No se encontro 'Corvette.jpg'. Revisa la ruta del archivo.")

# 2. Dibujar Linea
print("==LA LINEA 0093==")
img = np.zeros((512, 512, 3), np.uint8)
img = cv2.line(img, (0, 0), (511, 511), (255, 255, 255), 3)
cv2.imshow("LA LINEA 0093", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3. Dibujar Circulo
print("==EL CIRCULO 0093==")
img = cv2.circle(img, (260, 260), 10, (255, 0, 0), -1)
cv2.imshow("El CIRCULO 0093", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 4. Añadir Texto
print("==EL TEXTO 0093==")
img = cv2.putText(
    img,
    "PEDRO MARTINEZ 0093",
    (200, 30),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.5,
    (255, 255, 255),
    2,
)
cv2.imshow("El TEXTO 0093", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 5. Trackbars
print("== Trackbars 0093==")


def on_trackbar(val):
    print(val)


img_trackbar = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow("frame")

cv2.createTrackbar("R", "frame", 0, 255, on_trackbar)
cv2.createTrackbar("G", "frame", 0, 255, on_trackbar)
cv2.createTrackbar("B", "frame", 0, 255, on_trackbar)

while True:
    cv2.imshow("frame", img_trackbar)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # Tecla ESC
        break

    # Se protege con try-except para evitar el error 'NULL window' si se cierra la 'X'
    try:
        r = cv2.getTrackbarPos("R", "frame")
        g = cv2.getTrackbarPos("G", "frame")
        b = cv2.getTrackbarPos("B", "frame")
    except cv2.error:
        break  # Sale del ciclo suavemente si la ventana ya no existe

    img_trackbar[:] = [b, g, r]

cv2.destroyAllWindows()

# 6. Thresholding
print("==Thresholding 0093==")
img_thresh = cv2.imread("Corvette.jpg", 0)

if img_thresh is not None:
    ret, thr1 = cv2.threshold(img_thresh, 127, 255, cv2.THRESH_BINARY)
    ret, thr2 = cv2.threshold(img_thresh, 127, 255, cv2.THRESH_BINARY_INV)
    ret, thr3 = cv2.threshold(img_thresh, 127, 255, cv2.THRESH_TRUNC)
    ret, thr4 = cv2.threshold(img_thresh, 127, 255, cv2.THRESH_TOZERO)
    ret, thr5 = cv2.threshold(img_thresh, 127, 255, cv2.THRESH_TOZERO_INV)

    cv2.imshow("BINARY", thr1)
    cv2.imshow("BINARY_INV", thr2)
    cv2.imshow("TRUNC", thr3)
    cv2.imshow("TOZERO", thr4)
    cv2.imshow("TOZERO_INV", thr5)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error al cargar la imagen para Thresholding.")
print("Pedro Martinez 0093")