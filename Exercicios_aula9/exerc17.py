custo = float(input("Informe quanto custou seu produto: "))

precoVen = custo + (custo * 0.45)
# Lucro de 45% se o valor da compra for < R$ 20,00
if custo <= 20.0:
    print("O produto custou {} e para ter um lucro de 45% a venda dele deve ser de R${} reais".format(custo, precoVen))
else:
    ## Lucro de 30% se o valor da compra for > R$ 20,00
    if custo > 20.0:
        print("O produto custou {} e para ter um lucro de 30% a venda dele deve ser de R${} reais".format(custo, precoVen))
