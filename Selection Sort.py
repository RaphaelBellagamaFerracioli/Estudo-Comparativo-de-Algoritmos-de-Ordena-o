import random
import time


def gerar_vetor(tamanho, tipo):
    if tipo == 'melhor':
        return list(range(tamanho))  
    elif tipo == 'pior':
        return list(range(tamanho, 0, -1))  
    else:
        return random.sample(range(tamanho * 2), tamanho) 

def selection_sort(arr):
    n = len(arr)
    comparacoes = 0
    trocas = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            comparacoes += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            trocas += 1
    return comparacoes, trocas

# Tamanhos das entradas
tamanhos = [1000, 10000, 100000]

# Tipos de caso
tipos = ['melhor', 'medio', 'pior']


for tamanho in tamanhos:
    for tipo in tipos:
        print(f"\n=== SELECTION SORT | Tamanho: {tamanho} elementos | Caso: {tipo.upper()} ===")

       
        vetor = gerar_vetor(tamanho, tipo)

        vetor_copia = vetor.copy()

        inicio = time.time()
        comparacoes, trocas = selection_sort(vetor_copia)
        fim = time.time()
        tempo_execucao = fim - inicio

        print(f"Tempo de execução: {tempo_execucao:.4f} segundos")
        print(f"Total de comparações: {comparacoes}")
        print(f"Total de trocas: {trocas}")
