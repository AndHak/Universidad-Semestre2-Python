import cv2
import numpy as np
import matplotlib.pyplot as plt

imagen = cv2.imread('Python con derivadas\gato.jpg', cv2.IMREAD_GRAYSCALE)

alto, ancho = imagen.shape

#Creamos una matriz con ceros
derivada_x = np.zeros((alto, ancho))
derivada_y = np.zeros((alto, ancho))

#Para calcular la segunda derivada hacia adelante en x
for i in range(1, alto):
    #Entramos ahora en cada valor que hay en la fila, es decir los pixeles
    for j in range(1, ancho-2):
        #en la matriz con ceros en la posicion i, j
        #Hacemos los calculos correspondientes para encontrar f''(x)
        derivada_x[i, j] = imagen[i, j+2] - 2*imagen[i, j+1] + imagen[i, j]

#Para calcular la segunda derivada hacia adelante en y
for i in range(1, alto-2):
    #Entramos ahora en cada valor que hay en la fila, es decir los pixeles
    for j in range(1, ancho):
        #en la matriz con ceros en la posicion i, j
        #Hacemos los calculos correspondientes para encontrar f''(y)
        derivada_y[i, j] = imagen[i+2, j] - 2*imagen[i+1, j] + imagen[i, j]

derivada_xy = np.sqrt(derivada_x**2 + derivada_y**2)

# Primera fila: Imágenes originales y derivadas de primer orden
plt.subplot(2, 4, 1),plt.imshow(imagen, cmap="gray"),plt.title("Imagen original")
plt.subplot(2, 4, 2),plt.imshow(derivada_x, cmap="gray"),plt.title("f''(x)")
plt.subplot(2, 4, 5),plt.imshow(derivada_y, cmap="gray"),plt.title("f''(y)")
plt.subplot(2, 4, 6),plt.imshow(derivada_xy, cmap="gray"),plt.title("f''(x) + f''(y)")

plt.show()
