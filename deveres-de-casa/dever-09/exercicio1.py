import heapq

def prim_mst(vertices, grafo):
    # Escolhemos o vértice 'A' como ponto de partida
    inicio = 'A'
    mst = []
    visitados = {inicio}
    # Arestas candidatas: (peso, origem, destino)
    arestas_candidatas = [
        (peso, inicio, destino) for destino, peso in grafo[inicio]
    ]
    heapq.heapify(arestas_candidatas) # Transforma em fila de prioridade (menor peso primeiro)

    custo_total = 0

    print(f"{'Exploração':<15} | {'Aresta Escolhida':<20} | {'Custo':<10}")
    print("-" * 50)

    while arestas_candidatas:
        peso, u, v = heapq.heappop(arestas_candidatas)

        if v not in visitados:
            visitados.add(v)
            mst.append((u, v, peso))
            custo_total += peso
            
            print(f"Conectando {v:<6} | {u} - {v:<13} | {peso:<10}")

            # Adiciona as novas arestas do vértice que acabamos de conectar
            for vizinho, proximo_peso in grafo[v]:
                if vizinho not in visitados:
                    heapq.heappush(arestas_candidatas, (proximo_peso, v, vizinho))

    return mst, custo_total

# --- Configuração do Grafo (Dicionário de Adjacência) ---
# Representa as conexões da imagem
grafo = {
    'A': [('B', 2), ('D', 3), ('C', 6)],
    'B': [('A', 2), ('D', 5)],
    'C': [('A', 6), ('D', 4)],
    'D': [('A', 3), ('B', 5), ('C', 4)]
}

vertices = ['A', 'B', 'C', 'D']

# Execução
resultado_mst, total = prim_mst(vertices, grafo)

print("-" * 50)
print(f"Custo Total da MST: {total}")
print("Arestas que formam a MST:", resultado_mst)