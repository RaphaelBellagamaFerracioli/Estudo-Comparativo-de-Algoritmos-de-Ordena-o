import random
import time
import matplotlib.pyplot as plt
import pandas as pd
import sys

# Aumentar o limite de recursão
sys.setrecursionlimit(20000)

# Função para gerar os vetores de entrada
def gerar_vetor(tamanho, tipo):
    if tipo == 'melhor':
        return list(range(tamanho))  # Ordenado crescente
    elif tipo == 'pior':
        return list(range(tamanho, 0, -1))  # Ordenado decrescente
    else:
        return random.sample(range(tamanho * 2), tamanho)  # Aleatório (caso médio)

# Implementação do Quick Sort com pivô aleatório
def quick_sort(arr):
    comparacoes = [0]
    trocas = [0]

    def partition(low, high):
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        trocas[0] += 1

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

# Tamanhos das entradas e tipos de caso
tamanhos = [1000, 10000, 100000]
tipos = ['melhor', 'medio', 'pior']

resultados = []

# Loop de execução
for tamanho in tamanhos:
    for tipo in tipos:
        print(f"\n=== QUICK SORT | Tamanho: {tamanho} elementos | Caso: {tipo.upper()} ===")
        vetor = gerar_vetor(tamanho, tipo)
        vetor_copia = vetor.copy()
        inicio = time.time()
        comparacoes, trocas = quick_sort(vetor_copia)
        fim = time.time()
        tempo_execucao = fim - inicio
        print(f"Tempo de execução: {tempo_execucao:.4f} segundos")
        print(f"Total de comparações: {comparacoes}")
        print(f"Total de trocas: {trocas}")

        resultados.append({
            'Tamanho': tamanho,
            'Caso': tipo,
            'Tempo': tempo_execucao,
            'Comparações': comparacoes,
            'Trocas': trocas
        })

# Converter resultados em DataFrame
df = pd.DataFrame(resultados)

# ================================
# Gráfico 1: Tempo de Execução vs Tamanho da Entrada
plt.figure(figsize=(8, 5))
for caso in df['Caso'].unique():
    subset = df[df['Caso'] == caso]
    plt.plot(subset['Tamanho'], subset['Tempo'], marker='o', label=f'Caso {caso.capitalize()}')
plt.title('Tempo de Execução vs Tamanho da Entrada (Quick Sort)')
plt.xlabel('Tamanho da Entrada')
plt.ylabel('Tempo de Execução (segundos)')
plt.legend()
plt.grid(True)
plt.show()

# ================================
# Gráfico 2: Comparações vs Tamanho da Entrada
plt.figure(figsize=(8, 5))
for caso in df['Caso'].unique():
    subset = df[df['Caso'] == caso]
    plt.plot(subset['Tamanho'], subset['Comparações'], marker='o', label=f'Caso {caso.capitalize()}')
plt.title('Comparações vs Tamanho da Entrada (Quick Sort)')
plt.xlabel('Tamanho da Entrada')
plt.ylabel('Número de Comparações')
plt.legend()
plt.grid(True)
plt.show()

# ================================
# Gráfico 3: Trocas vs Tamanho da Entrada
plt.figure(figsize=(8, 5))
for caso in df['Caso'].unique():
    subset = df[df['Caso'] == caso]
    plt.plot(subset['Tamanho'], subset['Trocas'], marker='o', label=f'Caso {caso.capitalize()}')
plt.title('Trocas vs Tamanho da Entrada (Quick Sort)')
plt.xlabel('Tamanho da Entrada')
plt.ylabel('Número de Trocas')
plt.legend()
plt.grid(True)
plt.show()

df = pd.DataFrame(resultados)
df.to_csv('resultados_bubble.csv', index=False)
print("\n✅ CSV salvo: resultados_bubble.csv")