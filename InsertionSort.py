def insertion(list, size):
    for atual in range(1, size):
        ant = atual - 1
        dado_temp = list[atual]
        while ant >= 0 and dado_temp < list[ant]:
            list[ant], list[atual] = list[atual], list[ant]
            atual += 1
            return list       

def main():
    list = [2, 5, 1, 6, 4]
    size = len(list)
    print("Lista antes: ", list)
    list = insertion(list, size)
    print("Lista depois: ", list)
main()