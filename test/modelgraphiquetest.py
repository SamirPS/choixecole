#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 19:41:49 2018
@author: samir
"""
from tkinter import Tk,StringVar, Label, Radiobutton,Entry,filedialog
import modeltest

class ChoixEcole:
   
    
    def __init__(self):
        """Initialise l'application"""
 
        # self.root représente la fenêtre dans la quelle se déroule notre application
         
        self.root = Tk()
        self.root.title("ChoixEcole TSI") # Ajout d'un titre 
       
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
        
        
        self.Specialite=[]#liste des spécialité
        self.Ecole=[]
        self.Commune=[]
        self.Concours=[]
        self.Coeffccs=[]
        self.Coeffccp=[]
        
        
        self.entry_maths = Entry(self.root, textvariable=self.var_maths)
        self.entry_physique = Entry(self.root, textvariable=self.var_physique)
        self.entry_si = Entry(self.root, textvariable=self.var_si)
        self.entry_info = Entry(self.root, textvariable=self.var_info)
        self.entry_francais = Entry(self.root, textvariable=self.var_francais)
        self.entry_anglais = Entry(self.root, textvariable=self.var_anglais)
        
        
        self.label_maths=Label(self.root,text='Rentre ta moyenne de Maths')
        self.label_physique=Label(self.root,text='Rentre ta moyenne de Physique')
        self.label_si=Label(self.root,text='Rentre ta moyenne de SI')
        self.label_info=Label(self.root,text='Rentre ta moyenne en Informatique')
        self.label_francais=Label(self.root,text='Rentre ta moyenne de Francais')
        self.label_anglais=Label(self.root,text='Rentre ta moyenne d"Anglais')
        self.label_ecole = Label(self.root, text='Ecole :')
        self.label_commune = Label(self.root, text='Commune :')
        self.label_spe = Label(self.root, text='Specialité :' )
        self.label_concours=Label(self.root,text='Concours:')
        
        self.basededonnee=filedialog.askopenfilename(
        title="Ouvrir un fichier",
        filetypes=[('SQL Files','.db')])
        modeltest.file(self.basededonnee)
        
        self.Coeffccs=modeltest.renvoie_coeffccs()
        self.Coeffccp=modeltest.renvoie_coeffccp()
        self.Specialite=modeltest.renvoie_specialite()
        self.Commune=modeltest.renvoie_commune()
        self.Concours=modeltest.renvoie_concours()
        
        
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
        
        self.root.mainloop()

        
        
        
    def update_label(self):
            """Met a jour les écoles en fonction de la case qui est cochée"""
            text=""
            communeid=""
            concoursid=""
            NoteMode=(float(self.entry_maths.get())+float(self.entry_maths.get()))/2
            NoteMaths=float(self.entry_maths.get())
            NotePhysique=float(self.entry_physique.get())
            NoteSi=float(self.entry_si.get())
            NoteFrancais=float(self.entry_francais.get())
            NoteAnglais=float(self.entry_anglais.get())
            NoteInfo=float(self.entry_info.get())
            Note=0
            Ecole1=[]
            Ecole2=[]
                
            for d in range(len(self.Commune)):
                if self.var_commune.get()==self.Commune[d]:
                    communeid=self.Commune[d]
            
                    
            for e in range(len(self.Concours)):
                if self.var_concours.get()==self.Concours[e]:
                    concoursid=self.Concours[e]
            
            if concoursid=="CCP" :
               
                Note=(self.Coeffccp[0]*NoteMode+self.Coeffccp[1]*NoteMaths+self.Coeffccp[2]*NotePhysique+self.Coeffccp[3]*NoteSi+self.Coeffccp[4]*NoteFrancais+self.Coeffccp[5]*NoteAnglais+self.Coeffccp[6]*NoteInfo)/sum(self.Coeffccp)
                Note=round(Note,1)
                print(Note)
                
            if concoursid=="CCS":
                Note=(self.Coeffccs[0]*NoteMode+self.Coeffccs[1]*NoteMaths+self.Coeffccs[2]*NotePhysique+self.Coeffccs[3]*NoteSi+self.Coeffccs[4]*NoteFrancais+self.Coeffccs[5]*NoteAnglais+self.Coeffccs[6]*NoteInfo)/sum(self.Coeffccs)
                Note=round(Note,1)
            
                
    
            for f in range (len(self.Specialite)):
                if concoursid=="Peu importe":
                    if self.var_choix.get()==self.Specialite[f]:
                         Note=(self.Coeffccs[0]*NoteMode+self.Coeffccs[1]*NoteMaths+self.Coeffccs[2]*NotePhysique+self.Coeffccs[3]*NoteSi+self.Coeffccs[4]*NoteFrancais+self.Coeffccs[5]*NoteAnglais+self.Coeffccs[6]*NoteInfo)/sum(self.Coeffccs)
                         Note=round(Note,1)
                         Ecole1=modeltest.filtre(f+1,communeid,concoursid,Note)
                         Note=(self.Coeffccp[0]*NoteMode+self.Coeffccp[1]*NoteMaths+self.Coeffccp[2]*NotePhysique+self.Coeffccp[3]*NoteSi+self.Coeffccp[4]*NoteFrancais+self.Coeffccp[5]*NoteAnglais+self.Coeffccp[6]*NoteInfo)/sum(self.Coeffccp)
                         Note=round(Note,1)
                         Ecole2=modeltest.filtre(f+1,communeid,concoursid,Note)
                         self.Ecole=Ecole1+Ecole2
                         self.Ecole=list(set(self.Ecole))
                         
                    break
                else:
                    if self.var_choix.get()==self.Specialite[f]:
                        self.Ecole=modeltest.filtre(f+1,communeid,concoursid,Note)
                    break
             
            
            if concoursid=="Peu importe":
                for g in range(len(self.Ecole)):
                    text=text+"\n"+self.Ecole[g][0]+" "+self.Ecole[g][1]
            else:
                for h in range(len(self.Ecole)):
                    text=text+"\n"+self.Ecole[h][0]
                
                    
            self.label_ecole.config(text="Ecole :" + text)
            
            
        
    
    
if __name__ == '__main__':
    ChoixEcole()
