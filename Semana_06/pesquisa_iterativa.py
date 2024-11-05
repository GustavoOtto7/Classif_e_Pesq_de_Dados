def busca_binaria_iterativa(lista, item):
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == item:
            return meio 
        elif lista[meio] < item:
            esquerda = meio + 1  
        else:
            direita = meio - 1  
    return -1  

'''def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    resultado = busca_binaria_iterativa(lista, 6)
    print(f"Iterativa - Elemento encontrado no índice: {resultado}" if resultado != -1 else "Elemento não encontrado")
main()'''