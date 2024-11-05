import math

def jump_search(lista, item):
    n = len(lista)
    m = int(math.sqrt(n))
    i = 0
    
    while i < n and lista[min(i + m, n) - 1] < item:
        i += m
    
    for j in range(i, min(i + m, n)):
        if lista[j] == item:
            return j  

    return -1 

'''def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    resultado = jump_search(lista, 6)
    if resultado != -1:
        print(f"Jump Search - Elemento encontrado no índice: {resultado}")
    else:
        print("Elemento não encontrado")
main()
'''