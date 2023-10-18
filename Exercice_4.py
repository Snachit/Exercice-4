chaine=input("entre votre chaine :")
sous_chaine=input("entrer votre sous chaine :")
n= chaine.find(sous_chaine)
if   n != -1:
    print("la sous_chaine",sous_chaine,"a ete trouver a la position",n,"dans la chaine")
else :
    print("La sous_chaine",sous_chaine,"est pas trouver")