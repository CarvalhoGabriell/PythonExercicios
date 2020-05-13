nome = input("Digite seu nome aqui: ")
notSemest = float(input("Olá {} , digite aqui sua nota: ".format(nome)))
notalab = float(input("Digte aqui sua segunda nota: "))
notaFim = float(input("Digite aqui sua última nota: "))

mediaPom = ((notSemest*2) + (notalab*3) + (notaFim*5))/10

print(mediaPom)

if (mediaPom< 0 or mediaPom >10):
    print("Média inválida, verifique suas notas")
else:

    if (mediaPom >= 0.0 and mediaPom <= 4.9): {
        print("Conceito E")
        }

    elif (mediaPom >= 5.0  and mediaPom <= 5.9): {
            print("Conceito D")
        }

    elif (mediaPom >= 6.0 and mediaPom <= 6.9): {
            print("Conceito C")
        }

    elif (mediaPom >= 7 and mediaPom <= 7.9): {
            print("Conceito B")
        }

    elif (mediaPom >= 8 and mediaPom <= 10.0): {
            print("Conceito A")
        }

