cont = 0
maior_idade = -1
menor_idade = 1000
while cont < 20:
    idade = int(input("Digite uma idade: "))
    if(idade >= 0 and idade < 110):

         if idade > maior_idade:
            maior_idade = idade

         if idade < menor_idade:
            menor_idade = idade

    else:
        print("Idade inválida")
    cont += 1
print("A maior idade fornecida é ", maior_idade, "\n")
print("A menor idade fornecida é ", menor_idade)