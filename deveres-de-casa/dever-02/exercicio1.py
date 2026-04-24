import time 

#função que calcular o fatorial de um número
def fatorial(n):
    
    if n == 1:
        return 1
    

    return n * fatorial(n - 1)

#lista para calcular o fatorial dos elementos
lista = [10, 100, 500, 1000]

#loop que calcular o fatorial e o tempo de cada elemento da lista
for i in lista:

    tempo_antes = time.time()
    fatorial(i)
    tempo_depois = time.time()

    tempo_total = tempo_depois - tempo_antes

    print(f"O tempo de execução para o fatorial de {i} é: {tempo_total} segundos")
    

'''
A complexidade do algoritmo é O(n), pois a n é proporcional a quantidade de chamadas recursivas.
se for fatorial de 10, Terá 10 chamadas recursivas e 10 multiplicações.OU seja, no final a quantidade
de multiplicações e chamadas e proporcional a número que quer saber o fatorial.


'''

