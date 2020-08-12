
def maiornumero(tuplas):

    for i in range(len(tuplas)):
        numero = int(tuplas[0])
        if int(tuplas[i]) > int(numero):
            maior_num = int(tuplas[i])
    return maior_num


numbers = (10,20,4,5,48,75,9,100,2,1000)

maior_numero = maiornumero(numbers)
print("O maior numero é: {}".format(maior_numero))