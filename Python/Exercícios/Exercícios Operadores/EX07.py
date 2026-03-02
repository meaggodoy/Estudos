#Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de
#reajuste. Calcular e escrever o valor do novo salário.

salario = float(input("Digite seu salário atual: "))
reajuste = float(input("Digite o percentual de reajuste: "))

novo_salario = (1+(reajuste/100)) * salario

print("Seu novo salário será de: ", novo_salario)