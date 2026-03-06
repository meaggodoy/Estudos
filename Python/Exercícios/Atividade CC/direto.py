import linecache
import time

linha_desejada = 99999

inicio = time.time()

conteudo = linecache.getline(r"C:\Users\maria\meag.dev\Python\Exercícios\Atividade CC\dados.txt", linha_desejada)
fim = time.time()

print(f"Conteúdo: {conteudo.strip()}")
print(f"Tempo de Acesso Direto: {fim - inicio:.4f} segundos")