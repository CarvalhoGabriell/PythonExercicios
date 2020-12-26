listaA = [9,8,7,1,6,2,4,3,1,6]
listaB = [8,6,4,9,5,3,1,3,6,4]
listA = set(listaA)
listB = set(listaB)

uniao = list(listB.union(listA))
result = listaA + listaB
print("Numeros que existem na mesma lista", listA.intersection(listB))
print("Numeros que aparecem na listA e nao na listB", listA.difference(listB))
print("Todos os elementos das duas listas: ", result)
print("Uniao das duas lista sem numeros repetidos, ",uniao)

# faltou esse
def numerosRepetidos(lista):
    repetidos =[]
    numero =[]
    for num in lista:
        if num in numero:
            repetidos.append(num)
        else:
            numero.append(num)
    return repetidos

print("Valores repetidos na listaA, ",numerosRepetidos(listaA))
print("Valores repetidos na listaA, ",numerosRepetidos(listaB))