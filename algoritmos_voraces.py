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
def ProblemaMochila(Peso, valores, pesos):
    valor_peso = []
    soluciones = [0.0*n for n in range(len(valores))]
    for i in range(len(valores)):
        valor_peso.append(valores[i]/pesos[i])
        max = valor_peso[0]
    
    for i in range(1, len(valor_peso)):
        if max < valor_peso[i]:
            max = valor_peso[i]
        
    print(max)
    
    
pesos = [10, 20, 30, 40, 50]
valores = [20, 30, 66, 40, 60]
ProblemaMochila(100, valores, pesos)