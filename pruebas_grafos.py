# vertices = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6']
# n = len(vertices)

# matriz_adyacencia = [[0] * n for _ in range(n)]


# indice = {v: i for i, v in enumerate(vertices)}
# print(indice)

# conexiones = [
#     ('V1', 'V2'), ('V1', 'V3'), ('V2', 'V3'), ('V2', 'V5'),
#     ('V3', 'V4'), ('V4', 'V5'), ('V4', 'V6'), ('V5', 'V6')
# ]

# for v1, v2 in conexiones:
#     i, j = indice[v1], indice[v2]
#     matriz_adyacencia[i][j] = 1

# print("\nMatriz de adyacencia:")    
# print("    ", " ".join(f"{v:2}" for v in vertices))
# for i, fila in enumerate(matriz_adyacencia):
#     print(f"{vertices[i]:2}: ", " ".join(f"{x:2}" for x in fila))
    
# # Crear matriz de pesos (-1 = no hay arista, valor = peso de la arista)
# matriz_pesos = [[-1] * n for _ in range(n)]

# # Definir las aristas con sus pesos
# aristas_con_pesos = [
#     ('V1', 'V2', 3), ('V1', 'V3', 4), ('V2', 'V3', 8), ('V2', 'V5', 5),
#     ('V3', 'V4', 3), ('V4', 'V5', 7), ('V4', 'V6', 2), ('V5', 'V6', 3)
# ]

# for v1, v2, peso in aristas_con_pesos:
#     i, j = indice[v1], indice[v2]
#     matriz_pesos[i][j] = peso
    

# def mostrar_matriz_pesos(matriz, vertices):
#     print("\nMatriz de Pesos:")
#     print("    ", " ".join(f"{v:2}" for v in vertices))
#     for i, fila in enumerate(matriz):
#         print(f"{vertices[i]:2}: ", " ".join(f"{x:2}" for x in fila))

# mostrar_matriz_pesos(matriz_pesos, vertices)

vertices_red = ['R1', 'R2', 'R3', 'R4', 'R5']

conexiones_red = [
    ('R1', 'R2', 6),
    ('R1', 'R3', 3),
    ('R2', 'R3', 2),
    ('R2', 'R4', 5),
    ('R3', 'R4', 3),
    ('R3', 'R5', 8),
    ('R4', 'R5', 4)
]  # Red bidireccional

def construir_lista_adyacencia(vertices: list, conexiones):
    """
    Construya la lista de adyacencia de la red como un diccionario:
    {vertice: [(vecino, peso), ...]}
    La red es bidireccional: cada conexion debe agregarse en ambos sentidos.
    """
    grafo = {v: [] for v in vertices}

    for k, _ in grafo.items():
        for n1, n2, peso in conexiones:
            if k == n1:
                grafo[k].append((n2, peso))
            elif k == n2:
                grafo[k].append((n1, peso))
    return grafo

def construir_matriz_pesos(vertices, conexiones):
    """
    Construya la matriz de pesos V x V.
    Utilice -1 para indicar que no existe conexion directa entre dos vertices.
    """
    n = len(vertices)
    indices = {v: indx for indx, v in enumerate(vertices)}
    grafo_matriz = [[-1]*n for _ in range(n)]
    
    for n1, n2, peso in conexiones:
        grafo_matriz[indices[n1]][indices[n2]] = peso
        grafo_matriz[indices[n2]][indices[n1]] = peso
    return grafo_matriz

def matriz_a_lista(matriz, vertices):
    """
    A partir de la matriz de pesos, reconstruya la lista de adyacencia
    equivalente (mismo formato que 'construir_lista_adyacencia').
    """
    n = len(vertices)
    grafo = {v: [] for v in vertices}
    
    for fila in range(n):
        for columna in range(n):
            valor = matriz[fila][columna]
            if fila != columna and valor != -1:
                id_fila = vertices[fila]
                id_columna = vertices[columna]
                grafo[id_fila].append((id_columna, valor))

    return grafo

def dijkstra(grafo, inicio):
    """
    Implemente el algoritmo de Dijkstra desde cero.
    Retorna un diccionario {vertice: distancia_minima_desde_inicio}.
    """
    pass

Matriz_pesos = construir_matriz_pesos(vertices_red, conexiones_red)
print("\nMATRIZ DE PESOS")
for fila in Matriz_pesos:
    print(fila)
matriz_lista = matriz_a_lista(Matriz_pesos, vertices_red)
print("\nDE MATRIZ A LISTA")
for k, v in matriz_lista.items():
    print(k, v)