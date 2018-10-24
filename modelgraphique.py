#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 19:41:49 2018
@author: samir
"""
import sqlite3
from tkinter import Tk, StringVar, Label, Radiobutton
from functools import partial

connexion = sqlite3.connect('choixecole.db')#On ouvre la base de donnée
curseur = connexion.cursor() #execute les commandes sql

class ChoixEcole:
    def __init__(self):
        Spe=[]#liste des spécialité
        Ecole=[]#Liste des ecoles
        Alternance=["non ","oui","n'importe"]
        self.root = Tk()
        self.var_choix = StringVar(self.root,)
        self.var_alternance=StringVar(self.root,)
        label_ecole = Label(self.root, text='Ecole :' + self.var_choix.get())
        def specialite():
            """Nous revoie toutes les spécialité disponible sous forme d'une liste de tuples"""
            curseur.execute("SELECT Nom FROM Specialite")
            specialite = curseur.fetchall() #resultats de la commande
            for specialite in specialite:
                Spe.append(specialite[0]) #apprend les specialité dans la table spe
            return Spe
        
        
        Spe=specialite()
        def filtre(specialiteid,alternanceid):
            Ecole=[]
            if alternanceid==3:
                curseur.execute("SELECT Nom FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? and IdAlternance=?",(specialiteid,0))
                ecole = curseur.fetchall() #resultat de la commande
                for ecole in ecole:
                    Ecole.append(ecole[0]) #appends les ecoles en fonction de la  specialité 
                curseur.execute("SELECT Nom FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? and IdAlternance=?",(specialiteid,1))
                ecole = curseur.fetchall() #resultat de la commande
                for ecole in ecole:
                    Ecole.append(ecole[0]) #appends les ecoles en fonction de la  specialité 
                return Ecole
            else :  
                curseur.execute("SELECT Nom FROM EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id WHERE IdSpe=? and IdAlternance=?",(specialiteid,alternanceid))
                ecole = curseur.fetchall() #resultat de la commande
                for ecole in ecole:
                    Ecole.append(ecole[0]) #appends les ecoles en fonction de la  specialité 
                    return Ecole
        
        def update_label(label,Ecole):
            s=""
            choixspe = self.var_choix.get()
            choixalt = self.var_alternance.get()
            for i in range(len(Alternance)):
                if str(choixalt)==str(Alternance[z]):
                    choixalt=str(choixalt)
            if str(choixalt)==str(Alternance[0]):
                for i in range(len(Spe)):
                    
                    if str(choixspe)==str(Spe[i]):
                        Ecole=filtre(i+1,0)
                
            elif str(choixalt)==str(Alternance[1]) :
                for i in range(len(Spe)):
                    if str(choixspe)==str(Spe[i]):
                        Ecole=filtre(i+1,1)
            elif str(choixalt)==str(Alternance[2]):
                for i in range(len(Spe)):
                    if str(choixspe)==str(Spe[i]):
                        Ecole=filtre(i+1,3)
                
            for k in range(len(Ecole)):
                    s=s+"\n"+str(Ecole[k])
                
                
            label.config(text='Ecole :' + s)
            
        for z in range(len(Alternance)):
            choix_2=Radiobutton(self.root,variable=self.var_alternance,text=Alternance[z], value=Alternance[z],command=partial(update_label,label_ecole,Ecole))
            choix_2.grid(row=z+1, column=2,padx=20,sticky="w")    
        for i in range(len(Spe)):
            choix_1 = Radiobutton(self.root,variable=self.var_choix,text=str(Spe[i]), value=Spe[i],command=partial(update_label,label_ecole,Ecole))
            choix_1.grid(row=i+1, column=1,sticky="w")
       
        label_ecole.grid(row=1, column=3,padx =40)
        label_spe = Label(self.root, text='Specialité :' )
        label_alt = Label(self.root, text='Alternance :' )
        label_spe.grid(row=0, column=1)
        label_alt.grid(row=0, column=2)
    
       
        self.root.mainloop()
       
        
    
    
if __name__ == '__main__':
    ChoixEcole()