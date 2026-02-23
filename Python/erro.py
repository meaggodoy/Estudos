def erroZero(a, b):
    return 10 / 0

try:
    erroZero(10, 0)
except:
    print("Erro. Divisão por zero")