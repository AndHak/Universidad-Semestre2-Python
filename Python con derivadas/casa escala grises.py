import numpy as np
import matplotlib.pyplot as plt

B = np.array([[255, 255, 245, 255, 246, 255, 255, 255],
              [255, 255, 254, 46, 52, 242, 251, 252],
              [239, 255, 29, 141, 125, 42, 255, 255],
              [255, 17, 149, 131, 147, 157, 20, 249],
              [34, 39, 39, 50, 23, 42, 28, 54],
              [255, 101, 80, 90, 100, 81, 106, 249],
              [240, 89, 255, 81, 108, 49, 80, 255],
              [255, 95, 96, 94, 88, 43, 82, 255]])

# Mostrar la imagen en escala de grises
plt.imshow(B, cmap='gray')

# Agregar título
plt.title('Imagen Escala de Grises')

# Mostrar la subgráfica
plt.show()
