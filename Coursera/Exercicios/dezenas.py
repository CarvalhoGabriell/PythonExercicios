valor = int(input("Informe um valor inteiro:"))

# extraindo o valor da unidade do numero
unidade = valor % 10

#excluindo o valor da unidade
valor =(valor -unidade) //10

# capturando o valor da dezena
dezena = valor %10

print("O dígito das dezenas é",dezena)