"""# fibonacci en memorización

cache = {}
def fibonacci_memo(n, cache = None):
    
    if n <= 1:
        return n
    
    if cache == None:
        cache = {}
        
    if n in cache:
        return cache[n]
        
    cache[n] = fibonacci_memo(n-1,cache) + fibonacci_memo(n-2,cache)
    
    return cache[n]

print(fibonacci_memo(6, cache))
print(fibonacci_memo(7, cache))
"""

"""# fibonachi tabulacion
def fibonacci_tab(n):
    dp = {}
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2,n+1):
        dp[i] = dp[i-2] + dp[i-1]
        
    return dp[n]

print(fibonacci_tab(3))
print(fibonacci_tab(5))
print(fibonacci_tab(6))
"""

"""# Secuencia más larga
def Subsecuencia_mas_larga(lista: list):
    lenght = [1] * len(lista)
    
    for i in range(len(lista)):
        for k in range(i):
            if lista[k] < lista[i]:
                lenght[i] = max(lenght[i], lenght[k]+1)
        
    return max(lenght)


ejercicio = [6, 2, 5, 1, 7, 4, 8, 3]
print(Subsecuencia_mas_larga(ejercicio)) 
"""

# caminos en cuadricula

def max_path_sum(cuadricula):
    n  = len(cuadricula)
    paths = [[0]*(n+1) for _ in range(n+1)]
    
    for f in range(1, n+1): # f = 1 cuadricula[1][iteraciones de c] y asi sucesivamente
        for c in range(1, n+1): 
            paths[f][c] = max(paths[f][c-1], paths[f-1][c]) + cuadricula[f-1][c-1]
            
    
    return paths

cuadri =[
    [3, 7, 9, 2, 7],
    [9, 8, 3, 5, 5],
    [1, 7, 9, 8, 5],
    [3, 8, 6, 4, 10],
    [6, 3, 9, 7, 8]
]
# cuadri = [
#     [4, 10, 15, 12],
#     [12, 11, 14, 12],
#     [10, 7, 5, 9],
#     [10, 14, 20, 30]
# ]
cuadri_cero = max_path_sum(cuadri)
n = len(cuadri)
secuencias = [[0]*(n) for _ in range(len(cuadri))]
f, c = 1, 1
secuencias[0][0] = 1

while f < n:
    abajo = cuadri_cero[f+1][c] if f+1 < n+1 else -1
    derecha = cuadri_cero[f][c+1] if c+1 < n+1 else -1
    if abajo > derecha:
        f += 1
        secuencias[f-1][c-1] = 1
    else:
        c += 1
        secuencias[f-1][c-1] = 1

for sec in secuencias:
    print(sec)

