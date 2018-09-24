import sys

#On définit les variables annee / mois / jour en tant qu'entier
annee = int(0)  # Annee en entier
mois = int(0)  # Mois en entier
jour = int(0)  # Jour en entier

#On crée la fonction pour obtenir le jour de la semaine d'une date X
def anneeMoisJour():
    # Recuperation des variables de la date entrée par l'utilisateur
    annee = int(input("Merci d'entrer l'année : "))
    mois = int(input("Merci d'entrer le mois (en chiffres) : "))
    jour = int(input("Merci d'entrer le jour : "))

    #On crée une boucle, tant que l'année est inférieur a 1581, ou différent de Octobre 1582 et un mois supérieur & 12 et jour supérieur a 31
    #Pour limiter les erreurs de saisie et le date du minimum (Octobre 1582) pour le bon fonctionnement de l'algorithme.
    #Ainsi, l'utilisateur est invité à resaisir les informations nécessaires jusqu'à ce qu'elles soient correctes.
    while (annee <= int(1581)) or (annee == int(1582) and mois < int(11)) or (mois > 12) or (jour > 31):
        print("")
        print("La date est invalide")
        annee = int(input("Merci d'entrer l'année : "))
        mois = int(input("Merci d'entrer le mois (en chiffres) : "))
        jour = int(input("Merci d'entrer le jour : "))

    # On récupèrer les deux derniers chiffres de l'année dans la variable anneeDeux, on type en string /
    # / On récupère les deux dernières valeur de l'année / on retype entier
    anneeDeux = str(annee)
    anneeDeux = anneeDeux[2:4]
    anneeDeux = int(anneeDeux)

    # On divise par 4 la valeur d'anneeDeux qu'on met dans la variable somme, on change le type de somme en typant en string / on garde que la valeur entière / typant entier
    #Puis on ajoute la valeur d'anneeDeux + la somme dans la variable somme
    somme = anneeDeux / int(4)
    somme = str(somme)
    somme = somme[0:2]
    somme = int(somme)
    somme = anneeDeux + somme

    # On ajoute a la variable somme, sa propre valeur et celle du jour
    somme = somme + jour

    # On analyse à quoi correspond le mois pour ajouter ajouter à somme la valeur équivalente
    # + 1 pour le mois de janvier / + 3 pour le mois de février ....
    if mois == 1:  # Janvier
        somme = somme + 0
    elif mois == 2:  # Février
        somme = somme + 3
    elif mois == 3:  # Mars
        somme = somme + 3
    elif mois == 4:  # Avril
        somme = somme + 6
    elif mois == 5:  # Mai
        somme = somme + 1
    elif mois == 6:  # Juin
        somme = somme + 4
    elif mois == 7:  # Juillet
        somme = somme + 6
    elif mois == 8:  # Aout
        somme = somme + 2
    elif mois == 9:  # Septembre
        somme = somme + 5
    elif mois == 10:  # Octobre
        somme = somme + 0
    elif mois == 11:  # Novembre
        somme = somme + 3
    elif mois == 12:  # Decembre
        somme = somme + 5

    # Si c'est une annee Bissextile ET (mois de Janvier OU mois de Février), on retire 1 à la somme
    if (annee % 400 == 0) and (mois == 1 or mois == 2):
        somme = somme - 1

    # On  type en string / on récupère les 2 premiers valeur / on retype en entier
    anneeSiecle = str(annee)
    anneeSiecle = anneeSiecle[0:2]
    anneeSiecle = int(anneeSiecle)

    # La valeur d'anneeSiecle permet d'ajouter une valeur correspondante à la variable somme
    if anneeSiecle == 16:  # + 6 si c'est dans les 1600
        somme = somme + 6
    elif anneeSiecle == 17:  # + 4 si c'est dans les 1700
        somme = somme + 4
    elif anneeSiecle == 18:  # + 2 si c'est dans les 1800
        somme = somme + 2
    elif anneeSiecle == 19:  # + 0 si c'est dans les 1900
        somme = somme + 0
    elif anneeSiecle == 20:  # + 6 si c'est dans les 2000
        somme = somme + 6
    elif anneeSiecle == 21:  # + 4 si c'est dans les 2100
        somme = somme + 4

    # On divise la somme par 7, on met cette valeur dans une nouvelle variable, "valeurJour"
    valeurJour = somme % 7

    #La nouvelle valeur dans la variable "valeurJour" permet de déterminer le jour de la semaine de la date entrée par l'utilisateur
    if valeurJour == 0:  # 0 = Dimanche
        leJour = "dimanche"
    if valeurJour == 1:  # 1 = Lundi
        leJour = "lundi"
    if valeurJour == 2:  # 2 = Mardi
        leJour = "mardi"
    if valeurJour == 3:  # 3 = Mercredi
        leJour = "mercredi"
    if valeurJour == 4:  # 4 = Jeudi
        leJour = "jeudi"
    if valeurJour == 5:  # 5 = Vendredi
        leJour = "vendredi"
    if valeurJour == 6:  # 6 = Samedi
        leJour = "samedi"

    #On renvoit la date de l'utilisateur et le jour de la semaine a l'aide de la varibale leJour
    print("Votre date du ", jour, "/", mois, "/", annee, " est un ", leJour)

    #On relance le programme si l'utilisateur souhaite entrer une nouvelle date
    print("")
    choix = print("Souhaitez-vous entrer une nouvelle date ? Oui/Non")
    choix = input()
    
    while (choix != "Oui") or (choix != "Non"):
        if choix == "Oui":
                anneeMoisJour()
        elif choix == "Non":
                sys.exit()
        print("Votre choix n'est pas valide !")
        print("Souhaitez-vous entrer une nouvelle date ? Oui / Non")
        choix = input()
    #ATTENTION, ici probleme, les 3 dernières lignes sont en haut !
    #Seul moyen pour que cela fonctionne correctement
        
anneeMoisJour()
