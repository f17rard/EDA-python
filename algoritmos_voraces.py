# Ejercicio del cambio
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


# Ejercicio de la mochila
def ProblemaMochila(Peso: int, valores: list, pesos: list):
    soluciones = [0.0*i for i in range(len(valores))]
    valor_peso = [valores[i]/pesos[i] for i in range(len(valores))]
    suma = 0
    indices = SeleccionVoraz(valor_peso)
    
    for i in indices:
        if suma + pesos[i] <= Peso and soluciones[i] == 0.0:
            suma += pesos[i]
            soluciones[i] = 1.0
        else:
            fraccion = (Peso-suma)/pesos[i]
            soluciones[i] = fraccion
            suma += pesos[i] * fraccion
            
        if suma == Peso:
            break
    
    return soluciones

def SeleccionVoraz(Valor_peso: list):
    usados = []
    while len(usados) < len(Valor_peso):
        valor_indice = -1
        valor_mayor = 0.0
        for i in range(len(Valor_peso)):
            if valor_mayor < Valor_peso[i] and i not in usados:
                valor_mayor = Valor_peso[i]
                valor_indice = i
        
        if valor_indice == -1:
            break
        
        usados.append(valor_indice)
    
    return usados


if __name__ == "__main__":
    pesos = [10, 20, 30, 40, 50]
    valores = [20, 30, 66, 40, 60]
            #   0,  1,  2,  3,  4
    solucion = ProblemaMochila(100, valores, pesos)
    casos=[
        (100,[20,30,66,40,60],[10,20,30,40,50]),
        (50,[20,10,10],[20,5,5]),
        (50,[20,30,30],[30,20,30]),
        (10,[1,2,3],[1,2,3])
        ]
    for c in casos:
        print(c, ProblemaMochila(*c))

# Ejercicio de los trabajadores
trabajadores = ["A","B","C","D"]
tareas = ["T1","T2","T3","T4"]
costos = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4],
]

def mejores_costos(Workers, Tasks, Costs:list):
    costos_minimos = []
    tareas_asignadas = []
    for i in range(len(Workers)):
        menor_tarea = float("inf")
        menor_indice = None
        for j in range(len(Tasks)):
            if menor_tarea > Costs[i][j] and Tasks[j] not in tareas_asignadas:
                menor_tarea = Costs[i][j]
                menor_indice = j
        tareas_asignadas.append(Tasks[menor_indice])
        costos_minimos.append((Workers[i],Tasks[menor_indice]))
        
    return costos_minimos

print(mejores_costos(trabajadores, tareas, costos))