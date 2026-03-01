#Faça um algoritmo que pergunte quanto a pessoa ganha por hora (salário por hora) e o número
#de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
from datetime import datetime, timedelta

salarioHora = float(input("Quanto você ganha por hora? "))
mes = input("Quantas horas você trabalhou esse mês? ")

tempo = datetime.strptime(mes, '%H:%M')

total = tempo.minute/60 + tempo.hour
salario = total * salarioHora

print("Seu salário do mês será de: ", salario)
