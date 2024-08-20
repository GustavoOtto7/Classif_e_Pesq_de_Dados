def merge_sort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if (fim - inicio) > 1:
        meio = (fim + inicio)//2 
        merge_sort(lista, inicio, meio)
        merge_sort(lista, meio, fim)
        merge(lista, inicio, meio, fim)

def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0
    for k in range(inicio, fim):
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right += 1
        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left += 1
        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left += 1
        else:
            lista[k] = right[top_right]
            top_right += 1

def main():
    lista = [3, 9, 7, 2, 5, 10, 8, 1, 4, 6]
    print("Lista antes: ", lista)
    merge_sort(lista)
    print("Lista depois: ", lista)

    lista_ordenada = [1, 2, 3, 4, 5, 6, 7]
    print("Lista antes: ", lista_ordenada)
    merge_sort(lista_ordenada)
    print("Lista depois: ", lista_ordenada)

    lista_inversa = [7, 6, 5, 4, 3, 2, 1]
    print("Lista antes: ", lista_inversa)
    merge_sort(lista_inversa)
    print("Lista depois: ", lista_inversa)

    lista_repetida = [2, 7, 10, 4, 3, 5, 2, 7, 10, 4, 3, 5]
    print("Lista antes: ", lista_repetida)
    merge_sort(lista_repetida)
    print("Lista depois: ", lista_repetida)
main()