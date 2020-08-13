#
# nomes = ("FIAP", "1TDST", "gabiru", "leticia ne", "ok")
#
#
# def maiorPalavra(tupla):
#     maior_string = 0
#     posicao = 0
#     for i in tupla:
#         if len(i) > posicao:
#             posicao = len(i)
#             maior_string = i
#     return maior_string
#
# print(maiorPalavra(nomes))

# ou na melhor forma

palavras = ("Alanzoka", "Adultoey", "FIAP", "Python", "Java")
caracteres = []

def maiorString(tupla):
    for i in tupla:
        caracteres.append(len(i))
    maior = max(caracteres)
    for x in range(len(caracteres)):
        if (len(tupla[x]) == maior):
            print(tupla[x])

resultado = maiorString(palavras)
