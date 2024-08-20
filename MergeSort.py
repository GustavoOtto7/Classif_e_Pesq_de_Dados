def division_merge(lista):
    tam = len(lista) #10
    meio = tam/2 
    ini = 0
    fim = tam - 1
    p1 = ini
    p2 = meio + 1
    return lista, tam, p1, p2, fim

def merge_sort(lista, tam, p1, p2, fim):
    

    for i in range(0, i < tam):
        if lista[p1][0] > lista[p2][0]:
            

        if p1 != fim - 1 or p2 != fim - 1:    
            division_merge(lista)


        elif p1 == fim and p2 == fim:
            print("Fim das divisões! ")


    


def main():
    lista = [3, 9, 7, 2, 5, 10, 8, 1, 4, 6]
    tam, p1, p2, fim = division_merge(lista)
    merge_sort(lista, tam, p1, p2, fim)




main()