def busca_binaria_recursiva(lista, item, esquerda, direita):
    if esquerda > direita:
        return -1 
    meio = (esquerda + direita) // 2  
    if lista[meio] == item:
        return meio  
    elif lista[meio] < item:
        return busca_binaria_recursiva(lista, item, meio + 1, direita)  
    else:
        return busca_binaria_recursiva(lista, item, esquerda, meio - 1)  

'''def main():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    resultado = busca_binaria_recursiva(lista, 6, 0, len(lista) - 1)
    print(f"Recursiva - Elemento encontrado no índice: {resultado}" if resultado != -1 else "Elemento não encontrado")
main()'''