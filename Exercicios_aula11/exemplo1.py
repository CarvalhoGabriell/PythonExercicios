
cont = 3
senha = int(input("Digite sua senha: "))
while(senha!= 1214 and cont>1):
    print("Senha incorreta. Você tem mais ", cont-1, "chances")
    senha= int(input("Digite a senha novamente: "))
    cont = cont - 1

if(senha == 1214):
    print("Acesso permitido")
else:
    print("Senha bloqueada !!! Contate o setor responsável...")