# fibonacci en memorización

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

# fibonachi tabulacion

# def fibonacci_tab(n):
#     dp = {}
#     dp[0] = 0
#     dp[1] = 1
    
#     for i in range(2,n+1):
#         dp[i] = dp[i-2] + dp[i-1]
        
#     return dp[n]

# print(fibonacci_tab(3))
# print(fibonacci_tab(5))
# print(fibonacci_tab(6))

def Subsecuencia_mas_larga(lista: list):
    lenght = [1] * len(lista)
    
    for i in range(len(lista)):
        for k in range(i):
            if lista[k] < lista[i]:
                lenght[i] = max(lenght[i], lenght[k]+1)
        
    return max(lenght)


ejercicio = [6, 2, 5, 1, 7, 4, 8, 3]
print(Subsecuencia_mas_larga(ejercicio)) 
