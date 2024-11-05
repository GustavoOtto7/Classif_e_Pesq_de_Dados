def pesqBin(lista, chave):
    esq = 0
    dir = len(lista) - 1
    
    while esq <= dir:
        #meio = (dir + esq) // 2
        meio = esq + ((dir - esq) * (chave - lista[esq])) // (lista[dir] - lista[esq])
        if lista[meio] == chave:
            return meio
        elif lista[meio] > chave:
            dir = meio - 1
        elif lista[meio] < chave:
            esq = meio + 1

'''def main():
    lista = [1, 10, 12, 14, 16, 18, 20]
    chave = 20
    ind = pesqBin(lista, chave)
    print("Interpolation - Elemento encontrado no índice: ", ind)
main()'''