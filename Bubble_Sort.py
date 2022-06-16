from time import perf_counter

lista = [48,29,36,35,58,1,12,7,90,88]

def bubble_sort(lista):
    for j in range(len(lista)):
        for i in range(len(lista)-1):
            if lista[i] < lista[i+1]:
                continue
            else:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    print(lista) 

      
start = perf_counter()
bubble_sort(lista)
end = perf_counter()
print(end-start) 