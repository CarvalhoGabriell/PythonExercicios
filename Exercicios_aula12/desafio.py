n1 = 1
n2 = 4
n3 = (n1 * n2) + n1
while(n1<=8):
     print(n1, "+", n2, "=", n3)
     n1 += 1
     n2 += 1
     n3 = (n1*n2)+n1


a1 = 1
a2 = 4
soma = 0
while a1 < 9:
    soma = soma + (a1 + a2)
    print("{}+{}={}".format(a1, a2, soma))
    a1 += 1
    a2 += 1