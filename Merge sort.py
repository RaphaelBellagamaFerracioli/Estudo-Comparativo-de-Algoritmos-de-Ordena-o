import random
import time
import matplotlib.pyplot as plt
import pandas as pd

# Função para gerar os vetores de entrada
def gerar_vetor(tamanho, tipo):
    if tipo == 'melhor':
        return list(range(tamanho))  # Ordenado crescente
    elif tipo == 'pior':
        return list(range(tamanho, 0, -1))  # Ordenado decrescente
    else:
        return random.sample(range(tamanho * 2), tamanho)  # Aleatório (caso médio)

# Implementação do Merge Sort com contagem de comparações e trocas
def merge_sort(arr):
    comparacoes = [0]
    trocas = [0]

    def merge(left, right):
        resultado = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparacoes[0] += 1
            if left[i] <= right[j]:
                resultado.append(left[i])
                trocas[0] += 1  # Contando movimentação como troca
                i += 1
            else:
                resultado.append(right[j])
                trocas[0] += 1
                j += 1
        while i < len(left):
            resultado.append(left[i])
            trocas[0] += 1
            i += 1
        while j < len(right):
            resultado.append(right[j])
            trocas[0] += 1
            j += 1
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
        arr[i] = resultado[i]
    return comparacoes[0], trocas[0]

# Tamanhos das entradas e tipos de caso
tamanhos = [1000, 10000, 100000]
tipos = ['melhor', 'medio', 'pior']

resultados = []

# Loop de execução
for tamanho in tamanhos:
    for tipo in tipos:
        print(f"\n=== MERGE SORT | Tamanho: {tamanho} elementos | Caso: {tipo.upper()} ===")
        vetor = gerar_vetor(tamanho, tipo)
        vetor_copia = vetor.copy()
        inicio = time.time()
        comparacoes, trocas = merge_sort(vetor_copia)
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

# Converter resultados para DataFrame
df = pd.DataFrame(resultados)

# ================================
# Gráfico 1: Tempo de Execução vs Tamanho da Entrada
plt.figure(figsize=(8, 5))
for caso in df['Caso'].unique():
    subset = df[df['Caso'] == caso]
    plt.plot(subset['Tamanho'], subset['Tempo'], marker='o', label=f'Caso {caso.capitalize()}')
plt.title('Tempo de Execução vs Tamanho da Entrada (Merge Sort)')
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
plt.title('Comparações vs Tamanho da Entrada (Merge Sort)')
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
plt.title('Trocas vs Tamanho da Entrada (Merge Sort)')
plt.xlabel('Tamanho da Entrada')
plt.ylabel('Número de Trocas')
plt.legend()
plt.grid(True)
plt.show()

df = pd.DataFrame(resultados)
df.to_csv('resultados_bubble.csv', index=False)
print("\n✅ CSV salvo: resultados_bubble.csv")