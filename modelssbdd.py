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
        Spe=["Informatique","Sport","Maths"]#liste des spécialité
        Ecole=["SamSam","Besnier","MathsSchool"]#Liste des ecoles
        self.root = Tk()
        self.var_choix = StringVar(self.root,)
        label_ecole = Label(self.root, text='Ecole :' + self.var_choix.get())
        
        
        def update_label(label):
            s=""
            choixspe = self.var_choix.get()
            for i in range(len(Ecole)):
                if str(choixspe)==str(Spe[i]):
                    s=s+"\n"+str(Ecole[i])
            label.config(text='Ecole :' + s)
              
        
        for i in range(len(Spe)):
            choix_1 = Radiobutton(self.root,variable=self.var_choix,text=str(Spe[i]), value=Spe[i],command=partial(update_label,label_ecole))
            choix_1.grid(row=i+1, column=1,sticky="w")
       
        label_ecole.grid(row=1, column=3,padx =40)
        label_spe = Label(self.root, text='Specialité :' )
        label_spe.grid(row=0, column=1)
    
       
        self.root.mainloop()
       
        
    
    
if __name__ == '__main__':
    ChoixEcole()