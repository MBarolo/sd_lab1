import time
import numpy as np
#Se define clase estacion para facilidad de manejo de los datos.
class Station:
    def __init__(self, name):
        self.name = name
        self.temps = []

#Encuentra una estación por nombre de una lista
def stationByName(stations, name):
    for s in stations:
        if s.name == name:
            return s
    return None


start_time = time.time()
i = open('entrada.txt', 'r')
o = open('salida.txt', 'w')
lines = i.readlines()
stations = []

#Se lee el archivo de entrada
for l in lines:
    name, temp = l.split(';')
    temp = float(temp)
    station = stationByName(stations, name)
    if station == None:
        station = Station(name)
        station.temps.append(temp)
        stations.append(station)
    else:
        station.temps.append(temp)

#Se calcula lo requerido (min, max, mean)
for s in stations:
    o.write("Estación %s - Mínimo: %f - Máximo: %f - Media: %f\n" %(s.name, min(s.temps), max(s.temps),  np.mean(s.temps)))

i.close()
o.close()
print("Tiempo de ejecución: %s [s]" %(time.time() - start_time))