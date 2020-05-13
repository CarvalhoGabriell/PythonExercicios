x = float(input("Informe uma medida: "))
y = float(input("Informe uma segunda medida: "))
z = float(input("Informe a ultima medida: "))

if(x + y < z and x + z < y and z + y < x):
    print("############ AGORA VAMOS VERIFICAR SE CONSEGUIMOS MONTAR UM TRIÂNGULO COM ELES ############\n")
    if (x == y == z ):
        print("Você formou um Triângulo Equilátero -> Todos os lados são iguais")
    elif(x == y or x == z or z == y):
        print("Você formou um Triângulo Isósceles - > Existem dois lados iguais")
    else:
        print("Você construiu um Triângulo Escaleno -> Todos os lados são de medidas diferentes")
        print("Medidas inválidas, não se pode montae um triângulo com valor 0\n")
else:
    print("Medidas inválidas, não se pode montae um triângulo com valor 0\n")