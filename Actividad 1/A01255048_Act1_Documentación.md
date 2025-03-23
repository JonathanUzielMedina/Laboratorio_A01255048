<h1>Actividad 1: Implementación de Convolución</h1>
<h2>Características:</h2>
<ul>
  <li>Se desarrolló un algoritmo que aplica filtros de convolución a una imagen.</li>
  <li>El usuario debe ingresar el nombre y extensión de la imagen a procesar (ej.: imagen.jpg). Es muy recomendable que la imagen esté en el mismo directorio que el programa.</li>
  <li>Las entradas que se reciben son la imagen y la matriz del filtro.</li>
  <li>Los filtros que se manejan en este código son el de extensión de punto, suavizado 3x3, nitidez 3x3 y uno que yo mismo creé.</li>
  <li>Al final se muestran 4 versiones de la imagen, donde a cada una se le aplica un filtro.</li>
  <li><strong>IMPORTANTE:</strong> Es necesario tener las librerías: OpenCV, Matplotlib, OS y Numpy.</li>
</ul>

<h2>Función creada:</h2>
<strong>convolución():</strong> Esta función aplica un filtro de convolución a una imagen.
La precondición es que haya una matriz de imagen válida. Las entradas son las matrices de la imagen y del filtro de convolución.
La salida es la matriz de la imagen con el filtro aplicado. La postcondición es que la imagen tenga el filtro aplicado.
Su complejidad es O(n<sup>4</sup>) porque recorre n columnas de n filas de la matriz de la imagen y al recorrer las columnas se
recorren n columnas de n filas del filtro y del fragmento de la imagen a procesar.

<h2>Casos de Prueba:</h2>

<table>
  <thead>
    <th># Caso</th>
    <th>Nombre del Archivo</th>
    <th>Salida</th>
    <th>Propósito</th>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>minidv.jpg</td>
      <td><img src="https://github.com/user-attachments/assets/6d7b1f9d-9585-4a85-ac7c-3d2a09471a52" width="650"></td>
      <td>En este caso se demuestra cómo de utilizarse este programa correctamente.</td>
    </tr>
    <tr>
      <td>2</td>
      <td>fundas.jpg</td>
      <td><img src="https://github.com/user-attachments/assets/7525af06-3dbe-4abf-948b-e9c0fd8c1595" width="650"></td>
      <td>En este caso se demuestra que este programa funciona con cualquier otra imagen.</td>
    </tr>
    <tr>
      <td>3</td>
      <td>minidv</td>
      <td>No se pudo encontrar la imagen.</td>
      <td>En este caso se demuestra que es necesario ingresar la extensión del archivo de la imagen para poder encontrarla.</td>
    </tr>
    <tr>
      <td>4</td>
      <td>asdsdgdffd</td>
      <td>No se pudo encontrar la imagen.</td>
      <td>En este caso se demuestra que es necesario ingresar el nombre de una imagen que sí exista y esté en la misma carpeta.</td>
    </tr>
  </tbody>
</table>
