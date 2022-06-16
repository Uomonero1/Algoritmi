from time import perf_counter
import numpy as np

lista = np.random.randint(0, 1000, size=1000, dtype=int)

def bubble_sort(lista):
    for _ in range(len(lista)):
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