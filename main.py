from tkinter import *
from tkinter import ttk
import tkinter.font as font
from tkinter.messagebox import showinfo
import sys, os

import subprocess
import monolitico
import servicios


def inputExists(filename):
    if os.path.isfile("./" + filename):
        return True
    return False


def execution():
    filename = filename_entry.get()
    if not inputExists(filename):
        showinfo("Error", "Archivo de entrada no existe.")
    else:
        time_monolithic = monolitico.main(filename)
        time_services = servicios.main(filename)

        command_events = ['mpiexec', '-n', str(n.get()), 'python', './eventos.py', '-i', filename]

        result_events = subprocess.run(command_events, stdout=subprocess.PIPE)
        time_events = float(result_events.stdout.decode("utf-8"))
        showinfo("Ejecución completada", "Tiempos de ejecución:\n"
                                         "   - Arquitectura monolítica: %f [s]\n"
                                         "   - Arquitectura basada en servicios: %f [s]\n"
                                         "   - Arquitectura basada en eventos: %f [s] \n\n"
                                         "Los archivos de salida se encuentran en '%s' en las carpetas respectivas por "
                                         "arquitectura."
                 % (time_monolithic, time_services, time_events, os.path.abspath(os.path.dirname(sys.argv[0]))))


# Bloque principal
root = Tk()
root.geometry("")
root.title("Laboratorio 1 SD")
frm = ttk.Frame(root, padding=10)

# Labels
ttk.Label(root, text="Arquitecturas de Sistemas Distribuidos", padding=10, font=font.Font(size=10, weight='bold')) \
    .grid(row=1, columnspan=4)
ttk.Label(root, text="Ingrese el nombre de archivo de entrada [ejemplo.txt]: ", anchor="w", padding=10).grid(row=2,
                                                                                                             column=0,
                                                                                                             sticky=W)
ttk.Label(root, text="Ingrese el número de hebras (Arquitectura basada en eventos)", padding=10).grid(row=3, sticky=W)

# Entries
filename_entry = ttk.Entry(root)
n = ttk.Spinbox(root, from_=1, to=10, increment=1)

# Posición entries
filename_entry.grid(row=2, column=1, padx=5)
n.grid(row=3, column=1, padx=5)

# Botones
ttk.Button(root, text="Ejecutar arquitecturas", command=execution).grid(row=12, pady=5, columnspan=2)
ttk.Button(root, text="Salir", command=root.destroy).grid(row=13, columnspan=2, pady=5)
root.mainloop()
