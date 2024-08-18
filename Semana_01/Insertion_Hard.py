class Lista:
    def __init__(self, info=None):
        self.info = info  
        self.prox = None  

def insere(lista, info):
    novo_no = Lista(info)
    if not lista:
        return novo_no
    last_node = lista
    while last_node.prox:
        last_node = last_node.prox
    last_node.prox = novo_no
    return lista

def insertion_sort(lista):
    if not lista or not lista.prox:
        return lista
    lista_ordenada = None
    atual = lista
    while atual:
        prox_no = atual.prox
        lista_ordenada = insere_ordenado(lista_ordenada, atual)
        atual = prox_no
    return lista_ordenada

def insere_ordenado(lista_ordenada, novo_no):
    if not lista_ordenada or lista_ordenada.info >= novo_no.info:
        novo_no.prox = lista_ordenada
        lista_ordenada = novo_no
    else:
        atual = lista_ordenada
        while atual.prox and atual.prox.info < novo_no.info:
            atual = atual.prox
        novo_no.prox = atual.prox
        atual.prox = novo_no
    return lista_ordenada

def lista_imprime(lista):
    atual = lista
    while atual:
        print(atual.info, end=" -> ")
        atual = atual.prox
    print("None")

def main():
    lista = None
    for item in [2, 5, 1, 6, 4]:
        lista = insere(lista, item)
    print("Lista original:")
    lista_imprime(lista)
    lista = insertion_sort(lista)
    print("Lista após ordenação:")
    lista_imprime(lista)
main()