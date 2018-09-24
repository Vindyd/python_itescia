#Module sys pour fermer le programme à la demande
import sys

#Variables annee / mois / jour en tant qu'entier
annee = int(0)  # Annee en entier
mois = int(0)  # Mois en entier
jour = int(0)  # Jour en entier

#Fonction pour obtenir le jour de la semaine d'une date X
def anneeMoisJour():
    # Recuperation des variables de la date entrée par l'utilisateur
    annee = int(input("Merci d'entrer l'année : "))
    mois = int(input("Merci d'entrer le mois (en chiffres) : "))
    jour = int(input("Merci d'entrer le jour : "))

    #Boucle, tant que l'année est inférieur/égal a 1581, ou différent de Octobre 1582 et un mois supérieur & 12 et jour supérieur a 31
    #Pour limiter les erreurs de saisie et le date du minimum (Octobre 1582)
    while (annee <= int(1581)) or (annee == int(1582) and mois < int(11)) or (mois > 12) or (jour > 31):
        print("")
        print("La date est invalide")
        annee = int(input("Merci d'entrer l'année : "))
        mois = int(input("Merci d'entrer le mois (en chiffres) : "))
        jour = int(input("Merci d'entrer le jour : "))

    #Deux derniers chiffres de l'année dans variable anneeDeux, type en string / récupère les deux dernières valeur de l'année / retype entier
    anneeDeux = str(annee)
    anneeDeux = anneeDeux[2:4]
    anneeDeux = int(anneeDeux)

    #Divise par 4 la valeur d'anneeDeux dans somme, somme en type string / on garde que la valeur entière / type entier
    #Valeur d'anneeDeux + somme dans somme
    somme = anneeDeux / int(4)
    somme = str(somme)
    somme = somme[0:2]
    somme = int(somme)
    somme = anneeDeux + somme

    #Ajout valeur du jour dans somme
    somme = somme + jour

    #Analyse du mois pour ajouter ajouter à somme la valeur équivalente + 1 pour le mois de janvier / + 3 pour le mois de février ....
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

    #Si annee Bissextile ET (mois de Janvier OU mois de Février), -1 a somme
    if (annee % 400 == 0) and (mois == 1 or mois == 2):
        somme = somme - 1

    #Type string / 2 premieres valeurs / retype entier
    anneeSiecle = str(annee)
    anneeSiecle = anneeSiecle[0:2]
    anneeSiecle = int(anneeSiecle)

    #anneeSiecle permet d'ajouter une valeur correspondante à somme
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

    #Divise la somme par 7, dans une nouvelle variable "valeurJour"
    valeurJour = somme % 7

    #"valeurJour" permet de déterminer le jour de la semaine de la date entrée par l'utilisateur
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

    #Renvoit la date de l'utilisateur et le jour de la semaine a l'aide de la varibale leJour
    print("Votre date du ", jour, "/", mois, "/", annee, " est un ", leJour)

    #On relance le programme si l'utilisateur souhaite entrer une nouvelle date
    print("")
    choix = print("Souhaitez-vous entrer une nouvelle date ? Oui/Non")
    choix = input()

    #On crée une boucle pour limiter les erreurs de saisie
    while (choix != "Oui") or (choix != "Non"):
        if choix == "Oui":
            #Si l'utilisateur répond oui pour choisir une nouvelle date, on relance le programme
                anneeMoisJour()
        elif choix == "Non":
            #Si l'utilisateur répond non et n'a plus de date à rentrer, on ferme le programme
                sys.exit()
                
        print("Votre choix n'est pas valide !")
        print("Souhaitez-vous entrer une nouvelle date ? Oui / Non")
        choix = input()
    #ATTENTION, ici probleme, les 3 dernières lignes sont en haut !
    #Seul moyen pour que cela fonctionne correctement
        
anneeMoisJour()
