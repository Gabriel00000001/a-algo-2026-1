def bellman_ford(vertices, arestas, origem):
    # Inicialização: Distância infinita para todos e None para predecessores
    distancias = {v: float('inf') for v in vertices}
    predecessores = {v: None for v in vertices}
    distancias[origem] = 0

    n_vertices = len(vertices)
    
    print(f"{'Iteração':<10} | {'Vértices (Distância/Predecessor)':<60}")
    print("-" * 80)

    # Relaxamento das arestas (V-1 vezes)
    for i in range(1, n_vertices):
        for u, v, peso in arestas:
            if distancias[u] != float('inf') and distancias[u] + peso < distancias[v]:
                distancias[v] = distancias[u] + peso
                predecessores[v] = u
        
        # Formatação para exibir a tabela como no dever
        linha = " | ".join([f"V{v}: {distancias[v]}/{predecessores[v]}" for v in vertices])
        print(f"Iteração {i:<2} | {linha}")

    # Verificação de Ciclo Negativo
    tem_ciclo_negativo = False
    for u, v, peso in arestas:
        if distancias[u] != float('inf') and distancias[u] + peso < distancias[v]:
            tem_ciclo_negativo = True
            break

    return distancias, tem_ciclo_negativo

# --- Configuração do Grafo da Imagem ---
vertices = [0, 1, 2, 3, 4]
# (origem, destino, peso)
arestas = [
    (0, 1, 5),
    (1, 2, 1),
    (1, 3, 2),
    (2, 4, 1),
    (4, 3, -1)
]

# Execução
dist_finais, ciclo = bellman_ford(vertices, arestas, 0)

print("-" * 80)
print(f"Existe ciclo negativo? {'Sim' if ciclo else 'Não'}")