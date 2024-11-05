import random
import timeit
from pesquisa_iterativa import busca_binaria_iterativa
from pesquisa_recursiva import busca_binaria_recursiva
from jump_search import jump_search
from fibonacci import fibMonaccianSearch
from interpolation import pesqBin

def gerar_lista_ordenada(tamanho):
    return list(range(tamanho))

def testar_algoritmos(lista, item):
    resultados = {}
    tempo_iterativo = timeit.timeit(lambda: busca_binaria_iterativa(lista, item), number=1)
    resultados['Iterativa'] = tempo_iterativo

    tempo_recursiva = timeit.timeit(lambda: busca_binaria_recursiva(lista, item, 0, len(lista) - 1), number=1)
    resultados['Recursiva'] = tempo_recursiva

    tempo_salto = timeit.timeit(lambda: jump_search(lista, item), number=1)
    resultados['Salto'] = tempo_salto

    tempo_fibonacci = timeit.timeit(lambda: fibMonaccianSearch(lista, item), number=1)
    resultados['Fibonacci'] = tempo_fibonacci

    tempo_interpolar = timeit.timeit(lambda: pesqBin(lista, item))
    resultados['Interpolar'] = tempo_interpolar

    return resultados

def main():
    lista = gerar_lista_ordenada(10000)
    item = random.choice(lista)
    print("Número escolhido: ", item)
    resultados = testar_algoritmos(lista, item)
    for metodo, tempo in resultados.items():
        print(f"{metodo}: {tempo:.6f} segundos")
main()