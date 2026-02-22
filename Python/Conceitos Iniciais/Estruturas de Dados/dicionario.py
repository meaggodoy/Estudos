pessoa = {"nome": "João", "idade": 25, "cidade": "Madri"}
#Dicionário coleção mutável e não ordenada

#Acesso:
print(pessoa["nome"]) 
print(pessoa.get("idade"))

#Métodos:
print(pessoa.keys()) #retorna as chaves
print(pessoa.values()) #retorna os valores
print(pessoa.items()) #retorna os pares

pessoa.update({"profissao": "Engenheiro"})
print(pessoa) #adiciona no dicionário
