import subprocess
import monolitico
import servicios

# Bloque principal

# parametrizar según interfaz
filename = "entrada.txt"
n = 4

monolitico.main(filename)

command_events = ['mpiexec', '-n', str(n), 'python', './eventos.py', '-i', filename]
result_events = subprocess.run(command_events, stdout=subprocess.PIPE)

servicios.main(filename)
