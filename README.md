# sd_lab1
Laboratorio 1 de la asignatura Sistemas Distribuidos. Desarrollado por Matías Barolo y Hernán Aravena.
## Requisitos:
	- Python 3.12.3
	- Microsoft MPI v10.1.3
	- NumPy 1.26.4
	- Tkinter 8.6

## Utilización:
	
	1. Instalar requisitos (Sección anterior)
	
	2. Para realizar la ejecución del programa debe ejecutarse el archivo main.py que corresponde a la capa
	de presentación. Posteriormente debe ingresarse el nombre del archivo de entrada incluyendo extensión y
	el número de hebras a utilizar (Arquitectura basada en eventos).
		2.1. Se incluye un script generador de archivos de entrada que por defecto genera un archivo llamado "e.txt"
		con 10.000 entradas con el nombre de la estación seguido y la temperatura correspondiente (entre 0 y 30 grados)
		según la estructura del archivo de entrada del enunciado. El nombre y el tamaño del archivo generado pueden
		ser cambiados pero debe hacerse mediante un editor de texto editando el script.
	
	3. Al presionar "Ejecutar arquitecturas" el programa procede con la ejecución de las tres arquitecturas implementadas
	(es posible que Windows detecte el proceso como "No responde" según el tamaño de la entrada que se le entregue) y al
	finalizar se levanta una ventana con los tiempos de ejecución correspondientes a cada arquitectura. Cada arquitectura
	además genera archivos de texto en donde entrega la solución encontrada. Estos archivos se encuentran separados por
	carpeta correspondiente a la arquitectura y cada uno de ellos se identifica con un timestamp de manera de que las
	soluciones sean almacenadas para posterior revisión.
	
	4. Posteriormente es posible ejecutar nuevamente las arquitecturas con otro archivo de entrada o bien distinto número
	de hebras.