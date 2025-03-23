"""
Herramientas Computacionales: El Arte de la Programación

Actividad 1: Implementación de Convolución

Alumno: Jonathan Uziel Medina Rodríguez (A01255048)

Docente: Baldomero Olvera Villanueva

Fecha: 21/03/2025

Descripción: Programa que aplica filtros de convolución a una imagen con padding incluido.
"""
# Librerías
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

# Función para agregar un filtro de convolución a una imagen. Complejidad O(n^4) al tener 4 iteraciones anidadas.
def convolucion(imagen, filtro):
    filaImg, colImg, = imagen.shape                                                 # Tamaño de la imagen (m filas, n columnas).
    filaF, colF = filtro.shape                                                      # Tamaño del filtro/kernel (k filas, l columnas).

    padding_y = int((filaF - 1)/2)                                                  # Padding en el eje Y (altura).
    padding_x = int((colF - 1)/2)                                                   # Padding en el eje X (ancho).

    matriz = np.zeros(imagen.shape)                                                 # Matriz resultante de ceros.

    imagenPadding = np.zeros((filaImg + (padding_y*2), colImg + (padding_x*2)))     # Matriz de ceros de la imagen con padding añadido.
    
    imagenPadding[padding_y:imagenPadding.shape[0] - padding_y,                     # Parte de la matriz es tomada por toda la imagen.
                  padding_x:imagenPadding.shape[1] - padding_x] = imagen

    """
    Se recorre cada columna de cada fila para llevara cabo la operación de convolución:
    sumatoria del producto de cada celda del filtro y de la imagen.
    """
    for i in range(filaImg):
        for j in range(colImg):
            matriz[i][j] = np.sum(imagenPadding[i:i + filaF, j:j + colF] * filtro)

    return matriz # Retornar matriz


# Programa principal
if __name__ == "__main__":

    # Ingresar nombre o directorio del archivo. 
    archivo = input("\nIngrese el nombre de la imagen: ")

    if os.path.isfile(archivo) == False:
        # Imagen no encontrada.
        print("\nNo se pudo encontrar la imagen.")

    else:
        # Se lee la imagen.
        imagen = cv2.imread(archivo)

        # La imagen se convierte a blanco y negro (escala de grises). 
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

        # Matriz del filtro de extensión de punto.
        filtro1 = np.array([[-0.627,  0.352, -0.627],
                           [0.352, 2.923, 0.352],
                           [-0.627,  0.352, -0.627]])  
        
        # Matriz de convolución 1.
        matriz1 = convolucion(imagen, filtro1)

        # Matriz del filtro de suavizado 3x3.
        filtro2 = np.array([[1, 2, 1],
                            [2, 4, 2],
                            [1, 2, 1]])  
        
        # Matriz de convolución 2.
        matriz2 = convolucion(imagen, filtro2)

        # Matriz del filtro de nitidez 3x3.
        filtro3 = np.array([[-1, -1, -1],
                            [-1,  9, -1], 
                            [-1, -1, -1]])  
        
        # Matriz de convolución 3.
        matriz3 = convolucion(imagen, filtro3)

        # Matriz de mi propio filtro.
        filtro4 = np.array([[-1,-0.5,-1], 
                            [-2,0.33,-2],
                            [-1,-0.5,-1]])   
        
        # Matriz de convolución 4.
        matriz4 = convolucion(imagen, filtro4)

        # Mostrar la convolución de la imagen con el filtro 1 en la 1era. posición.
        plt.subplot(2, 2, 1)
        plt.axis("off")
        plt.imshow(matriz1, cmap="gray")
        plt.title("Convolución de la Imagen con Filtro de Extensión de Punto")

        # Mostrar la convolución de la imagen con el filtro 2 en la 2da. posición.
        plt.subplot(2, 2, 2)
        plt.axis("off")
        plt.imshow(matriz2, cmap="gray")
        plt.title("Convolución de la Imagen con Filtro de Suavizado 3X3")

        # Mostrar la convolución de la imagen con el filtro 3 en la 3era. posición.
        plt.subplot(2, 2, 3)
        plt.axis("off")
        plt.imshow(matriz3, cmap="gray", )
        plt.title("Convolución de la Imagen con Filtro de Nitidez 3X3")
        
        # Mostrar la convolución de la imagen con el filtro 4 en la 4ta. posición.
        plt.subplot(2, 2, 4)
        plt.axis("off")
        plt.imshow(matriz4, cmap="gray", )
        plt.title("Convolución de la Imagen con mi Propio Filtro")

        # Mostrar las imágenes.
        plt.show()

