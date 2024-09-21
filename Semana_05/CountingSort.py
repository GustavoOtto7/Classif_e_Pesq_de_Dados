import random

def counting_sort(lista):
    size = max(lista) + 1
    lista_repeat = [0] * size
    for num in lista:
        lista_repeat[num] += 1
    return lista_repeat

def count_sorting(lista_repeat):
    lista_final = []
    for i in range(len(lista_repeat)):
        while lista_repeat[i] > 0:
            lista_final.append(i)
            lista_repeat[i] -= 1
    return lista_final

def main():
    lista = [random.randint(0, 10) for _ in range(20)]
    print("Lista antes: ", lista)
    lista_repeat = counting_sort(lista)
    print("Lista repetições: ", lista_repeat)
    lista_final = count_sorting(lista_repeat)
    print("Lista final: ", lista_final)
main()