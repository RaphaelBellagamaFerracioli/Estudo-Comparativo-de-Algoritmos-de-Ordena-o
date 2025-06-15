import random
import time

def gerar_vetor(tamanho, tipo):
    if tipo == 'melhor':
        return list(range(tamanho))  
    elif tipo == 'pior':
        return list(range(tamanho, 0, -1))  
    else:
        return random.sample(range(tamanho * 2), tamanho)  


def insertion_sort(arr):
    n = len(arr)
    comparacoes = 0
    trocas = 0
    for i in range(1, n):
        chave = arr[i]
        j = i - 1
        while j >= 0:
            comparacoes += 1  
            if arr[j] > chave:
                arr[j + 1] = arr[j]
                trocas += 1
                j -= 1
            else:
                break
        arr[j + 1] = chave
        if j + 1 != i:
            trocas += 1  
    return comparacoes, trocas


tamanhos = [1000, 10000, 100000]

# Tipos de caso
tipos = ['melhor', 'medio', 'pior']

# Loop para executar os testes
for tamanho in tamanhos:
    for tipo in tipos:
        print(f"\n=== INSERTION SORT | Tamanho: {tamanho} elementos | Caso: {tipo.upper()} ===")

        
        vetor = gerar_vetor(tamanho, tipo)

        
        vetor_copia = vetor.copy()

        
        inicio = time.time()
        comparacoes, trocas = insertion_sort(vetor_copia)
        fim = time.time()
        tempo_execucao = fim - inicio

        
        print(f"Tempo de execução: {tempo_execucao:.4f} segundos")
        print(f"Total de comparações: {comparacoes}")
        print(f"Total de trocas: {trocas}")
