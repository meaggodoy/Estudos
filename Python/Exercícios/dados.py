with open("dados.txt", "w") as f:
    for i in range(1, 1000001):
        f.write(f"Linha {i}: Dados sequenciais\n")

print("Arquivo criado com sucesso!")