def fibMonaccianSearch(lista, x):
    n = len(lista)
    # inicializa fibonacci
    fibMMm2 = 0  # (m-2) Fibonacci 'th 
    fibMMm1 = 1  # (m-1) Fibonacci 'th  
    fibM = fibMMm2 + fibMMm1  # Fibonacci m'th 

    # fibM irá armazenar o menor número de Fibonacci maior ou igual a n
    #1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …
    while (fibM < n):
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1

    # Marca o intervalo eliminado pela frente
    offset = -1

    # Enquanto houver elementos a serem inspecionados.
    # Observe que comparamos lista[fibMm2] com x. 
    # Quando fibM se torna 1, fibMm2 se torna 0, então paramos, acabou
    while (fibM > 1):

        # Verifique se fibMm2 é um local válido
        i = min(offset+fibMMm2, n-1)

        # Se x for maior que o valor em
        # índice fibMm2, corta a matriz do subarray
        # a partir deslocamento de i
        if (lista[i] < x):
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i

        # Se x for menor que o valor em
        # índice fibMm2, corte o subarray
        # depois de i+1
        elif (lista[i] > x):
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1

        # Elemento encontrado, retorna indice
        else:
            return i

    # Comparando o ultimo elemento da lista com x */
    if(fibMMm1 and lista[n-1] == x):
        return n-1

    # Elemento não encontrado. return -1
    return -1

'''def main():
    lista = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100, 235]
    lista = [50, 58, 64, 74, 80, 85, 90, 99]
    x = 58
    ind = fibMonaccianSearch(lista, x)
    if ind>=0:
        print("Fibonacci - Elemento encontrado no índice: ",ind)
    else:
        print(x,"Não encontrado na lista")
main()'''