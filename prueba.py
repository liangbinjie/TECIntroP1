a = open('resultados.txt', "r")
linea = a.readline().strip().split(";")
for i in range(len(linea)):
    linea[i] = int(linea[i])

linea[0] = linea[0] + 1

o = ""
for i in linea:
    o += ";"+str(i)

r = open("resultados.txt", "w")
r.write(o[1::])
r.close()