"""""
idade = int(input("Digite sua idade: "))

if idade <= 0:
    print("Idade invalida......")
else:
    if idade < 18:
        print("Voce é menor de idade")
    else:
        print("Voce é maior de idade!!!")
"""""
x = 1
y = x
if x > y:
    print("x maior que y")
elif x == y:
    print("x igual a y")
else:
    print("x menor que y")