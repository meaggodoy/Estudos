#Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade
#dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias. Calcular
#quantos dias a pessoa já viveu até hoje.

print("Digite sua idade em anos, meses e dias:")
anos = int(input("Anos: "))
meses = int(input("Meses: "))
dias = int(input("Dias: "))

idade = anos * 365 + meses * 30 + dias

print("Sua idade em dias é de: ", idade)

#Outra maneira:
from datetime import datetime, date
nasc = input("Digite sua data de nascimento: ")
dtNasc = datetime.strptime(nasc, '%d/%m/%Y').date()
agora = date.today()
id = agora - dtNasc
print(id.days)