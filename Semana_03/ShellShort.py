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
    lista = [18, 32, 12, 5, 38, 33, 16, 2]
    print("Lista before: ", lista)
    lista = shellsort(lista)
    print("This is the new ordened list: ", lista)
main()