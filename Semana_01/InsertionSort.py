def insertion(list):
    size = len(list)
    print("Lista antes: ", list)
    for atual in range(1, size):
        ant = atual - 1
        dado_temp = list[atual]
        while ant >= 0 and dado_temp < list[ant]:
            list[ant + 1] = list[ant]
            ant -= 1
        list[ant + 1] = dado_temp
    print("Lista depois: ", list)   

def main():
    list_ord = [1, 2, 3, 4, 5]
    list_inv = [5, 4, 3, 2, 1]
    list_dup = [1, 3, 2, 1, 4, 3, 2]
    list_rand = [2, 5, 1, 6, 4]
    insertion(list_ord)
    insertion(list_inv)
    insertion(list_dup)
    insertion(list_rand)
main()