import random
import time

# Função para gerar os vetores de entrada
def gerar_vetor(tamanho, tipo):
    if tipo == 'melhor':
        return list(range(tamanho))  # Vetor já ordenado
    elif tipo == 'pior':
        return list(range(tamanho, 0, -1))  # Vetor decrescente
    else:
        return random.sample(range(tamanho * 2), tamanho)  # Vetor aleatório

# Implementação do Merge Sort com contagem de comparações
def merge_sort(arr):
    comparacoes = [0]  # Usamos uma lista para contar comparações dentro das funções internas

    def merge(left, right):
        resultado = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparacoes[0] += 1
            if left[i] <= right[j]:
                resultado.append(left[i])
                i += 1
            else:
                resultado.append(right[j])
                j += 1
        resultado.extend(left[i:])
        resultado.extend(right[j:])
        return resultado

    def sort(sub_arr):
        if len(sub_arr) <= 1:
            return sub_arr
        meio = len(sub_arr) // 2
        esquerda = sort(sub_arr[:meio])
        direita = sort(sub_arr[meio:])
        return merge(esquerda, direita)

    resultado = sort(arr)
    for i in range(len(arr)):
        arr[i] = resultado[i]  # Copia de volta para o array original
    return comparacoes[0]

# Tamanhos das entradas
tamanhos = [1000, 10000, 100000]
# Tipos de caso
tipos = ['melhor', 'medio', 'pior']

# Loop para executar os testes
for tamanho in tamanhos:
    for tipo in tipos:
        print(f"\n=== MERGE SORT | Tamanho: {tamanho} elementos | Caso: {tipo.upper()} ===")

        # Gerar o vetor de entrada
        vetor = gerar_vetor(tamanho, tipo)

        # Criar uma cópia para preservar o vetor original
        vetor_copia = vetor.copy()

        # Medir o tempo de execução
        inicio = time.time()
        comparacoes = merge_sort(vetor_copia)
        fim = time.time()
        tempo_execucao = fim - inicio

        # Exibir os resultados
        print(f"Tempo de execução: {tempo_execucao:.4f} segundos")
        print(f"Total de comparações: {comparacoes}")
