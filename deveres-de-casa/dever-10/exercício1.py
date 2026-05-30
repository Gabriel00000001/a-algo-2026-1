import heapq

def dijkstra(grafo, inicio, fim):
    # Inicializa distâncias com infinito e o início com 0
    distancias = {no: float('inf') for no in grafo}
    distancias[inicio] = 0
    
    # Dicionário para rastrear o caminho (predecessores)
    predecessores = {no: None for no in grafo}
    
    # Fila de prioridade: (distancia, no_atual)
    fila_prioridade = [(0, inicio)]
    
    while fila_prioridade:
        distancia_atual, no_atual = heapq.heappop(fila_prioridade)
        
        # Se já encontramos um caminho melhor para esse nó, ignoramos
        if distancia_atual > distancias[no_atual]:
            continue
            
        # Explora os vizinhos
        for vizinho, peso in grafo[no_atual].items():
            distancia = distancia_atual + peso
            
            # Se o novo caminho for menor, atualiza
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                predecessores[vizinho] = no_atual
                heapq.heappush(fila_prioridade, (distancia, vizinho))
    
    # Reconstrói o caminho de trás para frente
    caminho = []
    atual = fim
    while atual is not None:
        caminho.append(atual)
        atual = predecessores[atual]
    
    return caminho[::-1], distancias[fim]

# Representação do grafo da imagem (Dicionário de Adjacência)
grafo = {
    0: {1: 4, 2: 1},
    1: {3: 1},
    2: {1: 2, 4: 5},
    3: {4: 1},
    4: {}
}

# Execução
rota, custo = dijkstra(grafo, 0, 4)

print(f"Caminho Mínimo: {rota}")
print(f"Custo Total: {custo}")