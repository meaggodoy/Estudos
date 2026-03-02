"""
Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por mês,
mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas por ele
efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor total de suas
vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e escreva o salário final do
vendedor.
"""

salario_fixo = float(input("Digite seu salário fixo: "))
carros_vendidos = int(input("Digite o número de carros vendidos: "))
total_vendas = float(input("Digite o valor total de suas vendas: "))
valor_carro = float(input("Digite o valor ganho em cada carro: "))

salario_final = salario_fixo + (0.05 * total_vendas) + (valor_carro * carros_vendidos)

print("Seu salário final será de: ", salario_final)