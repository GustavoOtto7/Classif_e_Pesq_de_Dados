def shellsort(lista):
    size = len(lista)
    jump = size//2 
    while jump > 0:
        for inicio in range(jump):
            


    for i in range(0, size/2):
        if lista[i] > lista[i + jump]:
            lista[i + jump], lista[i] = lista[i], lista[i + jump]
        
    jump = jump // 2

def jump_insertion(lista, inicio, jump):
    for ind in range(inicio + jump, len(lista, jump)):
        valor_atual = lista[ind]
        while ind >= jump and lista[ind-jump] > valor_atual:


def main():
    lista = [18, 32, 12, 5, 38, 33, 16, 2]
    shellsort(lista)


main()