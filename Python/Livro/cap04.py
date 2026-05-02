#Exercício 4.2:
velocidade = int(input("Digite sua velocidade: "))

if velocidade > 80:
    print("Você foi multado.")
    multa = 5 * (velocidade - 80)
    print(multa)
else:
    print("Dentro dos limites.")

#Exercício 4.3 (Misericórdia)
"""
n1 = int(input("Digite valor 1: "))
n2 = int(input("Digite valor 2: "))
n3 = int(input("Digite valor 3: "))

if n1 > n2 and n1 > n3:
    print(f"O valor de {n1} é o maior")
if n2 > n1 and n2 > n3:
    print(f"O valor de {n2} é o maior")
if n3 > n1 and n3 > n2:
    print(f"O valor de {n3} é o maior")

if n1 < n2 and n1 < n3:
    print(f"O valor de {n1} é o menor")
if n2 < n1 and n2 < n3:
    print(f"O valor de {n2} é o menor")
if n3 < n1 and n3 < n2:
    print(f"O valor de {n3} é o menor")
"""