def division_merge(lista):
    tam = len(lista) #10
    meio = tam/2 
    ini = 0
    fim = tam - 1
    p1 = ini
    p2 = meio + 1
    return lista, tam, p1, p2, fim

def merge_sort(lista, inicio, fim):
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
        if top_right >= len(right):
            lista[k] = left[top_left]
            top_left += 1
        if left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left += 1
        else:
            lista[k] = right[top_right]
            top_right += 1


        if p1 != fim or p2 != fim:    
            division_merge(lista)

        elif p1 == fim and p2 == fim:
            print("Fim das divisões! ")
            for top_left in range(0, top_left < tam):
                if lista[p1][0] > lista[p2][0]:


def main():
    lista = [3, 9, 7, 2, 5, 10, 8, 1, 4, 6]
    tam, p1, p2, fim = division_merge(lista)
    merge_sort(lista, tam, p1, p2, fim)

main()