def ola():
    print("Olá, Mundo!")

def saudacao(nome):
    print(f"Olá, {nome}")

def soma(a, b):
    return a + b
resultado = soma(3, 4)
print(resultado)

ola()
saudacao("Maria")

#função anônima
quadrado = lambda x: x ** 2
print(quadrado(5))
