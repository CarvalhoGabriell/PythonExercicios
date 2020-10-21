from openpyxl import load_workbook

wb = load_workbook('Planilha.xlsx')
nomePlan = wb['Plan1']

sheet = wb.active

def dadosDoAluno(celua1, celual2) :

    celulas1 = sheet['A4': 'C4']
    for c1,c2, c3 in celulas1:
        print("{0:8} {1:8} {2:8}".format(c1.value,c2.value,c3.value))
    return

def notasCp (celula1, celual2):
    celulas = sheet['E4': 'G4']
    for c1,c2,c3 in celulas:
        nota1 = c1.value
        nota2 = c2.value
        nota3 = c3.value
        if (nota1 < nota2 and nota1 < nota3) :
            nota1 = 0
            media_cp = (nota2 + nota3) / 2
        elif (nota2 < nota1 and nota2 < nota3) :
            nota2 = 0
            media_cp = (nota1 + nota3) / 2
        elif (nota3 < nota2 and nota3 < nota1):
            nota3 = 0
            media_cp = (nota1 + nota2) / 2
        else:
            print("erro")
    print(media_cp)
    return media_cp

def notasChallenge(celula1, celula2):
    celulas2 = sheet['I4': 'J4']
    for c1,c2 in celulas2:
        challengNota1 = c1.value
        challengNota2 = c2.value
        media_chal = (challengNota1 +challengNota2)/2
    print(media_chal)
    return media_chal

global_solucion =( ((6 - (0.4 * 6))/ 0.6) - (0.4 * (media_cp +media_chal)/ 2) )/ 0.6
print("Nota no GB necessaria pra ficar com a media 6.....: {:.2f}".format(global_solucion))

