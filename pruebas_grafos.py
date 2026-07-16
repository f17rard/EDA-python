vertices = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6']
n = len(vertices)

matriz_adyacencia = [[0] * n for _ in range(n)]

print(matriz_adyacencia)

indice = {v: i for i, v in enumerate(vertices)}
print(indice)