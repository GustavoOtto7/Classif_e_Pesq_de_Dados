import random

def new_lista_ordenada(size=100):
    size = int (input("Digite o tamanho da lista ordenada desejado: "))
    lista = []
    for x in range(1, size + 1):
        lista.append(x)
    return lista

def new_lista_invertida(size=100):
    size = int (input("Digite o tamanho da lista invertida desejado: "))
    lista = []
    for x in range(1, size + 1):
        lista.append(x)
    lista.reverse()
    return lista

def new_lista_random(size=100):
    lista = []
    size = int (input("Digite o tamanho da lista random desejado: "))
    for x in range(size):
        while True:
            num = random.randint(1, size)
            if num not in lista:
                lista.append(num)
                break
    return lista

def new_lista_repeat(size=100):
    lista = []
    size = int (input("Digite o tamanho da lista repetida desejado: "))
    for x in range(1, size + 1):
        lista.append(random.randint(1, size))
    return lista