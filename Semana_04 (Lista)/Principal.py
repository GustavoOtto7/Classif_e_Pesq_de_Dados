import GeradorLista
import timeit

def medir_tempo(funcao, lista):
    tempo = timeit.timeit(lambda: funcao(lista.copy()))
    return tempo

def insertion_sort(list):
    size = len(list)
    for atual in range(1, size):
        ant = atual - 1
        dado_temp = list[atual]
        while ant >= 0 and dado_temp < list[ant]:
            list[ant + 1] = list[ant]
            ant -= 1
        list[ant + 1] = dado_temp

def selection_sort(list):
    size = len(list)
    for i in range(size):
        min_ind = i
        for j in range(i + 1, size):
            if list[j] < list[min_ind]:
                min_ind = j
        list[i], list[min_ind] = list[min_ind], list[i] 

def bubble_sort(lista):
    size = len(lista) - 1
    for j in range(0, size):
        for i in range(0, size):
            if lista[i] > lista[i + 1]:
                lista[i + 1], lista[i] = lista[i], lista[i + 1]

def merge_sort(lista):
    def merge_sort1(lista, inicio=0, fim=None):
        if fim is None:
            fim = len(lista)
        if (fim - inicio) > 1:
            meio = (fim + inicio)//2 
            merge_sort1(lista, inicio, meio)
            merge_sort1(lista, meio, fim)
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

def quick_sort(lista):
    def division(lista):
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
        lista[dir], lista[0] = lista[0], lista[dir]
        return dir

    def quicksort(lista):
        if len(lista) <= 1:
            return lista
        pivo_ind = division(lista)
        left = quicksort(lista[:pivo_ind])
        right = quicksort(lista[pivo_ind+1:])
        return left + [lista[pivo_ind]] + right

def shell_sort(lista):
    def shellsort(lista):
        size = len(lista)
        jump = size//2 
        while jump > 0:
            for i in range(jump, size):
                jump_insertion(lista, i, jump)
            jump = jump // 2
        return lista

    def jump_insertion(lista, inicio, jump):
        current_value = lista[inicio]
        position = inicio
        while position >= jump and lista[position - jump] > current_value:
            lista[position] = lista[position - jump]
            position -= jump
        lista[position] = current_value

def main():
    lista_ordenada = GeradorLista.new_lista_ordenada()
    lista_inversa = GeradorLista.new_lista_invertida()
    lista_random = GeradorLista.new_lista_random()
    lista_repetidos = GeradorLista.new_lista_repeat()

    print("----- INSERTION  SORT -----")
    tempo1 = medir_tempo(insertion_sort, lista_ordenada)
    tempo2 = medir_tempo(insertion_sort, lista_inversa)
    tempo3 = medir_tempo(insertion_sort, lista_random)
    tempo4 = medir_tempo(insertion_sort, lista_repetidos)
    print(f"Tempo para ordenar a lista ordenada: {tempo1} segundos")
    print(f"Tempo para ordenar a lista inversa: {tempo2} segundos")
    print(f"Tempo para ordenar a lista randômica: {tempo3} segundos")
    print(f"Tempo para ordenar a lista com repetidos: {tempo4} segundos")

    print("----- SELECTION  SORT -----")
    tempo1 = medir_tempo(selection_sort, lista_ordenada)
    tempo2 = medir_tempo(selection_sort, lista_inversa)
    tempo3 = medir_tempo(selection_sort, lista_random)
    tempo4 = medir_tempo(selection_sort, lista_repetidos)
    print(f"Tempo para ordenar a lista ordenada: {tempo1} segundos")
    print(f"Tempo para ordenar a lista inversa: {tempo2} segundos")
    print(f"Tempo para ordenar a lista randômica: {tempo3} segundos")
    print(f"Tempo para ordenar a lista com repetidos: {tempo4} segundos")

    print("----- BUBBLE  SORT -----")
    tempo1 = medir_tempo(bubble_sort, lista_ordenada)
    tempo2 = medir_tempo(bubble_sort, lista_inversa)
    tempo3 = medir_tempo(bubble_sort, lista_random)
    tempo4 = medir_tempo(bubble_sort, lista_repetidos)
    print(f"Tempo para ordenar a lista ordenada: {tempo1} segundos")
    print(f"Tempo para ordenar a lista inversa: {tempo2} segundos")
    print(f"Tempo para ordenar a lista randômica: {tempo3} segundos")
    print(f"Tempo para ordenar a lista com repetidos: {tempo4} segundos")

    print("----- MERGE  SORT -----")
    tempo1 = medir_tempo(merge_sort, lista_ordenada)
    tempo2 = medir_tempo(merge_sort, lista_inversa)
    tempo3 = medir_tempo(merge_sort, lista_random)
    tempo4 = medir_tempo(merge_sort, lista_repetidos)
    print(f"Tempo para ordenar a lista ordenada: {tempo1} segundos")
    print(f"Tempo para ordenar a lista inversa: {tempo2} segundos")
    print(f"Tempo para ordenar a lista randômica: {tempo3} segundos")
    print(f"Tempo para ordenar a lista com repetidos: {tempo4} segundos")

    print("----- QUICK  SORT -----")
    tempo1 = medir_tempo(quick_sort, lista_ordenada)
    tempo2 = medir_tempo(quick_sort, lista_inversa)
    tempo3 = medir_tempo(quick_sort, lista_random)
    tempo4 = medir_tempo(quick_sort, lista_repetidos)
    print(f"Tempo para ordenar a lista ordenada: {tempo1} segundos")
    print(f"Tempo para ordenar a lista inversa: {tempo2} segundos")
    print(f"Tempo para ordenar a lista randômica: {tempo3} segundos")
    print(f"Tempo para ordenar a lista com repetidos: {tempo4} segundos")

    print("----- SHELL  SORT -----")
    tempo1 = medir_tempo(shell_sort, lista_ordenada)
    tempo2 = medir_tempo(shell_sort, lista_inversa)
    tempo3 = medir_tempo(shell_sort, lista_random)
    tempo4 = medir_tempo(shell_sort, lista_repetidos)
    print(f"Tempo para ordenar a lista ordenada: {tempo1} segundos")
    print(f"Tempo para ordenar a lista inversa: {tempo2} segundos")
    print(f"Tempo para ordenar a lista randômica: {tempo3} segundos")
    print(f"Tempo para ordenar a lista com repetidos: {tempo4} segundos")

main()