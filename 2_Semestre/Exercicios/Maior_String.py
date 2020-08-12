
nomes = ("FIAP", "1TDST", "gabiru", "leticia ne", "ok")


def maiorPalavra(tupla):
    maior_string = 0
    for i in range(len(tupla)):
        if tupla[i] > maior_string:
            return maior_string

print(maiorPalavra(nomes))