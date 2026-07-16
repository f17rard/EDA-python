"""Ejercicio del cambio
denominaciones = [100, 20, 10, 5, 1]

montos = [47, 83, 156, 1, 3]

for monto in montos:
    restante = monto
    num_billetes = [0, 0, 0, 0, 0]
    for i in range(len(denominaciones)):
        while restante>=denominaciones[i]:
            restante -= denominaciones[i]
            num_billetes[i] += 1
            
    print(num_billetes)

""" 

"""Ejercicio de la mochila"""
