import random
import time

# Função para gerar os vetores de entrada
def gerar_vetor(tamanho, tipo):
    if tipo == 'melhor':
        return list(range(tamanho)) 
    elif tipo == 'pior':
        return list(range(tamanho, 0, -1)) 
    else:
        return random.sample(range(tamanho * 2), tamanho) 


def heap_sort(arr):
    n = len(arr)
    comparacoes = [0]
    trocas = [0]

    def heapify(n, i):
        maior = i
        esquerda = 2 * i + 1
        direita = 2 * i + 2

        if esquerda < n:
            comparacoes[0] += 1
            if arr[esquerda] > arr[maior]:
                maior = esquerda

        if direita < n:
            comparacoes[0] += 1
            if arr[direita] > arr[maior]:
                maior = direita

        if maior != i:
            arr[i], arr[maior] = arr[maior], arr[i]
            trocas[0] += 1
            heapify(n, maior)

    
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        trocas[0] += 1
        heapify(i, 0)

    return comparacoes[0], trocas[0]


tamanhos = [1000, 10000, 100000]
# Tipos de caso
tipos = ['melhor', 'medio', 'pior']


for tamanho in tamanhos:
    for tipo in tipos:
        print(f"\n=== HEAP SORT | Tamanho: {tamanho} elementos | Caso: {tipo.upper()} ===")

        vetor = gerar_vetor(tamanho, tipo)

        vetor_copia = vetor.copy()
        
        inicio = time.time()
        comparacoes, trocas = heap_sort(vetor_copia)
        fim = time.time()
        tempo_execucao = fim - inicio
        print(f"Tempo de execução: {tempo_execucao:.4f} segundos")
        print(f"Total de comparações: {comparacoes}")
        print(f"Total de trocas: {trocas}")
