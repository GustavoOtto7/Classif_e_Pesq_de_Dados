import random

def heapfy(lista, n, i):
    menor = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n and lista[esquerda] < lista[menor]:
        menor = esquerda

    if direita < n and lista[direita] < lista[menor]:
        menor = direita

    if menor != i:
        lista[i], lista[menor] = lista[menor], lista[i]
        heapfy(lista, n, menor)

def heap_sort(lista):
    n = len(lista)

    for i in range(n // 2 - 1, -1, -1):
        heapfy(lista, n, i)

    for i in range(n-1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapfy(lista, i, 0)

def main():
    lista = random.sample(range(1, 101), 20)
    print("Lista original:", lista)
    heap_sort(lista)
    print("Lista ordenada:", lista)
main()