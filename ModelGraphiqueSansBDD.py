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
        Ecole=["SamSam","Besnier","MathsSchool"]#Liste des ecoles
        self.root = Tk() # On créer une fenetre
        self.var_choix = StringVar(self.root,)
        label_ecole = Label(self.root, text='Ecole :' + self.var_choix.get())
        
        
        def update_label(label):
            """Met a jour le label en fonction de la case qui est cochée"""
            text=""
            for i in range(len(Ecole)):
                if str(self.var_choix.get())==str(Specialité[i]):
                    text=text+"\n"+str(Ecole[i])
            label.config(text='Ecole :' + text)
              
        
        for i in range(len(Specialité)):
            choix_1 = Radiobutton(self.root,variable=self.var_choix,text=str(Specialité[i]), value=Specialité[i],command=partial(update_label,label_ecole))
            choix_1.grid(row=i+1, column=1,sticky="w")
       
        label_ecole.grid(row=1, column=3,padx =40)
        label_spe = Label(self.root, text='Specialité :' )
        label_spe.grid(row=0, column=1)
    
       
        self.root.mainloop()
       
        
    
    
if __name__ == '__main__':
    ChoixEcole()
