import cv2
import numpy as np
import matplotlib.pyplot as plt

# Leer la imagen
imagen = cv2.imread('Python con derivadas\imagen.jpg')
# Aplicar un filtro de desenfoque para suavizar la imagen
# Aplicar el operador de Sobel para calcular las derivadas en las direcciones x e y
derivada_x_textura = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=3)
derivada_y_textura = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize=3)

# Calcular la magnitud del gradiente
magnitud_gradiente_textura = np.sqrt(derivada_x_textura**2 + derivada_y_textura**2)

# Visualizar la imagen de textura y la magnitud del gradiente
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1), plt.imshow(imagen, cmap='gray'), plt.title('Imagen de Textura')
plt.subplot(1, 2, 2), plt.imshow(magnitud_gradiente_textura, cmap='gray'), plt.title('Magnitud del Gradiente (Textura)')
plt.show()