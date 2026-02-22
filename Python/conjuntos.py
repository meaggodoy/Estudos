c1 = {1, 2, 3}
c2 = set([3, 4, 5, 6])
#Conjuntos

uniao = c1 | c2
print(uniao) 

interseccao = c1 & c2
print(interseccao) 

diferenca = c1 - c2
print(diferenca) 

simetria = c1 ^ c2
print(simetria) #equivalente ao q n foi apresentado na interseccao

#operações por fora
frutas = {"maçã", "pera", "uva"}
frutas.add("banana")
print(frutas)
frutas.remove("uva")
print(frutas)
frutas.discard("morango")
print(frutas) #se tiver o elemento, descarta, senão não faz nada
frutas.clear()
print(frutas) #remove tudo
