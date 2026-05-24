class TriagemHospitalar:
    def __init__(self):
        self.heap = []          # Lista que representa a estrutura de Max-Heap
        self.pacientes = {}     # Dicionário {nome: índice_na_lista} para acesso O(1)

    def _trocar(self, i, j):
        """Troca dois elementos e atualiza o mapeamento de índices"""
        nome_i = self.heap[i]['nome']
        nome_j = self.heap[j]['nome']
        self.pacientes[nome_i], self.pacientes[nome_j] = j, i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _subir(self, idx):
        """Move o paciente para cima se a dor for maior que a do pai"""
        while idx > 0:
            pai = (idx - 1) // 2
            if self.heap[idx]['dor'] > self.heap[pai]['dor']:
                self._trocar(idx, pai)
                idx = pai
            else:
                break

    def _descer(self, idx):
        """Move o paciente para baixo se a dor for menor que a dos filhos"""
        tamanho = len(self.heap)
        while True:
            maior = idx
            esq = 2 * idx + 1
            dir = 2 * idx + 2

            if esq < tamanho and self.heap[esq]['dor'] > self.heap[maior]['dor']:
                maior = esq
            if dir < tamanho and self.heap[dir]['dor'] > self.heap[maior]['dor']:
                maior = dir

            if maior != idx:
                self._trocar(idx, maior)
                idx = maior
            else:
                break

    def adicionar_paciente(self, nome, dor):
        """Adiciona um novo paciente e rebalanceia o Max-Heap"""
        if nome in self.pacientes:
            self.ajustar_prioridade(nome, dor)
            return
        
        paciente = {'nome': nome, 'dor': dor}
        self.heap.append(paciente)
        idx = len(self.heap) - 1
        self.pacientes[nome] = idx
        self._subir(idx)

    def ajustar_prioridade(self, nome, nova_dor):
        """Altera a prioridade de um paciente já existente (O(log N))"""
        if nome not in self.pacientes:
            print(f"\n[Erro] Paciente {nome} não encontrado.")
            return
        
        print(f"\n Paciente {nome} piorou, ajustando prioridade")
        idx = self.pacientes[nome]
        dor_antiga = self.heap[idx]['dor']
        self.heap[idx]['dor'] = nova_dor

        # Se a dor aumentou, ele sobe; se diminuiu, ele desce
        if nova_dor > dor_antiga:
            self._subir(idx)
        else:
            self._descer(idx)

    def mostrar_estado_fila(self):
        """Mostra a ordem exata de atendimento (1º, 2º, 3º...)"""
        print("\n--- STATUS ATUAL DA FILA (Ordem de Prioridade) ---")
        if not self.heap:
            print("A fila está vazia.")
            return

        # Para mostrar a ordem correta, ordenamos uma cópia da heap
        # A heap garante que o 1º é o maior, mas não garante a ordem total
        fila_ordenada = sorted(self.heap, key=lambda x: x['dor'], reverse=True)

        for i, p in enumerate(fila_ordenada, 1):
            posicao = f"{i}º lugar"

            
            print(f"{posicao:<10} | Paciente: {p['nome']:<10} | Dor: {p['dor']}")
        print("-" * 50)

    def processar_proximo(self):
        """Remove e retorna o paciente com a maior dor (o topo do Max-Heap)"""
        if not self.heap:
            return None
        
        topo = self.heap[0]
        ultimo = self.heap.pop()
        
        if self.heap:
            self.heap[0] = ultimo
            self.pacientes[ultimo['nome']] = 0
            self._descer(0)
            
        del self.pacientes[topo['nome']]
        return topo['nome'], topo['dor']

# --- Simulação ---
hospital = TriagemHospitalar()
hospital.adicionar_paciente("João", 5)
hospital.adicionar_paciente("Maria", 9)
hospital.adicionar_paciente("José", 2)

hospital.mostrar_estado_fila()

# José piorou muito!
hospital.ajustar_prioridade("José", 10)

hospital.mostrar_estado_fila()

# Atendendo o primeiro
nome, dor = hospital.processar_proximo()
print(f"\nChamando para atendimento: {nome} (Dor: {dor})")

hospital.mostrar_estado_fila()