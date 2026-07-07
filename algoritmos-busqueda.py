listA = [ -8, 2, 4, 6, 8, 12, 19, 23, 40] #lista para busqueda binaria
listB = [1, 5, 2, 40, 7, 8, 9, 6, 35, 12, 20] #lista para busqueda lineal

def secuencial_desordenado(lista, length, numero):
    i = 0
    while i < length and lista[i] != numero:
        i += 1
    if i == length: #si fuera ordenado se podria comparar el indice actual con el valor si es mayor
        print("Valor no encontrado")
    else:
        print(f"El valor se encuentra en el indice: {i}")


def binario_ordenado(lista, Cmin, Cmax, numero): 
    medio = round((Cmin + Cmax) / 2)
    
    if Cmin>Cmax:
        print("El valor no se encuentra en la lista")
        return
    elif lista[medio] == numero:
        print(f"El número {numero} se encuentra en el indice {medio}")
        return
    
    
    if lista[medio] < numero:
        binario_ordenado(lista, medio+1, Cmax, numero)
    elif lista[medio] > numero:
        binario_ordenado(lista, Cmin, medio-1, numero)
    
    
    
secuencial_desordenado(listB, len(listB), 14)

binario_ordenado(listA, 0, len(listA)-1, 40)