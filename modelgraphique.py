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
def filtre(table,specialiteid):
    curseur.execute("SELECT Nom FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=?",(specialiteid,))
    ecole = curseur.fetchall() #resultat de la commande
    for ecole in ecole:
        table.append(ecole) #appends les ecoles en fonction de la  specialité 
    return table

Spe=specialité(Spe)

fenetre = Tk()

var_choix = StringVar()
choix_1 = Radiobutton(fenetre, text=str(Spe[0]), variable=var_choix, value=Spe[0])
choix_2= Radiobutton(fenetre, text=str(Spe[1]), variable=var_choix, value=Spe[1])
choix_3 = Radiobutton(fenetre, text=str(Spe[2]), variable=var_choix, value=Spe[2])

choix_1.pack()
choix_2.pack()
choix_3.pack()

bouton_quitter = Button(fenetre, text="Clic", command=choix(Ecole))
bouton_quitter.pack()
fenetre.mainloop()
Ecole=choix(Ecole)
print(Ecole)