"""
Referencias:

- Función de convolución. (s. f.). ArcGIS Desktop. Recuperado el 20 de marzo de 2025 de https://desktop.arcgis.com/es/arcmap/latest/manage-data/raster-and-images/convolution-function.htm
- GeeksforGeeks. (2020a, 22 abril). Matplotlib.pyplot.imshow() in Python. GeeksforGeeks. Recuperado el 20 de marzo de 2025 de https://www.geeksforgeeks.org/matplotlib-pyplot-imshow-in-python/
- GeeksforGeeks. (2022b, 10 febrero). How to Fix: ValueError: setting an array element with a sequence. GeeksforGeeks. Recuperado el 20 de marzo de 2025 de https://www.geeksforgeeks.org/how-to-fix-valueerror-setting-an-array-element-with-a-sequence/
- GeeksforGeeks. (2023c, 14 marzo). Introduction to Convolutions using Python. GeeksforGeeks. Recuperado el 20 de marzo de 2025 de https://www.geeksforgeeks.org/introduction-to-convolutions-using-python/
- GeeksforGeeks. (2024d, 24 abril). Python - How to Check if a file or directory exists. GeeksforGeeks. Recuperado el 20 de marzo de 2025 de https://www.geeksforgeeks.org/python-check-if-a-file-or-directory-exists/
- GeeksforGeeks. (2024e, 2 agosto). Python OpenCV | cv2.imread() method. GeeksforGeeks. Recuperado el 20 de marzo de 2025 de https://www.geeksforgeeks.org/python-opencv-cv2-imread-method/
- GeeksforGeeks. (2024f, 25 noviembre). How to display multiple images in one figure correctly in Matplotlib? GeeksforGeeks. Recuperado el 20 de marzo de 2025 de https://www.geeksforgeeks.org/how-to-display-multiple-images-in-one-figure-correctly-in-matplotlib/
- GeeksforGeeks. (2025g, 24 enero). Numpy.zeros() in Python. GeeksforGeeks. Recuperado el 20 de marzo de 2025 de https://www.geeksforgeeks.org/numpy-zeros-python/
- 8.2 Matriz de convolución. (s. f.). GIMP. https://docs.gimp.org/2.6/es/plug-in-convmatrix.html
- Olvera, B. (s. f.). Convolución [Diapositivas; Digital]. Tecnológico de Monterrey. https://experiencia21.tec.mx/courses/554652/discussion_topics/3503409
- Olvera, B. (s. f.). Procesamiento de Imágenes y Visión Computacional [Diapositivas; Digital]. Tecnológico de Monterrey. https://experiencia21.tec.mx/courses/554652/discussion_topics/3503409

Basado en los siguientes códigos:

- "convolution.py" por Abhisek Jana. Recuperado de https://github.com/benjaminva/semena-tec-tools-vision/tree/master/Scripts/Ejemplos
- "simple_conv.py" por Abhisek Jana y Benajmin Valdes. Recuperado de https://github.com/benjaminva/semena-tec-tools-vision/tree/master/Scripts/Ejemplos
- "simple_sobel.py" por Abhisek Jana y Benajmin Valdes. Recuperado de https://github.com/benjaminva/semena-tec-tools-vision/tree/master/Scripts/Ejemplos
"""
