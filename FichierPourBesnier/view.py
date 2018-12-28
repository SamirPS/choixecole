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
    
    """Cette class est l'interface graphique du projet choix ecole"""
    
    def __init__(self):
        
        
        """Initialise l'application et change le titre"""
 
         
        self.root = Tk()
        self.root.title("ChoixEcole")
        
        """Initialise les variables"""
        self.var_maths=StringVar(self.root)
        self.var_physique=StringVar(self.root)
        self.var_si=StringVar(self.root)
        self.var_info=StringVar(self.root)
        self.var_francais=StringVar(self.root)
        self.var_anglais=StringVar(self.root)
        self.var_specialite = StringVar(self.root)
        self.var_commune=StringVar(self.root)
        self.var_concours=StringVar(self.root)
        
        """Initialise les labels et entry et vcmd est une fonction qui verifie si l'utilisateur entre les bonnes informations"""
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
        self.entry_ecole=tkscrolled.ScrolledText(self.root, width=30, height=10,)
        self.label_commune = Label(self.root, text='Commune :')
        self.label_spe = Label(self.root, text='Specialité :' )
        self.label_concours=Label(self.root,text='Concours:')
        self.label_ecole=Label(self.root,text='Ecole:')
        
        """Initalise les listes en utilisant les fonction du fichier model.py"""
        self.Coeffccs=model.renvoie_information("Coefficient","CCSCoeff")
        self.Coeffccp=model.renvoie_information("Coefficient","CCPCoeff")
        self.Specialite=model.renvoie_information("Nom","Specialite")
        self.Commune=model.renvoie_information("Commune","EcoleS")
        self.Concours=model.renvoie_information("Admission","EcoleS")
        self.ListeEcole=model.renvoie_information("Nom,Admission,Commune","EcoleSpe join EcoleS on EcoleSpe.IdEcole=EcoleS.id")
        
        """Pour eviter d'écrire dans le champs Ecole"""
        self.entry_ecole.configure(state="disabled")
        
        """On affiche les cases a cocher"""
        for commune in range(len(self.Commune)):
            choix_commune = Radiobutton(self.root,variable=self.var_commune,text=self.Commune[commune], value=self.Commune[commune],command=self.AffichageEcole)
            choix_commune.grid(row=commune+1, column=3,sticky="w")
        
        for concours in range(len(self.Concours)):
            choix_concours= Radiobutton(self.root,variable=self.var_concours,text=self.Concours[concours], value=self.Concours[concours],command=self.AffichageEcole)
            choix_concours.grid(row=concours+1, column=4,sticky="w")
            
        for specialite in range(len(self.Specialite)):
            choix_specialite = Radiobutton(self.root,variable=self.var_specialite,text=self.Specialite[specialite], value=self.Specialite[specialite],command=self.AffichageEcole)
            choix_specialite.grid(row=specialite+1, column=2,sticky="w")
            
        """On place les élèments """
        
        self.label_maths.grid(row=0,column=1)
        self.label_physique.grid(row=2,column=1)
        self.label_si.grid(row=4,column=1)
        self.label_info.grid(row=6,column=1)
        self.label_francais.grid(row=8,column=1)
        self.label_anglais.grid(row=10,column=1)
        self.entry_ecole.grid(row=1, column=5,padx =40)
        self.label_spe.grid(row=0, column=2)
        self.label_commune.grid(row=0,column=3)
        self.label_concours.grid(row=0,column=4)
        
        
        self.entry_maths.grid(row=1,column=1)
        self.entry_physique.grid(row=3,column=1)
        self.entry_si.grid(row=5,column=1)
        self.entry_info.grid(row=7,column=1)
        self.entry_francais.grid(row=9,column=1)
        self.entry_anglais.grid(row=11,column=1)
        
            
 
        self.entry_ecole.grid(row=2, rowspan=8,column=5)  
        self.label_ecole.grid(row=1,column=5)
        
        
        
        self.root.mainloop()

        
    def validate(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        """
            Permet de verifier si l'utilisateur rentre des chiffres dans les entry
            Fonction fourni dans la documentation du module Entry
            
                                                                                  """
        if(action=='1'):
            if text in '0123456789.':
                try:
                    float(value_if_allowed)
                    return True
                except ValueError:
                    return False
            else:
                return False
        else:
            return True  
        
        
    def AffichageEcole(self):
        """Recuperer les variables entrée par l'utilisateur"""
        samir=[]
        textaffiche=""
        NoteMode=(self.entry_maths.get()+self.entry_maths.get())
        NoteMaths=(self.entry_maths.get())
        NotePhysique=(self.entry_physique.get())
        NoteSi=(self.entry_si.get())
        NoteFrancais=(self.entry_francais.get())
        NoteAnglais=(self.entry_anglais.get())
        NoteInfo=((self.entry_info.get()))
        
        communeid=""
        concoursid=""
        Note=0
        
        """Active le champs Ecole et supprime ce qu'il y avait écrit avant"""
        self.entry_ecole.configure(state="normal")
        self.entry_ecole.delete(0.7,'end');
        
        """Pour éviter les erreurs dans la console python"""
        if NoteMode=="" or NoteMaths=="" or NotePhysique=="" or NoteSi=="" or NoteFrancais=="" or NoteAnglais=="" or NoteInfo=="":
            NoteMode=20 
            NoteMaths=20
            NotePhysique=20
            NoteSi=20
            NoteFrancais=20
            NoteAnglais=20
            NoteInfo=20
        else:
            NoteMode=float(self.entry_maths.get()+self.entry_maths.get())
            NoteMaths=float(self.entry_maths.get())
            NotePhysique=float(self.entry_physique.get())
            NoteSi=float(self.entry_si.get())
            NoteFrancais=float(self.entry_francais.get())
            NoteAnglais=float(self.entry_anglais.get())
            NoteInfo=float((self.entry_info.get()))
                
        """Boucles pour avoir les parametres choisi par l'utilisateur pour les mettres dans la fonction filtre """   
        
        Notek=[(self.Coeffccp[0]*NoteMode+self.Coeffccp[1]*NoteMaths+self.Coeffccp[2]*NotePhysique+self.Coeffccp[3]*NoteSi+self.Coeffccp[4]*NoteFrancais+self.Coeffccp[5]*NoteAnglais+self.Coeffccp[6]*NoteInfo)/sum(self.Coeffccp),(self.Coeffccs[0]*NoteMode+self.Coeffccs[1]*NoteMaths+self.Coeffccs[2]*NotePhysique+self.Coeffccs[3]*NoteSi+self.Coeffccs[4]*NoteFrancais+self.Coeffccs[5]*NoteAnglais+self.Coeffccs[6]*NoteInfo)/sum(self.Coeffccs)]
        
        for communechoisie in range(len(self.Commune)):
            if self.var_commune.get()=="Peu importe" or self.var_commune.get()=="" :
                communeid=None
                break
            if self.var_commune.get()==self.Commune[communechoisie]:
                communeid=self.Commune[communechoisie]
        
                
        for concourschoisie in range(len(self.Concours)):
            if self.var_concours.get()=="Peu importe" or self.var_concours.get()=="":
                concoursid=None
                break
            if self.var_concours.get()==self.Concours[concourschoisie]:
                concoursid=self.Concours[concourschoisie]
        
        if concoursid=="CCP" :
           Note=round(Notek[0],1)
            
        if concoursid=="CCS":
           
            Note=round(Notek[1],1)
        
            
        """Creation de la liste Ecole"""
        for creationliste in range (len(self.Specialite)):
            if concoursid==None:
                if self.var_specialite.get()==self.Specialite[creationliste]:
                     for choixnote in range(1):
                         Note=round(Notek[choixnote],1)
                         samir=samir+model.filtre(creationliste+1,communeid,concoursid,Note)
                         self.ListeEcole=list(set(samir))# Evite les doublons
                         break
                elif self.var_specialite.get()=="":
                        for choixnote in range(1):
                            Note=round(Notek[choixnote],1)
                            samir=samir+model.filtre(None,communeid,concoursid,Note)
                            self.ListeEcole=list(set(samir))# Evite les doublons 
                            break
            else:
                if self.var_specialite.get()==self.Specialite[creationliste]:
                    
                    self.ListeEcole=model.filtre(creationliste+1,communeid,concoursid,Note)
                    break
                elif self.var_specialite.get()=="":
                    self.ListeEcole=model.filtre(None,communeid,concoursid,Note)
                    break
                    
        """Permet de génerer le texte affiché"""
        for texteaafficher in range(len(self.ListeEcole)):
            textaffiche=textaffiche+"\n"+self.ListeEcole[texteaafficher][0]+" "+self.ListeEcole[texteaafficher][1]+" "+self.ListeEcole[texteaafficher][2]
          
        """Affiche le texte et evite de pouvoir écrire par dessus"""   
        self.entry_ecole.insert(2.0,textaffiche)
        self.entry_ecole.configure(state="disabled")
        

if __name__ == '__main__':
    ChoixEcole()
