print("Escreva a baixo os numeros de forma crescente")

num1 = int(input("Informe 1° número : "))
num2 = int(input("Informe 2° número: "))
num3 = int(input("Agora o 3° número: "))

if (num1 < num2 < num3):
    print("Correto, você informou de forma crescente")
    print("O menor: {}. O do meio: {}. E o maior: {}".format(num1,num2,num3))
else:
    print("Erro... Por favor verifique a ordem dos números informados")

