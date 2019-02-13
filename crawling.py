# Import des Modules
from tkinter import Tk, Label, Entry, Button, Toplevel, Text, Listbox, messagebox, END
from tkinter.filedialog import *
import re
import csv
import urllib
from urllib import request
from urllib.parse import urlparse
import os
import smtplib
import re

# Création de la Fenetre principale et titre
root = Tk()
root.title("Web Target")

'''
*****************************
*Fonction fenetre principale*
*****************************
'''

# Fonction de Lecture du Fichier
def readFile():
    fileName = askopenfilename(title="Ouvrir votre document", filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
    file = open(fileName, "r")
    content = csv.reader(file, delimiter=";", quotechar='"')
    nombre = 0
    for line in content:
        listboxMail.insert(nombre, line)
        nombre = nombre + 1
    file.close()

# Fonction de Lecture d'une URL
def readUrl():
    url = entryUrl.get()  # Récupération de l'Url
    urlSet = urlparse(url).hostname
    if url == "": # Si l'URL est vide, renvoie message d'erreur sinon, suite
        messagebox.showinfo("Erreur", "L'URL saisie n'est pas valide.")
    else: #Suite, vérification du ping, si ping, adresse valide, récupération mail
        responseUrl = os.system("ping -c 1 " + urlSet)
        if responseUrl == 0:
            openUrl = urllib.request.urlopen(url)
            with openUrl as data:
                data = data.read()
                data = str(data)
                mailtoCount = data.count("mailto:")
                i = 0

                while i != mailtoCount:
                    i = i + 1
                    value = data.find("mailto:")
                    data = data[value + 7:]
                    dataMail = data.find('"')
                    dataMail = data[0:dataMail]
                    listboxMail.insert(i, dataMail)
        elif responseUrl == 1: #Si URL ping pas, erreur
            messagebox.showinfo("Erreur", "L'URL saisie n'est pas valide.")

# Fonction de suppression des doublons
def delDouble():
    the_list = []
    the_list.extend(listboxMail.get(0, END))
    the_list = list(set(the_list))
    taille = the_list.__len__()
    listboxMail.delete(0, END)
    for i in range(0, taille):
        listboxMail.insert(i, the_list[i])


# Fonction de suppression des adresses non valides
def delete_wrong():
    the_list = []
    the_list.extend(listboxMail.get(0, END))
    taille = the_list.__len__()
    listboxMail.delete(0, END)
    for i in range(0, taille):
        if "@" in the_list[i] and ((".com" in the_list[i][-4:]) or (".fr" in the_list[i][-3:])):
            listboxMail.insert(i, the_list[i])
        for letters in the_list[i]:
            if "@" in letters and ((".com" in letters[-4:]) or (".fr" in letters[-3:])):
                listboxMail.insert(i, the_list[i])


# Fonction d'envoie de mail avec ls arugments nécessaires
def send_my_mail(listboxMail, sendMail, entry_sender_mail, entry_sender_pass, message_mail):
    list_mail = listboxMail.get(0, END)
    login = entry_sender_mail.get()
    password = entry_sender_pass.get()
    text = message_mail.get("1.0", 'end-1c').encode('utf-8')
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(login, password)
    server.sendmail(login, list_mail, text)
    server.quit()
    exit_mail(sendMail)
    messagebox.showinfo("Statut", "Le message a bien été envoyé a votre liste !")

# Fonction de fermeture de la fenetre d'envoie de mail
def exit_mail(sendMail):
    sendMail.destroy()

# Fonction de la fenetre d'envoie de mail ET interface
def send_mail():
    sendMail = Toplevel()
    sendMail.title("Envoyer Mail")

    message_mail = Text(sendMail, height=10)
    message_mail.grid(column=0, row=2, columnspan=2)

    label_sender_mail = Label(sendMail, text="Adresse Mail Exépediteur : ")
    label_sender_mail.grid(column=0, row=3)
    entry_sender_mail = Entry(sendMail, width=60)
    entry_sender_mail.grid(column=1, row=3)

    label_sender_pass = Label(sendMail, text="Mot de Passe Expéditeur : ")
    label_sender_pass.grid(column=0, row=4)
    entry_sender_pass = Entry(sendMail, show="*", width=60)
    entry_sender_pass.grid(column=1, row=4)

    button_send_mail = Button(sendMail, text="Envoyer le mail", command=lambda: (send_my_mail(listboxMail, sendMail, entry_sender_mail, entry_sender_pass, message_mail)))
    button_send_mail.grid(column=0, row=5)

    button_exit_mail = Button(sendMail, text="Quitter", command=lambda: exit_mail(sendMail))
    button_exit_mail.grid(column=1, row=5)



# Fonction de fermeture de la fenetre
def exitWindowMain():
    root.destroy()

'''
*********************
*Interface Graphique*
*Fenetre principale *
*********************
'''

# Affichage du mot Menu
labelMenu = Label(root, text="==== MENU ====")
labelMenu.grid(column=1, row=0)

# Séléction d'un fichier
labelFile = Label(root, text="Ouvrir un fichier : ")
labelFile.grid(column=0, row=1)
buttonFile = Button(root, text="Fichier", command=readFile)
buttonFile.grid(column=1, row=1)

# Séléction d'une URL
labelUrl = Label(root, text="Votre URL : ")
labelUrl.grid(column=0, row=2)
entryUrl = Entry(root, width=30)
entryUrl.grid(column=1, row=2)
buttonUrl = Button(root, text="Continuer", command=readUrl)
buttonUrl.grid(column=2, row=2)

# Liste des mails vide au début
listboxMail = Listbox(root, width=30)
listboxMail.grid(column=1, row=3)

# Label des Options (Il sert surtout à équilibrer la fenetre :) )
label_options = Label(root, text="Options : ")
label_options.grid(column=0, row=4)

# Bouton validité des mails
buttonDelDouble = Button(root, text="Validité", command=delete_wrong)
buttonDelDouble.grid(column=1, row=4)

# Bouton Suppression Doublon
buttonDelDouble = Button(root, text="Dédoublonner", command=delDouble)
buttonDelDouble.grid(column=2, row=4)

# Bouton envoie a tous les Users
buttonSendMailAll = Button(root, text="Envoyer à toute la liste", command=send_mail)
buttonSendMailAll.grid(column=1, row=5)

# Bouton de Femeture
buttonExit = Button(root, text="Quitter", command=exitWindowMain)
buttonExit.grid(column=2, row=10)

root.mainloop()
