
num = int(input("Por favor digite aqui qualquer número: "))

if(num > 0 and num < 30):
    print("O numero {} esta entre esse intervalo entre 0 e 30.".format(num))
elif (num > 40 and num < 79):
    print("O numero {} esta entre esse intervalo entre 40 e 79.".format(num))
else:
    print("O numero {} não esta dentro dos intervalos acima".format(num))