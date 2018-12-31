#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 19:59:28 2018

@author: samir
"""

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
        self.root.geometry('900x260')
        self.root.resizable(False, False)
         
        """Initialise les variables"""
        self.var_specialite = StringVar(self.root)
        self.var_commune=StringVar(self.root)
        self.var_concours=StringVar(self.root)
        self.var_alternance=StringVar(self.root)
         
        """Initialise  entry et vcmd est une fonction qui verifie si l'utilisateur entre les bonnes informations"""
        vcmd = (self.root.register(self.callback),  '%P', '%S')
        self.entry_ecole=tkscrolled.ScrolledText(self.root, width=30, height=10,)
         
        """ Initialise les variables et les entrys et label pour afficher les moyennes et met 20 par défaut"""
        
        self.matieres = ('Maths', 'Physique', 'SI', 'Informatique', 'Francais', 'Anglais')
        self.var_matieres = [StringVar(self.root) for x in range(len(self.matieres))]
        self.labels_matiere = [ Label(self.root, text=f'Rentre ta moyenne de {mat}') for mat in self.matieres ] 
        for var in self.var_matieres: var.set(20) 
        self.entries_matiere = [ Entry(self.root, textvariable=var, validate='key', validatecommand = vcmd) for var in self.var_matieres ]
 
        """Initialise les labels et les affiches """
        
        Label(self.root, text='Specialité :' ).grid(row=0, column=2)
        Label(self.root, text='Commune :').grid(row=0,column=3)
        Label(self.root,text='Concours:').grid(row=0,column=4)
        Label(self.root,text='Alternance').grid(row=0,column=5)
        Label(self.root,text='Ecole:').grid(row=0,column=10)
        
        """Initalise les listes en utilisant les fonction du fichier model.py"""
         
        self.coeffccs=model.renvoie_information("Coefficient","CCSCoeff")
        self.coeffccp=model.renvoie_information("Coefficient","CCPCoeff")
        self.specialite=model.renvoie_information("Nom","Specialite")
        self.commune=model.renvoie_information("Commune","EcoleS")
        self.concours=model.renvoie_information("Admission","EcoleS")
        self.alternance=model.renvoie_information("Alternance","EcoleSpe")
         
        """Permet d'afficher toutes les ecoles contenue dans la base de données"""
         
        textaffiche=""
        self.listeecoles=list(set(model.filtre(None,None,None,None,20)))
        for texteaafficher in range(len(self.listeecoles)):
            textaffiche=textaffiche+"\n"+self.listeecoles[texteaafficher][0]+" "+self.listeecoles[texteaafficher][1]+" "+self.listeecoles[texteaafficher][2]
        self.entry_ecole.insert(0.0,textaffiche)
         
        """Pour eviter d'écrire dans le champs Ecole"""
        self.entry_ecole.configure(state="disabled")
         
        """On affiche les cases a cocher"""
        for specialite in range(len(self.specialite)):
            Radiobutton(self.root,variable=self.var_specialite,text=self.specialite[specialite], value=self.specialite[specialite],command=self.AffichageEcole).grid(row=specialite+1, column=2,sticky="w")
        
        for commune in range(len(self.commune)):
            Radiobutton(self.root,variable=self.var_commune,text=self.commune[commune], value=self.commune[commune],command=self.AffichageEcole).grid(row=commune+1, column=3,sticky="w")
        
        for concours in range(len(self.concours)):
            Radiobutton(self.root,variable=self.var_concours,text=self.concours[concours], value=self.concours[concours],command=self.AffichageEcole).grid(row=concours+1, column=4,sticky="w")
        
        for alternance in range(len(self.alternance)):
            Radiobutton(self.root,variable=self.var_alternance,text=self.alternance[alternance], value=self.alternance[alternance],command=self.AffichageEcole).grid(row=alternance+1, column=5,sticky="w")
            
        """On place les élèments """
        for i, lab in enumerate(self.labels_matiere):
            lab.grid(row=i*2, column=1)
         
        for i, entry in enumerate(self.entries_matiere):
            entry.grid(row=i*2+1, column=1)
 
        self.entry_ecole.grid(row=1, rowspan=8,column=10) 
         
        self.root.mainloop()
 
         
    def callback(self, value_if_allowed, text):
        """Gerer tous les types de notes pour avoir le bon nombre de décimales dans les notes"""
        if text=="²":
            return False
        elif value_if_allowed.replace(".", "", 1).isdigit() and float(value_if_allowed)<=20.00 or value_if_allowed == "":
            try :
                if value_if_allowed[2]=="." and len(value_if_allowed)<6 :
                    return True
                elif value_if_allowed[1]=="." and len(value_if_allowed)<5 :
                    return True
                else:
                    return False
            except IndexError:
                return True
        return False
        
    def AffichageEcole(self):
        """Recuperer les variables entrée par l'utilisateur"""
        ecoleintermediare=[]
        textaffiche=""
        matiere=[self.entries_matiere[0].get()+self.entries_matiere[2].get()]+[self.entries_matiere[i].get() for i in range(len(self.entries_matiere))]
        note=0
        zeropossible=("0","00.00","0.","00","00.0","0.0","0.00","00.")
               
        """Active le champs Ecole et supprime ce qu'il y avait écrit avant"""
        self.entry_ecole.configure(state="normal")
        self.entry_ecole.delete(0.7,'end');
        """Pour éviter les erreurs dans la console python"""
        for zero in range (len(zeropossible)):
            if zeropossible[zero] in matiere :
                self.entry_ecole.insert(0.0,"Soit pas aussi pessimiste")
                self.entry_ecole.configure(state="disabled")
                return
                
        if "" in matiere : 
            matiere=[20 for vide in range (len(matiere))]
            
        else:
            matiere=[(float(self.entries_matiere[0].get())+float(self.entries_matiere[2].get()))/2]+[float(self.entries_matiere[i].get()) for i in range(1,len(self.entries_matiere))]
             
        """Boucles pour avoir les parametres choisi par l'utilisateur pour les mettres dans la fonction filtre """  
        
        noteconcours=[sum((self.coeffccp[ccp]*matiere[ccp] for ccp in range (len(matiere))))/sum(self.coeffccp)]+[sum((self.coeffccs[ccs]*matiere[ccs] for ccs in range (len(matiere))))/sum(self.coeffccs)]

        for communechoisie in range(len(self.commune)):
            if self.var_commune.get()=="Peu importe" or self.var_commune.get()=="" :
                communeid=None
                break
            if self.var_commune.get()==self.commune[communechoisie]:
                communeid=self.commune[communechoisie]
                 
        for alternancechoisie in range(len(self.alternance)):
            if self.var_alternance.get()=="Peu importe" or self.var_alternance.get()=="" :
                alternanceid=None
                break
            if self.var_alternance.get()==self.alternance[alternancechoisie]:
                alternanceid=self.alternance[alternancechoisie]
         
        for concourschoisie in range(len(self.concours)):
            if self.var_concours.get()=="Peu importe" or self.var_concours.get()=="":
                concoursid=None
                break
            if self.var_concours.get()==self.concours[concourschoisie]:
                concoursid=self.concours[concourschoisie]
         
        for specialitechoisie in range(len(self.specialite)):
            if self.var_specialite.get()=="":
                specialiteid=None
                break
            if self.var_specialite.get()==self.specialite[specialitechoisie]:
                specialiteid=specialitechoisie+1
         
        if concoursid=="CCP" :
           note=round(noteconcours[0],2)
             
        if concoursid=="CCS":
            
            note=round(noteconcours[1],2)
             
        """Creation de la liste Ecole"""
        if concoursid==None:
                 for n in range(2):
                     note=round(noteconcours[n],2)
                     ecoleintermediare=ecoleintermediare+model.filtre(specialiteid,communeid,concoursid,alternanceid,note)
                     self.listeecoles=list(set(ecoleintermediare))
                     break
        else:
            self.listeecoles=list(set(model.filtre(specialiteid,communeid,concoursid,alternanceid,note)))
         
        """Permet de génerer le texte affiché"""
        for texteaafficher in range(len(self.listeecoles)):
            textaffiche=textaffiche+"\n"+self.listeecoles[texteaafficher][0]+" "+self.listeecoles[texteaafficher][1]+" "+self.listeecoles[texteaafficher][2]
           
        """Affiche le texte et evite de pouvoir écrire par dessus"""  
        self.entry_ecole.insert(0.0,textaffiche)
        self.entry_ecole.configure(state="disabled")
         
if __name__ == '__main__':
    ChoixEcole()