#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 19:41:49 2018
@author: samir
"""
from tkinter import Tk, StringVar, Label, Radiobutton
from functools import partial

class ChoixEcole:
   
    
    def __init__(self):
        """Initialise l'application"""
 
        # self.root représente la fenêtre dans la quelle se déroule notre application
         
        self.root = Tk() 
        """Initialise les variables"""
        
        self.var_choix = StringVar()
        self.Specialité=["Informatique","Sport","Maths"]#liste des spécialité
        self.Ecole=[("TelecomSudParis","Informatique"),("TsP","Sport"),("Samsam","Sport"),("Samsam","Maths")]#Liste des ecoles
        self.label_ecole = Label(self.root, text='Ecole :')
        
        """On affiche les cases a cocher"""
        
        for i in range(len(self.Specialité)):
            choix_1 = Radiobutton(self.root,variable=self.var_choix,text=self.Specialité[i], value=self.Specialité[i],command=partial(self.update_label))
            choix_1.grid(row=i+1, column=1,sticky="w")
        
        """On place les élèments """
        
        self.label_ecole.grid(row=1, column=3,padx =40)
        self.label_spe = Label(self.root, text='Specialité :' )
        self.label_spe.grid(row=0, column=1)
    
       
        self.root.mainloop()
    def update_label(self):
            """Met a jour les écoles en fonction de la case qui est cochée"""
            Z=[]
            text=""
            for i in range (len(self.Ecole)):
                Z=self.Ecole[i]
                if self.var_choix.get()==Z[1]:
                    text=text+"\n"+Z[0]
            self.label_ecole.config(text="Ecole" + text)
        
    
    
if __name__ == '__main__':
    ChoixEcole()
