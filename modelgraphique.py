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

class ChoixEcole:
    def specialite():
        """Nous revoie toutes les spécialité disponible sous forme d'une liste de tuples"""
        curseur.execute("SELECT Nom FROM Specialite")
        specialite = curseur.fetchall() #resultats de la commande
        for specialite in specialite:
            Spe.append(specialite[0]) #apprend les specialité dans la table spe
        return Spe
    Spe=specialite()
    
    
    def filtre(specialiteid):
        curseur.execute("SELECT Nom FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=?",(specialiteid,))
        ecole = curseur.fetchall() #resultat de la commande
        for ecole in ecole:
            Ecole.append(ecole[0]) #appends les ecoles en fonction de la  specialité 
        return Ecole
    
    def choix(Ecole):
        for i in range(len(Spe)):
            if str(self.var_choix.get())==str(Spe[i]):
                Ecole=filtre(Ecole,i+1)
        return Ecole
    
    def __init__(self):
        self.root = Tk()
        self.var_choix = StringVar()
        for i in range(len(Spe)):
            choix_1 = Radiobutton(self.root, text=str(Spe[i]), variable=self.var_choix, value=Spe[i])
            choix_1.pack()
        bouton_quitter = Button(self.root, text="clique ici", command=self.choix)
        bouton_quitter.pack()
        self.root.mainloop()
    
    
if __name__ == '__main__':
    ChoixEcole()
