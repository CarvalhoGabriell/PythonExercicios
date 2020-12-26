numeros_player = [1,2,3,4,5,6,7,8,9,10,11]
nomes = ["Goleiro", "Lateral Direito", "Zagueiro canhoto", "Zagueiro Destro", "Volante", "Laterla Esquerdo", "Ponta Esquerda", "Armador Suporte", "CentroAvante", "Armador central", "Ponta Direita"]
# da pra concatenar quantas lista vc quiser
for num, nome in zip(numeros_player, nomes):
    print(num, nome)