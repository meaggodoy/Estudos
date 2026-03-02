#Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos
#brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total
#de eleitores.

import pandas as pd

#df = data frame | r = read, também pra não dar problema com o caminho do arquivo
df = pd.read_excel(r"C:\Users\maria\meag.dev\Python\Exercícios Operadores\votacao_individual_municipio.xlsx")


print(df['Voto'].value_counts(normalize=True).round(3)*100)
