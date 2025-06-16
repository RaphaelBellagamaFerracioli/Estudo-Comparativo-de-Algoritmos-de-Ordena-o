import random
import time
import matplotlib.pyplot as plt
import pandas as pd

# Função para gerar os vetores de entrada
def gerar_vetor(tamanho, tipo):
    if tipo == 'melhor':
        return list(range(tamanho))  # Vetor ordenado crescente
    elif tipo == 'pior':
        return list(range(tamanho, 0, -1))  # Vetor ordenado decrescente
    else:
        return random.sample(range(tamanho * 2), tamanho)  # Vetor aleatório

# Implementação do Bubble Sort
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

# Tamanhos das entradas e tipos de caso
tamanhos = [1000, 10000, 100000]
tipos = ['melhor', 'medio', 'pior']

# Lista para armazenar os resultados
resultados = []

# Execução dos testes
for tamanho in tamanhos:
    for tipo in tipos:
        print(f"\n=== BUBBLE SORT | Tamanho: {tamanho} elementos | Caso: {tipo.upper()} ===")
        vetor = gerar_vetor(tamanho, tipo)
        vetor_copia = vetor.copy()
        inicio = time.time()
        comparacoes, trocas = bubble_sort(vetor_copia)
        fim = time.time()
        tempo_execucao = fim - inicio
        print(f"Tempo de execução: {tempo_execucao:.4f} segundos")
        print(f"Total de comparações: {comparacoes}")
        print(f"Total de trocas: {trocas}")

        # Salvar os resultados com nome do algoritmo
        resultados.append({
            'Algoritmo': 'Bubble Sort',             # <<< Importante para depois juntar com os outros
            'Tamanho': tamanho,
            'Caso': tipo,
            'Tempo': tempo_execucao,
            'Comparações': comparacoes,
            'Trocas': trocas
        })

# Converter resultados em DataFrame
df = pd.DataFrame(resultados)

# Criar o gráfico: Tempo de Execução vs Tamanho da Entrada
plt.figure(figsize=(8, 5))
for caso in df['Caso'].unique():
    subset = df[df['Caso'] == caso]
    plt.plot(subset['Tamanho'], subset['Tempo'], marker='o', label=f'Caso {caso.capitalize()}')

plt.title('Tempo de Execução vs Tamanho da Entrada (Bubble Sort)')
plt.xlabel('Tamanho da Entrada')
plt.ylabel('Tempo de Execução (segundos)')
plt.legend()
plt.grid(True)
plt.show()

# Salvar os resultados em CSV
df.to_csv('resultados_bubble.csv', index=False)
print("\n✅ Resultados salvos no arquivo: resultados_bubble.csv")
