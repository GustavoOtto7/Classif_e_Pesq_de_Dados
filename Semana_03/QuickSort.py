def division(lista):
    print("Lista 1: ", lista)
    pivo = lista[0]
    size = len(lista)
    esq = 1
    dir = size - 1
    while esq <= dir:
        while esq <= dir and lista[esq] <= pivo:
            esq += 1
        while esq <= dir and lista[dir] > pivo:
            dir -= 1
        if esq < dir:
            lista[esq], lista[dir] = lista[dir], lista[esq]
            print("Lista 2: ", lista)
    lista[dir], lista[0] = lista[0], lista[dir]
    print("Lista 3: ", lista) 
    return dir

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivo_ind = division(lista)
    left = quicksort(lista[:pivo_ind])
    right = quicksort(lista[pivo_ind+1:])
    return left + [lista[pivo_ind]] + right

def main():
    lista = [18, 32, 12, 5, 38, 33, 16, 2]
    lista = quicksort(lista)
    print("Lista final: ", lista)
main()