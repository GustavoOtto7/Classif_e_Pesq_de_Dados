
def selection_sort(list):
    size = len(list)
    print("Lista antes: ", list)
    for i in range(size):
        min_ind = i
        for j in range(i + 1, size):
            if list[j] < list[min_ind]:
                min_ind = j
        list[i], list[min_ind] = list[min_ind], list[i] 
    print("Lista depois: ", list)

def main():
    list = [23, 4, 67, -8, 90, 54, 21]
    selection_sort(list)
main()
