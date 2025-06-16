import random
import time
import matplotlib.pyplot as plt
import pandas as pd

# Função para gerar os vetores de entrada
def gerar_vetor(tamanho, tipo):
    if tipo == 'melhor':
        return list(range(tamanho))  # Vetor crescente
    elif tipo == 'pior':
        return list(range(tamanho, 0, -1))  # Vetor decrescente
    else:
        return random.sample(range(tamanho * 2), tamanho)  # Aleatório (caso médio)

# Implementação do Heap Sort com contagem de comparações e trocas
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

    # Construção inicial do heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    # Extração dos elementos um por um
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        trocas[0] += 1
        heapify(i, 0)

    return comparacoes[0], trocas[0]

# Tamanhos das entradas e tipos de caso
tamanhos = [1000, 10000, 100000]
tipos = ['melhor', 'medio', 'pior']

# Lista para armazenar os resultados
resultados = []

# Execução dos testes
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

        # Salvar os resultados
        resultados.append({
            'Tamanho': tamanho,
            'Caso': tipo,
            'Tempo': tempo_execucao,
            'Comparações': comparacoes,
            'Trocas': trocas
        })

# Converter os resultados em DataFrame
df = pd.DataFrame(resultados)

# ================================
# Gráfico 1: Tempo de Execução vs Tamanho da Entrada
plt.figure(figsize=(8, 5))
for caso in df['Caso'].unique():
    subset = df[df['Caso'] == caso]
    plt.plot(subset['Tamanho'], subset['Tempo'], marker='o', label=f'Caso {caso.capitalize()}')
plt.title('Tempo de Execução vs Tamanho da Entrada (Heap Sort)')
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
plt.title('Comparações vs Tamanho da Entrada (Heap Sort)')
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
plt.title('Trocas vs Tamanho da Entrada (Heap Sort)')
plt.xlabel('Tamanho da Entrada')
plt.ylabel('Número de Trocas')
plt.legend()
plt.grid(True)
plt.show()

df = pd.DataFrame(resultados)
df.to_csv('resultados_bubble.csv', index=False)
print("\n✅ CSV salvo: resultados_bubble.csv")