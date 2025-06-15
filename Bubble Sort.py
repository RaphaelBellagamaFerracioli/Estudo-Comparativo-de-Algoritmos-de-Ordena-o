import random
import time

# Gera valores de entrada para o algoritmo Bubble Sort
def gerar_vetor(tamanho, tipo):
    if tipo == 'melhor':
        return list(range(tamanho)) 
    elif tipo == 'pior':
        return list(range(tamanho, 0, -1))  
    else:
        return random.sample(range(tamanho * 2), tamanho) 


def bubble_sort(arr):
    n = len(arr)
    comparacoes = 0
    trocas = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            comparacoes += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocas += 1
    return comparacoes, trocas


tamanhos = [1000, 10000, 100000]
# Tipos de caso
tipos = ['melhor', 'medio', 'pior']


for tamanho in tamanhos:
    for tipo in tipos:
        print(f"\nBUBBLE SORT | Tamanho: {tamanho} elementos | Caso: {tipo.upper()} ===")

        # Gerar o vetor conforme o tipo de entrada
        vetor = gerar_vetor(tamanho, tipo)

        
        vetor_copia = vetor.copy()

        
        inicio = time.time()
        comparacoes, trocas = bubble_sort(vetor_copia)
        fim = time.time()
        tempo_execucao = fim - inicio

        
        print(f"Tempo de execução: {tempo_execucao:.4f} segundos")
        print(f"Total de comparações: {comparacoes}")
        print(f"Total de trocas: {trocas}")
