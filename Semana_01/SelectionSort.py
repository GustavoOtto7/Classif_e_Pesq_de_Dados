
def selection_sort(list):
    size = len(list)
    print("Lista antes: ", list)
    ini = 0
    contador = 0
    while contador < size:
        for num in range(ini, size):
            num_ini = list[ini]
            num_min = list[ini]
            if list[num] < list[ini]:
                list[ini] = list[num]
        list[ini] = num_min
        list[num] = num_ini    
        contador += 1 
    print("Lista depois: ", list)

def main():
    list = [23, 4, 67, -8, 90, 54, 21]
    selection_sort(list)
main()
