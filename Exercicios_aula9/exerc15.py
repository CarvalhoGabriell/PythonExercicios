nome = input("Olá Aluno(a), Digite seu nome aqui: ")
print("Salveee {}, fala suas notas abaixo pra gente conferir seu Status!!".format(nome).upper())
nota1 = float(input(" Informe sua nota 1: "))
nota2 = float(input(" Informe sua nota 2: "))
nota3 = float(input(" Informe sua nota 3: "))

totalFalt = int(input("Informe também o números de faltas que você teve: "))
# limite_falta = 80 * 0.25 = 20

media = (nota1 + nota2 + nota3)//3
if(media < 7.0):
    print(" {} você está REPROVADO POR MÉDIA...".format(nome).upper())
    if (media < 7.0 and totalFalt > 20):
        print("E infelizmente foi reprovado por faltas também".upper())
elif(totalFalt > 20):
    print(" {} você está REPROVADO POR FALTAS...".format(nome).upper())

else:
    print("Status APROVADO {}, nos vemos no próximo ano!!!".format(nome).upper())