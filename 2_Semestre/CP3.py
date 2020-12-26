from openpyxl import load_workbook

wb = load_workbook('Planilha.xlsx')
nomePlan = wb['Plan1']
sheet = wb.active


def media1Semestre(nota):
    celula = sheet[nota]
    print("Semestre 1...........:", celula.value, "\n")


def mostrarDisciplina(celula1, celula2):
    celulas = sheet[celula1:celula2]
    for c1, c2, c3 in celulas:
        print("{} {} {}".format(c1.value, c2.value, c3.value))


def dadosDoAluno(celula1, celula2):
    celulas1 = sheet[celula1: celula2]
    for c1, c2 in celulas1:
        print("{0:8} --> {1:8} \n".format(c1.value, c2.value))


def notasCp(celula1, celula2):
    celulas = sheet[celula1: celula2]
    global media_cp
    for c1, c2, c3 in celulas:
        nota1 = c1.value
        nota2 = c2.value
        nota3 = c3.value

        if nota1 < nota2 and nota1 < nota3:
            nota1 = 0
            media_cp = (nota2 + nota3) / 2
        elif nota2 < nota1 and nota2 < nota3:
            nota2 = 0
            media_cp = (nota1 + nota3) / 2
        elif nota3 < nota2 and nota3 < nota1:
            nota3 = 0
            media_cp = (nota1 + nota2) / 2
        else:
            print("erro")
    print("Checkpoints (Média).......:", media_cp)
    return media_cp


def notasChallenge(celula1, celula2):
    celulas2 = sheet[celula1: celula2]
    global media_chall
    for c1, c2 in celulas2:
        challengNota1 = c1.value
        challengNota2 = c2.value
        media_chall = (challengNota1 + challengNota2) / 2
    print("Challenge...............:", media_chall)
    return media_chall


def calculoGlobalSolut(media_check, media_chal):
    global global_solucion
    global_solucion = (((6 - (0.4 * 6)) / 0.6) - (0.4 * (media_check + media_chal) / 2)) / 0.6
    print("Nota mínima na Global Solution para aprovação:.....: {:.2f}\n".format(global_solucion))
    return global_solucion


def media2Semestre(challenge, media_checkp, global_solu):
    media_semestre = (0.4 * ((media_checkp + challenge) / 2)) + (0.6 * global_solu)
    print("Média do 2º Semestre..........:", media_semestre)
    return media_semestre


# mostrar aluno 1  FEITO
dadosDoAluno('A4', 'B4')
mostrarDisciplina('A1', 'C1')
media1Semestre('C4')
notasCp('E4', 'G4')
notasChallenge('I4', 'J4')
calculoGlobalSolut(media_cp, media_chall)
media2Semestre(media_chall, media_cp, global_solucion)

print("<>" * 50)
# mostrar aluno 2
dadosDoAluno('A5', 'B5')
mostrarDisciplina('A1', 'C1'"\n")
media1Semestre('C5')
notasCp('E5', 'G5')
notasChallenge('I5', 'J5')
calculoGlobalSolut(media_cp, media_chall)
media2Semestre(media_chall, media_cp, global_solucion)

print("<>" * 50)
# mostrar aluno 3
dadosDoAluno('A6', 'B6')
mostrarDisciplina('A1', 'C1'"\n")
media1Semestre('C6')
notasCp('E6', 'G6')
notasChallenge('I6', 'J6')
calculoGlobalSolut(media_cp, media_chall)
media2Semestre(media_chall, media_cp, global_solucion)

print("<>" * 50)
# mostrar aluno 4
dadosDoAluno('A7', 'B7')
mostrarDisciplina('A1', 'C1'"\n")
media1Semestre('C7')
notasCp('E7', 'G7')
notasChallenge('I7', 'J7')
calculoGlobalSolut(media_cp, media_chall)
media2Semestre(media_chall, media_cp, global_solucion)

print("<>" * 50)
# mostrar aluno 5
dadosDoAluno('A8', 'B8')
mostrarDisciplina('A1', 'C1'"\n")
media1Semestre('C8')
notasCp('E8', 'G8')
notasChallenge('I7', 'J7')
calculoGlobalSolut(media_cp, media_chall)
media2Semestre(media_chall, media_cp, global_solucion)
