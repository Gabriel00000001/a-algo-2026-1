import random
import time

#função que recebe um lista de numeros inteiros para ordenar
def insertion_sort(Lista_numeros):
    i = 1

    while i < len(Lista_numeros):
        valor_atual = Lista_numeros[i]
        trocou = False
        j = i - 1

        while j >= 0 and Lista_numeros[j] > valor_atual:
            Lista_numeros[j + 1] = Lista_numeros[j]
            trocou = True
            j -= 1
        
        if trocou:
            Lista_numeros[j + 1] = valor_atual
        
        i += 1
    


TAMANHOS = [1000, 5000, 10000, 20000, 50000] #define o tamanho da lista

# Loop que cria uma lista, emparalha e mede o tempo de ordenação para insertion e sorted
for tamanho in TAMANHOS:
    lista = list(range(tamanho))
    random.shuffle(lista)
    lista_insertion = lista.copy()
    lista_sorted = lista.copy()

    tempo_antes_insertion = time.time()
    insertion_sort(lista_insertion)
    tempo_depois_insertion = time.time()
    total_insertion = (tempo_depois_insertion - tempo_antes_insertion)

    tempo_antes_sorted = time.time()
    sorted(lista_sorted)
    tempo_depois_sorted = time.time()
    total_sorted = (tempo_depois_sorted - tempo_antes_sorted)


    print(f"Tempo de execução do insertion de uma lista de tamanho {len(lista)}:{total_insertion} segundos")
    print(f"Tempo de execução do sorted de uma lista de tamanho {len(lista)}:{total_sorted} segundos") 
