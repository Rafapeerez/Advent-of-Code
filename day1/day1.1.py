fich = open("/home/rafa/ASL/AoC/day1/input.txt","r") #abrimos fichero modo lectura

sol=0 #variable de la solucion del problema
cont=0 #variable de lineas leidas
vector = [] #vector de los valores

for lines in fich: #leemos el fichero linea por linea
    value = int(lines) #como lo que estamos leyendo son strings, los pasamos a enteros
    vector.append(value) #pasamos los valores de cada linea al final del vector
    cont = cont + 1 #incrementamos el numero de lineas leidas

for n,moment in enumerate(vector): #con enumerate creamos el vector iterativo
    if(n > 2):
        add1 = vector[n-3] + vector[n-2] + vector[n-1] #suma de los 3 valores anteriores
        add2 = vector[n-2] + vector[n-1] + moment #suma de los 2 valores anteriores y el actual
        if(add1 < add2): 
            sol = sol + 1

print(f"Lines: {cont}")
print(f"Solution: {sol}")

fich.close()