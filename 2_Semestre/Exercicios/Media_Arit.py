
def media(tuplas):
    mediaTuplas = sum(tuplas) / len(tuplas)
    return mediaTuplas

numbers = (5,48,2,7)

media_numeros = media(numbers)
print("A média aritimedica é: {}".format(media_numeros))

# OU USANDO FOR

def media(tuplas):
    soma = 0
    for num in tuplas:
        soma = soma + num
        result = soma / len(tuplas)
    return result

numeros = (15,10,74,5)

print(media(numeros))