# Auxiliar 0

**El colab asociado a esta aux se puede visitar [aca](https://colab.research.google.com/drive/12NA8gGzXe-MU8pm6XO_4T-f3e-3YJGyw)**


En esta auxiliar voy a introducir herramientas y flujos de trabajo basicos para que tod@s puedan tener un comienzo mas fluido en el curso y ojala lo menos frustrante posible.

Esta auxiliar esta orientada a personas con conocimientos basico o nulos sobre entornos de trabajo de python, asique es probable que a usuarios mas experimentados no les sea de mayor utilidad.


Primero voy a ver colab y aprovechar de explicar algunas de las herramientas que van a tener que usar en la minitarea 1.


# Google Colab
Es un entorno que permite escribir y ejecutar python en un web browser.

* Esencialmente un jupyter notebook
* Formato basado en celdas -> texto y codigo
* Acepta texto en formato markdown + algunos manjares extra
* Es posible ejecutar comando de shell con `!` antepuesto al comando

* Viene con todo instalado
* No requiere configuracion
* Da acceso a GPUs
* Completamente multiplataforma 

* Se puede conectar a fuentes de datos externas
* Con esto se pueden descargar datasets y extraerlos desde el notebook



# Numpy
* Libreria para realizar computacion matematica
* Tiene sintaxis similar a matlab
* Clase principal: ndarray
* Permite realizar operaciones matematicas entre vectores con sintaxis simple y concisa
* Calculo punto a punto es el default
* Incluye tambien muchas funciones de calculo y algebra lineal.


# Pandas
* Libreria para analisis y manejo de datos
* Tiene una api gigante
* Buena documentacion
* DataFrame es la clase principal, datos tabulares
* Soporta una gran cantidad de operaciones tipo SQL


# Datos
* Se puede conectar con Drive, se monta en el directorio local y se tiene acceso a todo el drive
* Tambien se pueden descargar datos usando la linea de comando


# Anaconda
* Version autocontenida de python + gestor de paquetes
* Para instalar seguir las instrucciones en https://docs.anaconda.com/anaconda/install/

* Tipear `anaconda-navigator` en una terminal. Interfaz grafica para facilitar acceso a los programas que se instalaron

* Tambien se puede usar desde la terminal
* Python default pasa a ser el que se instalo con anaconda, todos los programas viven en $HOME/anaconda3

* Muy simple de instalar, viene con todos los paquetes necesarios para hacer analisis ded datos
* Algunos paquetes nos estan disponibles


# Python puro + pip

* Considerablemente mas latero que las otras opciones
* Da mas control
* No requiere de otros programas, solo los que vienen preinstalados en el sistema (es posible que se tenga que instalar pip)
* Opcion "default" de python
* Acceso a todos los paquetes de python



# Demos

* Mostrar como ejecutar el notebook creado en colab en los otros dos "entornos"

