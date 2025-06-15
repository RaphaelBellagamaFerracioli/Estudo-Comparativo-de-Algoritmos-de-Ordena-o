import random
import time

# Função para gerar os vetores de entrada
def gerar_vetor(tamanho, tipo):
    if tipo == 'melhor':
        return list(range(tamanho))  # Ordenado crescente (pior caso clássico com pivot no fim)
    elif tipo == 'pior':
        return list(range(tamanho, 0, -1))  # Ordenado decrescente
    else:
        return random.sample(range(tamanho * 2), tamanho)  # Aleatório (caso médio)

# Implementação do Quick Sort com contadores
def quick_sort(arr):
    comparacoes = [0]
    trocas = [0]

    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparacoes[0] += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                trocas[0] += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        trocas[0] += 1
        return i + 1

    def quicksort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quicksort_recursive(low, pi - 1)
            quicksort_recursive(pi + 1, high)

    quicksort_recursive(0, len(arr) - 1)
    return comparacoes[0], trocas[0]

# Tamanhos das entradas
tamanhos = [1000, 10000, 100000]

# Tipos de caso
tipos = ['melhor', 'medio', 'pior']

# Loop para executar os testes
for tamanho in tamanhos:
    for tipo in tipos:
        print(f"\n=== QUICK SORT | Tamanho: {tamanho} elementos | Caso: {tipo.upper()} ===")

        # Gerar o vetor conforme o tipo de entrada
        vetor = gerar_vetor(tamanho, tipo)

        # Criar uma cópia para preservar o vetor original
        vetor_copia = vetor.copy()

        # Medir o tempo de execução
        inicio = time.time()
        comparacoes, trocas = quick_sort(vetor_copia)
        fim = time.time()
        tempo_execucao = fim - inicio

        # Exibir os resultados
        print(f"Tempo de execução: {tempo_execucao:.4f} segundos")
        print(f"Total de comparações: {comparacoes}")
        print(f"Total de trocas: {trocas}")
