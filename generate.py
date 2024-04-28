import random

newInput = open("e_10k.txt", "w")
stations = ["Hamburg", "Bulawayo", "Palembang", "St. John's", "Cracow", "Bridgetown", "Istanbul", "Conakry", "Roseau"]
size = 9999
for i in range(size):
    s = random.randint(0, 8)
    t = random.uniform(0.0, 30.0)
    newInput.write(stations[s] + ";" + str(round(t, 1)) + '\n')

newInput.close()
