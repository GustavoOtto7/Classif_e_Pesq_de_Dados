def division(lista):
    print("Lista 1: ", lista)
    pivo = lista[0]
    size = len(lista)
    esq = 1
    dir = size - 1
    while dir > esq:
        while pivo >= lista[esq]:
            esq += 1
        while pivo <= lista[dir]:
            dir -= 1
        if lista[esq] < lista[dir]:
            lista[esq], lista[dir] = lista[dir], lista[esq]
            print("Lista 2: ", lista)
            break
    lista[dir], pivo = pivo, lista[dir]
    print("Lista 3: ", lista)
    if size > 3:
        division(lista <= pivo)
        division(lista > pivo)
    else: 
        return lista

def main():
    lista = [18, 32, 12, 5, 38, 33, 16, 2]
    lista = division(lista)
    print("Lista final: ", lista)
main()