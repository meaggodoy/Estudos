#Listas: coleção de elementos
frutas = ["maçã", "pera", "laranja"]
#a lista começa em índice 0

#métodos:
frutas.append("uva") #adiciona um elemento ao final da lista
print(frutas)

frutas.insert(1, "banana") #adiciona um elemento em um índice específico
print(frutas)

frutas.remove("uva") #remove a primeira ocorrência do elemento
print(frutas)

frutaRemovida = frutas.pop(2) #remove elemento pelo índice e retorna
print(frutas)
print(frutaRemovida)

frutas.sort() #ordena a lista em ordem ascendente de elementos
print(frutas)

frutas.reverse() #inverte ordem dos elementos
print(frutas)

print(len(frutas)) #mostra tamanho da lista

#Listas de compreensão:
num = range(1, 11)
#baseado na lista num, vamos criar outra
#novaLista = [expressão for número in lista if condição]
quadradosPares = [x ** 2 for x in num if x % 2 == 0] 
print(quadradosPares) #irá apresentar apenas os quadrados pares na lista de números de 1 a 10

