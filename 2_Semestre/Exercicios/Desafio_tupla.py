
preco = (10.75, 9.78, 100.60)
result =sum(preco)
print("-----------------------------------------")
print("            LISTA DE PREÇOS              ")
print("-----------------------------------------")
print("PRODUTO1....................... R$  {}".format(preco[0]))
print("PRODUTO2....................... R$   {} ".format(preco[1]))
print("PRODUTO3....................... R$ {0:4.2f}".format(preco[2]))
print("-----------------------------------------")
print("TOTAL.......................... R$ {}".format(result))
