#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 19:41:49 2018
@author: samir
"""
from tkinter import Tk,StringVar, Label, Radiobutton
import modeltest

class ChoixEcole:
   
    
    def __init__(self):
        """Initialise l'application"""
 
        # self.root représente la fenêtre dans la quelle se déroule notre application
         
        self.root = Tk() 
        self.root.title("ChoixEcole") # Ajout d'un titre 
        """Initialise les variables"""
       
        self.var_choix = StringVar(self.root)
        self.var_commune=StringVar(self.root)
        self.var_concours=StringVar(self.root)
        self.Specialité=[]#liste des spécialité
        self.Ecole=[]#Liste des ecoles
        self.Commune=[]
        self.Concours=[]
        self.label_ecole = Label(self.root, text='Ecole :')
        self.label_commune = Label(self.root, text='Commune :')
        self.label_spe = Label(self.root, text='Specialité :' )
        self.label_concours=Label(self.root,text='Concours:')
        self.Specialité=modeltest.renvoie_specialite()
        self.Commune=modeltest.renvoie_commune()
        self.Concours=modeltest.renvoie_concours()
        """On affiche les cases a cocher"""
        for d in range(len(self.Commune)):
            choix_2 = Radiobutton(self.root,variable=self.var_commune,text=self.Commune[d], value=self.Commune[d],command=self.update_label)
            choix_2.grid(row=d+1, column=2,sticky="w")
        
        for e in range(len(self.Concours)):
            choix_3= Radiobutton(self.root,variable=self.var_concours,text=self.Concours[e], value=self.Concours[e],command=self.update_label)
            choix_3.grid(row=e+1, column=3,sticky="w")
            
        for a in range(len(self.Specialité)):
            choix_1 = Radiobutton(self.root,variable=self.var_choix,text=self.Specialité[a], value=self.Specialité[a],command=self.update_label)
            choix_1.grid(row=a+1, column=1,sticky="w")
            
            
        
        
        """On place les élèments """
        
        self.label_ecole.grid(row=1, column=4,padx =40)
        self.label_spe.grid(row=0, column=1)
        self.label_commune.grid(row=0,column=2)
        self.label_concours.grid(row=0,column=3)
        self.root.mainloop()
         
         
    def update_label(self):
            """Met a jour les écoles en fonction de la case qui est cochée"""
            text=""
            communeid=""
            concoursid=""
            
            for  k in range(len(self.Commune)):
                if self.var_commune.get()==self.Commune[k]:
                    communeid=self.Commune[k]
            
                    
            for z in range(len(self.Concours)):
                if self.var_concours.get()==self.Concours[z]:
                    concoursid=self.Concours[z]
                    
                         
            for b in range (len(self.Specialité)):
                if self.var_choix.get()==self.Specialité[b]:
                    self.Ecole=modeltest.filtre(b+1,communeid,concoursid)
                    
            if concoursid=="Peu importe":
                for c in range(len(self.Ecole)):
                    text=text+"\n"+self.Ecole[c][0]+" "+self.Ecole[c][1]
            else:
                for c in range(len(self.Ecole)):
                    text=text+"\n"+self.Ecole[c][0]
                    
            self.label_ecole.config(text="Ecole :" + text)
            
            
        
    
    
if __name__ == '__main__':
    ChoixEcole()
