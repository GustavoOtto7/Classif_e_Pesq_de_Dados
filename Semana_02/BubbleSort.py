def bubble_sort(lista):
    size = len(lista) - 1
    print("Lista antes: ", lista)
    for j in range(0, size):
        for i in range(0, size):
            if lista[i] > lista[i + 1]:
                '''aux = lista[i + 1]
                lista[i + 1] = lista[i]
                lista[i] = aux'''
                lista[i + 1], lista[i] = lista[i], lista[i + 1]
    print("Lista depois: ", lista)

def main():
    lista = [2, 7, 10, 4, 3, 5]
    bubble_sort(lista)
    lista_ordenada = [1, 2, 3, 4, 5, 6, 7]
    bubble_sort(lista_ordenada)
    lista_inversa = [7, 6, 5, 4, 3, 2, 1]
    bubble_sort(lista_inversa)
    lista_repetida = [2, 7, 10, 4, 3, 5, 2, 7, 10, 4, 3, 5]
    bubble_sort(lista_repetida)
main()