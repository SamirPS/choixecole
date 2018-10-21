#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 19:41:49 2018

@author: samir
"""
import sqlite3
from tkinter import *
Spe=[]#liste des spécialité
Ecole=[]#Liste des ecoles
connexion = sqlite3.connect('choixecole.db')#On ouvre la base de donnée
curseur = connexion.cursor() #execute les commandes sql

def specialité(table):
    """Nous revoie toutes les spécialité disponible sous forme d'une liste de tuples"""
    curseur.execute("SELECT Nom FROM Specialite")
    specialite = curseur.fetchall() #resultats de la commande
    for specialite in specialite:
        table.append(specialite) #apprend les specialité dans la table spe
    return table


def choix(Ecole):
    if str(var_choix.get())=="Informatique":
        Ecole=filtre(Ecole,1)
        return Ecole
    elif str(var_choix.get())=="Aeronautique":
        Ecole=filtre(Ecole,2)
        return Ecole
    if str(var_choix.get())=="BTP":
        Ecole=filtre(Ecole,3)
        return Ecole
    else:
        return Ecole
    
def filtre(table,specialiteid):
    curseur.execute("SELECT Nom FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=?",(specialiteid,))
    ecole = curseur.fetchall() #resultat de la commande
    for ecole in ecole:
        table.append(ecole) #appends les ecoles en fonction de la  specialité 
    return table

Spe=specialité(Spe)

fenetre = Tk()

var_choix = StringVar()
for i in range(len(Spe)):
    choix_1 = Radiobutton(fenetre, text=str(Spe[i]), variable=var_choix, value=Spe[i])
    choix_1.pack()


bouton_choix= Button(fenetre, text="Clic ici", command=choix(Ecole))
bouton_choix.pack()
bouton_quitter = Button(fenetre, text="puis ici ", command=fenetre.quit)
bouton_quitter.pack()
fenetre.mainloop()

Ecole=choix(Ecole)
print(Ecole)


fenetre2 = Tk()
if len(Ecole)==0:
    champ_label = Label(fenetre2, text="pas d'ecole trouve")
    champ_label.pack()
else :
    for i in range(len(Ecole)) :
        champ_label = Label(fenetre2, text=str(Ecole[i]))
        champ_label.pack()
fenetre.mainloop()
