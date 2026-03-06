import time

inicio = time.time()

with open(r"C:\Users\maria\meag.dev\Python\Exercícios\Atividade CC\dados.txt", "r") as f:
    for linha in f:
        pass #vai percorrer o arquivo
fim = time.time()

print(f"Tempo de Acesso Sequencial: {fim - inicio:.4f} segundos")