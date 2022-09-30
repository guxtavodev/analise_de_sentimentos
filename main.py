# Imports

from sklearn.svm import LinearSVC

from sklearn.metrics import accuracy_score

# Exemplos de situações

# 1 - Tem pergunta positiva?

# 2 -Tem palavra negativa?

# 3 - Tem a palavra MAS?

# 4 - Tem mais palavra positiva que negativa?

# 5 - Tem mais palavra negativa que positiva?

# 6 - Tem reticencias?

feliz = [1, 0, 0, 1, 0, 0]

feliz2 = [1,1,1,1,0,1]

feliz3 = [1,1,0,1,0,0]

feliz4 = [1,0,1,1,0,1]

feliz5 = [0,1,1,0,1,0]

triste = [0,1,0,0,1,1]

triste2 = [1,1,1,0,1,0]

triste3 = [0,1,0,1,0,1]

triste4 = [1,1,0,0,1,1]

triste5 = [1,0,1,1,0,0]

# Listas de palavras boas e ruins

palavrasBoas =[

	"Ótimo",	"Bom",

	"Kkk",

	"Oiee",

	"Hii",

	"Noooossa",

	"hahaha",

	"top",

	"KKKKK",

	"mt bomm",

	"good",

	"ksksks"

]

palavrasRuins = [

	"Hm",

	"Oi",

	"Diga",

	"...",

	"Mds",

	"Plmds",

	"K",

	"Ruim",

	"não",

	"odiei",

	"Hm?",

	"E?",

	"Ah",

	"ata",

	"aff",

	"plmds"

]

# Treinamento etc.

treino_x = [feliz, feliz2, feliz3, feliz4, feliz5, triste, triste2, triste3, triste4, triste5]

treino_y = [0,0,0,0,0,1,1,1,1,1]

# Importando...

from sklearn.svm import LinearSVC

modelo = LinearSVC()

modelo.fit(treino_x, treino_y)

# Loop para identificar as palavras.

def AcharPalavras(frase):

	# Frase já fatiada

	fraseFatiada = frase.split()

	# Numero de palavras

	numeroDePalavras = len(fraseFatiada)

	positivas = [] # Palavras positivas

	negativas = [] # Palavras negativas

	mas = 0 # Tem a palavra Mas? #

	prg_p = 0 # Tem pergunta positiva?

	prg_n = 0 # Tem pergunta negativa?

	p_n = 0 # Mais palavras positivas que negativa #

	n_p = 0 # Mais palavras negativas que positivas #

	tem_ret = 0 # Tem ... ? #

	vezes = 0 # Quantidade de vezes que o código foi repetido

	

	for item in fraseFatiada:

		if item == "mas," or item == "Mas" or item == "Mas," or item == "mas": # Verifica se na frase existe a palavra => MAS

			mas = 1

		if "..." in item:

			tem_ret = 1

		

		

		if vezes == numeroDePalavras:

			return

		else:

			for i in palavrasBoas:

				if item.replace(",", "").replace(".", "") == i.lower():

					positivas.append(item.replace(",","").replace(".", ""))

	for item in fraseFatiada:

		if vezes == numeroDePalavras:

			break

		else:

			for i in palavrasRuins:

				if item.replace(",", "").replace(".","") == i.lower():

					negativas.append(item.replace(",", "").replace(".",""))

					

			

		vezes+=1

	# Aqui começa o preenchimento dos testes.

	if len(positivas) > 0:

		prg_p = 1

	if len(negativas) > 0:

		prg_n = 1

	if len(positivas) > len(negativas):

		p_n = 1

	else:

		n_p = 1

	

	# Dados que foram preenchidos de acordo com a frase.

	pes = [prg_p, prg_n, mas, p_n, n_p, tem_ret]

	return pes

		

while True:

	frasei = input("Qual a frase?: ")

# Variaveis novas para o predict

	frase = AcharPalavras(frasei)

	prev = modelo.predict([frase])[0]

# Tratamento das respostas

	print(prev)

	if prev == 1:

		print("Ele tá triste!")

	else:

		print("Ele tá feliz")

		

	quer = input("Quer continuar?: ")

	if quer == "sim" or quer == "s":

		pass

	else:

		break
