
senhaAluno = input("Por favor informe sua senha de aluno para ter acesso ao sistema da FIAP: ").upper()

if(senhaAluno == "FIAP1TDS"):
    print("Acesso permitido")
else :
    print("Acesso negado, você não tem permissão")