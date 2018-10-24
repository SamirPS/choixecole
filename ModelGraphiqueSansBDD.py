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
        Specialité=["Informatique","Sport","Maths"]#liste des spécialité
        Ecole=[("TelecomSudParis","Informatique"),("TsP","Sport"),("Samsam","Sport"),("Samsam","Maths")]#Liste des ecoles
        self.root = Tk() # On créer une fenetre
        self.var_choix = StringVar(self.root,)
        label_ecole = Label(self.root, text='Ecole :' + self.var_choix.get())
        
        
        def update_label(label):
            """Met a jour le label en fonction de la case qui est cochée"""
            Z=[]
            text=""
            for i in range (len(Ecole)):
                Z=Ecole[i]
                if str(self.var_choix.get())==str(Z[1]):
                    text=text+"\n"+str(Z[0])
            label.config(text="Ecole" + text)
                    
        
        for i in range(len(Specialité)):
            choix_1 = Radiobutton(self.root,variable=self.var_choix,text=str(Specialité[i]), value=Specialité[i],command=partial(update_label,label_ecole))
            choix_1.grid(row=i+1, column=1,sticky="w")
       
        label_ecole.grid(row=1, column=3,padx =40)
        label_spe = Label(self.root, text='Specialité :' )
        label_spe.grid(row=0, column=1)
    
       
        self.root.mainloop()
        
    
    
if __name__ == '__main__':
    ChoixEcole()
