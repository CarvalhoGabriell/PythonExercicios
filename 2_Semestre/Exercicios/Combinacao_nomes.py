# lista_nomes =("Ana", "Bia", "Celi", "Diana", "Eva", "Fabia")
#
# def combinacaoPossible(nomes):
#     for a in nomes:
#         for b in nomes:
#             if a != b:
#                 if nomes.index(b) > nomes.index(a):
#                     print(a, "e", b)
#
# print(combinacaoPossible(lista_nomes))


def combinacoes(nomes):
    for a in range(len(nomes)):
        for b in range(len(nomes)):
            if (nomes[a] != nomes[b]) and (b > a):
                print(nomes[a], "e", nomes[b])

nomes = ("Ana", "Bia", "Celi", "Diana", "Eva", "Fabia")
combinacoes(nomes)