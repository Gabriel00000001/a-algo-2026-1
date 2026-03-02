import random
import time


def insertion_sort(n):
    i = 1

    while i < len(n):
        valor_atual = n[i]
        trocou = False
        j = i - 1

        while j >= 0 and n[j] > valor_atual:
            n[j + 1] = n[j]
            trocou = True
            j -= 1
        
        if trocou:
            n[j + 1] = valor_atual
        
        i += 1
    


tamanho = [1000, 5000, 10000, 20000, 50000]

for i in range(len(tamanho)):
    lista = list(range(tamanho[i]))
    random.shuffle(lista)

    tempo_antes_insertion = time.time()
    insertion_sort(lista)
    tempo_depois_insertion= time.time()
    total_insertion = (tempo_depois_insertion - tempo_antes_insertion)

    tempo_antes_sorted = time.time()
    sorted(lista)
    tempo_depois_sorted = time.time()
    total_sorted = (tempo_depois_sorted - tempo_antes_sorted)


    print(f"Tempo de execução do insertion de uma lista de tamanho {len(lista)}:{total_insertion} segundos")
    print(f"Tempo de execução do sorted de uma lista de tamanho {len(lista)}:{total_sorted} segundos") 
