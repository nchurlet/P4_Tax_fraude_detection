# -*-coding:UTF-8 -*


annee = input("Saisissez une année : ")
while (annee !='Q' and annee != 'q'):
	try :
		annee = int(annee)
		assert annee > 0
	except ValueError:
		print("N'entrez qu'une année ou Q pour quitter : ", ValueError)
	except AssertionError: 
		print("cette fonction ne traite pas les année négatives")
	else:
		quit = """ 
		print(annee)Entrez Q ou q pour quitter"""
		notBisextile = ("L'année ", annee, " n'est pas bisextile",quit)
		bisextile = ("L'année ", annee, " est  bisextile", quit)

		if annee % 4 == 0 :
			print(annee, " % 4 == 0")
			if annee % 400 == 0 :
				print(annee, " % 100 == 0 mais aussi ", annee, " % 400 == 0")
				print(bisextile)
			elif annee % 100 == 0 :
				print(annee, " % 100 == 0 mais ", annee, " % 400 != 0")
				print(notBisextile)
			else :
				print(annee, " % 4 == 0 mais ", annee, " % 400 != 0 ni à 100")
				print(bisextile)
		else : print (annee, " % 4 != 0", notBisextile)
	finally:
		annee = input("Saisissez une année : ")