#validação para não permitir número negativo
def validar_se_negativo(var):
    while True:
        if var < 0:
            print("Número inválido. Digite novamente: ")
        else: 
            break