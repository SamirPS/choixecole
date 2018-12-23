#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 19:41:49 2018
@author: samir
"""
from tkinter import Tk,StringVar, Label, Radiobutton,Entry
import model
import tkinter.scrolledtext as tkscrolled
from tkinter.ttk import *


class ChoixEcole:
   
    
    def __init__(self):
        
        
        """Initialise l'application"""
 
         
        self.root = Tk()
        """Initialise les variables"""
        self.var_maths=StringVar(self.root)
        self.var_physique=StringVar(self.root)
        self.var_si=StringVar(self.root)
        self.var_info=StringVar(self.root)
        self.var_francais=StringVar(self.root)
        self.var_anglais=StringVar(self.root)
        self.var_choix = StringVar(self.root)
        self.var_commune=StringVar(self.root)
        self.var_concours=StringVar(self.root)
        
        """Initialise les listes""" 
        self.Specialite=[]#liste des spécialité
        self.ListeEcole=[]
        self.Commune=[]
        self.Concours=[]
        self.Coeffccs=[]
        self.Coeffccp=[]
        
        """Initialise les labels et entry"""
        vcmd = (self.root.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.entry_maths = Entry(self.root, textvariable=self.var_maths,validate = 'key', validatecommand = vcmd)
        self.entry_physique = Entry(self.root, textvariable=self.var_physique,validate = 'key', validatecommand = vcmd)
        self.entry_si = Entry(self.root, textvariable=self.var_si,validate = 'key', validatecommand = vcmd)
        self.entry_info = Entry(self.root, textvariable=self.var_info,validate = 'key', validatecommand = vcmd)
        self.entry_francais = Entry(self.root, textvariable=self.var_francais,validate = 'key', validatecommand = vcmd)
        self.entry_anglais = Entry(self.root, textvariable=self.var_anglais,validate = 'key', validatecommand = vcmd)
        
        
        self.label_maths=Label(self.root,text='Rentre ta moyenne de Maths')
        self.label_physique=Label(self.root,text='Rentre ta moyenne de Physique')
        self.label_si=Label(self.root,text='Rentre ta moyenne de SI')
        self.label_info=Label(self.root,text='Rentre ta moyenne en Informatique')
        self.label_francais=Label(self.root,text='Rentre ta moyenne de Francais')
        self.label_anglais=Label(self.root,text='Rentre ta moyenne d"Anglais')
        self.label_ecole=tkscrolled.ScrolledText(self.root, width=30, height=10)
        self.label_commune = Label(self.root, text='Commune :')
        self.label_spe = Label(self.root, text='Specialité :' )
        self.label_concours=Label(self.root,text='Concours:')
        self.ecolelabel=Label(self.root,text='Ecole:')
        
        self.Coeffccs=model.renvoie_coeffccs()
        self.Coeffccp=model.renvoie_coeffccp()
        self.Specialite=model.renvoie_specialite()
        self.Commune=model.renvoie_commune()
        self.Concours=model.renvoie_concours()
        
        self.label_ecole.configure(state="disabled")
        
        """On affiche les cases a cocher"""
        for a in range(len(self.Commune)):
            choix_2 = Radiobutton(self.root,variable=self.var_commune,text=self.Commune[a], value=self.Commune[a],command=self.update_label)
            choix_2.grid(row=a+1, column=3,sticky="w")
        
        for b in range(len(self.Concours)):
            choix_3= Radiobutton(self.root,variable=self.var_concours,text=self.Concours[b], value=self.Concours[b],command=self.update_label)
            choix_3.grid(row=b+1, column=4,sticky="w")
            
        for c in range(len(self.Specialite)):
            choix_1 = Radiobutton(self.root,variable=self.var_choix,text=self.Specialite[c], value=self.Specialite[c],command=self.update_label)
            choix_1.grid(row=c+1, column=2,sticky="w")
            
            
        
        
        """On place les élèments """
        
        self.label_maths.grid(row=0,column=1)
        self.label_physique.grid(row=2,column=1)
        self.label_si.grid(row=4,column=1)
        self.label_info.grid(row=6,column=1)
        self.label_francais.grid(row=8,column=1)
        self.label_anglais.grid(row=10,column=1)
        self.label_ecole.grid(row=1, column=5,padx =40)
        self.label_spe.grid(row=0, column=2)
        self.label_commune.grid(row=0,column=3)
        self.label_concours.grid(row=0,column=4)
        
        
        self.entry_maths.grid(row=1,column=1)
        self.entry_physique.grid(row=3,column=1)
        self.entry_si.grid(row=5,column=1)
        self.entry_info.grid(row=7,column=1)
        self.entry_francais.grid(row=9,column=1)
        self.entry_anglais.grid(row=11,column=1)
        
            
 
        self.label_ecole.grid(row=2, rowspan=8,column=5)  
        self.ecolelabel.grid(row=1,column=5)
        
        
        
        self.root.mainloop()

        
    def validate(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if(action=='1'):
            if text in '0123456789.-+':
                try:
                    float(value_if_allowed)
                    return True
                except ValueError:
                    return False
            else:
                return False
        else:
            return True  
    def update_label(self):
            text=""
            test=False
            NoteMode=self.entry_maths.get()+self.entry_maths.get()
            NoteMaths=self.entry_maths.get()
            NotePhysique=self.entry_physique.get()
            NoteSi=self.entry_si.get()
            NoteFrancais=self.entry_francais.get()
            NoteAnglais=self.entry_anglais.get()
            NoteInfo=self.entry_info.get()
            communeid=""
            concoursid=""
            Note=0
            Ecole1=[]
            Ecole2=[]  
            self.label_ecole.configure(state="normal")
            self.label_ecole.delete(0.7,'end');
            
        
            while  self.var_commune.get()=="" or  self.var_concours.get()=="" or  self.var_choix.get()=="":
                
                return self.ListeEcole
            while test==False:
                if NoteMode=="" or NoteMaths=="" or NotePhysique=="" or NoteSi=="" or NoteFrancais=="" or NoteAnglais=="" or NoteInfo=="":
                    test=False
                    return self.ListeEcole
                else :
                    NoteMode=(float(self.entry_maths.get())+float(self.entry_maths.get()))/2
                    NoteMaths=float(self.entry_maths.get())
                    NotePhysique=float(self.entry_physique.get())
                    NoteSi=float(self.entry_si.get())
                    NoteFrancais=float(self.entry_francais.get())
                    NoteAnglais=float(self.entry_anglais.get())
                    NoteInfo=float(self.entry_info.get())
                    test=True
                    break
                
            for d in range(len(self.Commune)):
                if self.var_commune.get()==self.Commune[d]:
                    communeid=self.Commune[d]
            
                    
            for e in range(len(self.Concours)):
                if self.var_concours.get()==self.Concours[e]:
                    concoursid=self.Concours[e]
            
            if concoursid=="CCP" :
               
                Note=(self.Coeffccp[0]*NoteMode+self.Coeffccp[1]*NoteMaths+self.Coeffccp[2]*NotePhysique+self.Coeffccp[3]*NoteSi+self.Coeffccp[4]*NoteFrancais+self.Coeffccp[5]*NoteAnglais+self.Coeffccp[6]*NoteInfo)/sum(self.Coeffccp)
                Note=round(Note,1)
                
            if concoursid=="CCS":
                Note=(self.Coeffccs[0]*NoteMode+self.Coeffccs[1]*NoteMaths+self.Coeffccs[2]*NotePhysique+self.Coeffccs[3]*NoteSi+self.Coeffccs[4]*NoteFrancais+self.Coeffccs[5]*NoteAnglais+self.Coeffccs[6]*NoteInfo)/sum(self.Coeffccs)
                Note=round(Note,1)
            
                
    
            for f in range (len(self.Specialite)):
                if concoursid=="Peu importe":
                    if self.var_choix.get()==self.Specialite[f]:
                         
                         Note=(self.Coeffccs[0]*NoteMode+self.Coeffccs[1]*NoteMaths+self.Coeffccs[2]*NotePhysique+self.Coeffccs[3]*NoteSi+self.Coeffccs[4]*NoteFrancais+self.Coeffccs[5]*NoteAnglais+self.Coeffccs[6]*NoteInfo)/sum(self.Coeffccs)
                         Note=round(Note,1)
                         Ecole1=model.filtre(f+1,communeid,concoursid,Note)
                         Note=(self.Coeffccp[0]*NoteMode+self.Coeffccp[1]*NoteMaths+self.Coeffccp[2]*NotePhysique+self.Coeffccp[3]*NoteSi+self.Coeffccp[4]*NoteFrancais+self.Coeffccp[5]*NoteAnglais+self.Coeffccp[6]*NoteInfo)/sum(self.Coeffccp)
                         Note=round(Note,1)
                         Ecole2=model.filtre(f+1,communeid,concoursid,Note)
                         self.ListeEcole=list(set(Ecole1+Ecole2))
                         
                         break
                else:
                    if self.var_choix.get()==self.Specialite[f]:
                        
                        self.ListeEcole=model.filtre(f+1,communeid,concoursid,Note)
                        break
             
           
            for h in range(len(self.ListeEcole)):
                text=text+"\n"+self.ListeEcole[h][0]+" "+self.ListeEcole[h][1]+" "+self.ListeEcole[h][2]
              
                
            self.label_ecole.insert(2.0,text)
            self.label_ecole.configure(state="disabled")
            
                
            
            
        
    
    
if __name__ == '__main__':
    ChoixEcole()
