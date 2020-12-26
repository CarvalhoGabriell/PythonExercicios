
soma_notas = 0

for notas in range(1,5):
    nota = float(input("Digite suas notas: "))
    if nota >=0:
        soma_notas += nota
        media = soma_notas / 4
    print(nota)
print(media)