def anoBissexto(ano):
    if ano % 4 == 0:
        print("Esse ",ano, "é um ano Bisexto, Fevereiro teve 28 dias.")
    elif ano % 400 == 0:
        print("Esse ",ano, "é um ano Bisexto, Fevereiro teve 28 dias.")
    elif ano % 100 == 0:
        print("O ",ano, "Não É bisexto logo Fevereiro tem 29 dias.")

def informeData(dia, mes, ano):

    meses = ("janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro")
    if dia < 31:
        mesExtenso = meses[mes - 1]
        if mesExtenso == "fevereiro" and dia >= 30:
            print("Fevereiro só tem 28 ou 29 dias")
        elif mesExtenso == 'fevereiro' and dia > 28 and anoBissexto(ano) == False:
            print("Fevereiro só tem 28 dias em anos não bissextos!")
        elif ((mesExtenso == 'abril' or mesExtenso == 'junho' or mesExtenso == 'setembro'
               or mesExtenso == 'novembro') and dia == 31):
            print("O Mes de ", mesExtenso, " não tem 31 dias")
        else:
            print("%d de %s de %i" % (dia, mesExtenso, ano))
    else:
        print("Dia inválido")


data = input("Informe uma data no seguinte formato, <DD/MM/AAAA>: ")
dia,mes,ano = data.split('/')
informeData(int(dia), int(mes), int(ano))





