import random
import time
import matplotlib.pyplot as plt
import pandas as pd

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
tipos = ['melhor', 'medio', 'pior']

resultados = []

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

        resultados.append({
            'Tamanho': tamanho,
            'Caso': tipo,
            'Tempo': tempo_execucao,
            'Comparações': comparacoes,
            'Trocas': trocas
        })

# Converter para DataFrame
df = pd.DataFrame(resultados)

# Gráfico 1: Tempo de Execução vs Tamanho da Entrada
plt.figure(figsize=(8, 5))
for caso in df['Caso'].unique():
    subset = df[df['Caso'] == caso]
    plt.plot(subset['Tamanho'], subset['Tempo'], marker='o', label=f'Caso {caso.capitalize()}')
plt.title('Tempo de Execução vs Tamanho da Entrada (Insertion Sort)')
plt.xlabel('Tamanho da Entrada')
plt.ylabel('Tempo de Execução (segundos)')
plt.legend()
plt.grid(True)
plt.show()

# Gráfico 2: Comparações vs Tamanho da Entrada
plt.figure(figsize=(8, 5))
for caso in df['Caso'].unique():
    subset = df[df['Caso'] == caso]
    plt.plot(subset['Tamanho'], subset['Comparações'], marker='o', label=f'Caso {caso.capitalize()}')
plt.title('Comparações vs Tamanho da Entrada (Insertion Sort)')
plt.xlabel('Tamanho da Entrada')
plt.ylabel('Número de Comparações')
plt.legend()
plt.grid(True)
plt.show()

# Gráfico 3: Trocas vs Tamanho da Entrada
plt.figure(figsize=(8, 5))
for caso in df['Caso'].unique():
    subset = df[df['Caso'] == caso]
    plt.plot(subset['Tamanho'], subset['Trocas'], marker='o', label=f'Caso {caso.capitalize()}')
plt.title('Trocas vs Tamanho da Entrada (Insertion Sort)')
plt.xlabel('Tamanho da Entrada')
plt.ylabel('Número de Trocas')
plt.legend()
plt.grid(True)
plt.show()

df = pd.DataFrame(resultados)
df.to_csv('resultados_bubble.csv', index=False)
print("\n✅ CSV salvo: resultados_bubble.csv")