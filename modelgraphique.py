#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 19:41:49 2018
@author: samir
"""
import sqlite3
from tkinter import Tk, StringVar, Label, Radiobutton,Canvas
from functools import partial

connexion = sqlite3.connect('choixecole.db')#On ouvre la base de donnée
curseur = connexion.cursor() #execute les commandes sql

class ChoixEcole:
    def __init__(self):
        Spe=[]#liste des spécialité
        Ecole=[]#Liste des ecoles
        self.root = Tk()
        self.var_choix = StringVar(self.root,)
        label_color = Label(self.root, text='Specialité :' + self.var_choix.get())
        def specialite():
            """Nous revoie toutes les spécialité disponible sous forme d'une liste de tuples"""
            curseur.execute("SELECT Nom FROM Specialite")
            specialite = curseur.fetchall() #resultats de la commande
            for specialite in specialite:
                Spe.append(specialite[0]) #apprend les specialité dans la table spe
            return Spe
        
        
        Spe=specialite()
        def filtre(specialiteid):
            Ecole=[]
            curseur.execute("SELECT Nom FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=?",(specialiteid,))
            ecole = curseur.fetchall() #resultat de la commande
            for ecole in ecole:
                Ecole.append(ecole[0]) #appends les ecoles en fonction de la  specialité 
            return Ecole
        
        
        def choix(Ecole): #Permet de trier les écoles
            testvar = self.var_choix.get()
            for i in range(len(Spe)):
                if str(testvar)==str(Spe[i]):
                    Ecole=filtre(i+1)
            return Ecole
        
        def update_label(label):
            Ecole=[]
            s=""
            testvar = self.var_choix.get()
            for i in range(len(Spe)):
                if str(testvar)==str(Spe[i]):
                    Ecole=filtre(i+1)
            for k in range(len(Ecole)):
                s=s+str(Ecole[k])+" \n "
                
            label.config(text='Spécialité :' + s)
            
            
        for i in range(len(Spe)):
            choix_1 = Radiobutton(self.root,variable=self.var_choix,text=str(Spe[i]), value=Spe[i],command=partial(update_label,label_color))
            choix_1.grid(row=i+1, column=1)
        label_color.grid(row=0, column=0)
       
        self.root.mainloop()
        print(Ecole)
       
        
    
    
if __name__ == '__main__':
    ChoixEcole()
