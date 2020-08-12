# sports = ("futebol", "Golf", "Volei", "Basquet", "Judo", "Esport")
#
# # FAZER COM WHILE
# mostrar = 0
# while mostrar < len(sports):
#     print(sports[mostrar])
#     mostrar += 1
#
# # OU FAZER COM FOR
# for i in sports:
#     print(i)

numeros = (10,25,23,13,70,99,69,7,88,100,199,45,75)

print(type(numeros))

print("***** Lista de numeros da tupla ****\n")
for mostrar in numeros:
    print("Numeros da tupla: {}".format(mostrar))