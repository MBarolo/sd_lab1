import os
import time
import numpy as np
import datetime
import argparse

# Se define clase estacion para facilidad de manejo de los datos.
class Station:
    def __init__(self, name):
        self.name = name
        self.temps = []


# Encuentra una estación por nombre de una lista
def stationByName(stations, name):
    for s in stations:
        if s.name == name:
            return s
    return None

def readFile(filename):
    i = open(filename, 'r')
    lines = i.readlines()
    stations = []
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
    i.close()
    return stations

def main(filename):

    start_time = time.time()
    if not os.path.exists('./monolithic_out'):
        os.makedirs("monolithic_out")

    #stations = readFile(args.filename)
    stations = readFile(filename)
    o = open('./monolithic_out/[%s].txt' % (datetime.datetime.now().strftime("%Y-%m-%d %H.%M.%S")), 'w')

    # Se calcula lo requerido (min, max, mean)
    for s in stations:
        o.write(
            "Estación %s - Mínimo: %f - Máximo: %f - Media: %f\n" % (s.name, min(s.temps), max(s.temps), np.mean(s.temps)))
    o.close()

    return time.time() - start_time