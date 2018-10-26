#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 19:41:49 2018
@author: samir
"""
from tkinter import Tk,StringVar, Label, Radiobutton
import model

class ChoixEcole:
   
    
    def __init__(self):
        """Initialise l'application"""
 
        # self.root représente la fenêtre dans la quelle se déroule notre application
         
        self.root = Tk() 
        self.root.title("ChoixEcole") # Ajout d'un titre 
        """Initialise les variables"""
       
        self.var_choix = StringVar(self.root)
        self.Specialité=[]#liste des spécialité
        self.Ecole=[]#Liste des ecoles
        self.label_ecole = Label(self.root, text='Ecole :')
        self.label_spe = Label(self.root, text='Specialité :' )
        self.Specialité=model.renvoie_specialite()
        """On affiche les cases a cocher"""
        
        for a in range(len(self.Specialité)):
            choix_1 = Radiobutton(self.root,variable=self.var_choix,text=self.Specialité[a], value=self.Specialité[a],command=self.update_label)
            choix_1.grid(row=a+1, column=1,sticky="w")
        
        """On place les élèments """
        
        self.label_ecole.grid(row=1, column=5,padx =40)
        self.label_spe.grid(row=0, column=1)
        self.root.mainloop()
         
         
    def update_label(self):
            """Met a jour les écoles en fonction de la case qui est cochée"""
            text=""
            
            for b in range (len(self.Specialité)):
                if self.var_choix.get()==self.Specialité[b]:
                    self.Ecole=model.filtre(b+1)
                    
                    
            for c in range(len(self.Ecole)):
                text=text+"\n"+self.Ecole[c][0]+"  "+self.Ecole[c][1]
            self.label_ecole.config(text="Ecole" + text)
            
            
        
    
    
if __name__ == '__main__':
    ChoixEcole()
