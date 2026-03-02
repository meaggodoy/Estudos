"""
O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem do
distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do distribuidor
seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de fábrica de um carro,
calcular e escrever o custo final ao consumidor
"""

custo_fabrica = float(input("Digite o valor de custo de fábrica do veículo: "))

custo_final = (1 + 0.28 + 0.45) * custo_fabrica

print("O custo final para o consumidor será de: ", custo_final)