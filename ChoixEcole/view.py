#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 19:59:28 2018

@author: samir
"""
from tkinter import Tk,StringVar, Label, Radiobutton,Entry
import model
import tkinter.scrolledtext as tkscrolled
from tkinter.ttk import *

class ChoixEcole:
     
    def __init__(self):
        
        """Initialise l'application et change le titre"""
  
        self.root = Tk()
        self.root.title("ChoixEcole")
        self.root.resizable(False, False)
         
        """Initialise  entry et vcmd est une fonction qui verifie si l'utilisateur entre les bonnes informations"""
        
        vcmd = (self.root.register(self.callback),  '%P')
        self.entry_ecole=tkscrolled.ScrolledText(self.root, width=30, height=10,)
         
        """ Initialise les variables et les entrys et label pour afficher les moyennes et met 20 par défaut"""
        
        self.matieres = ('de maths', 'de physique', 'de si', "d'informatique", 'de francais',"d'anglais")
        self.var_matieres = [StringVar(self.root) for mat in range(len(self.matieres))]
        self.labels_matiere = [ Label(self.root, text='Moyenne '+mat) for mat in self.matieres ] 
        for var in self.var_matieres: var.set(20) 
        self.entries_matiere = [ Entry(self.root, textvariable=var, validate='key', validatecommand = vcmd) for var in self.var_matieres ]
 
        """Initialise les variables et les entrys et label pour afficher Specialite,Commune,Concours,Alternane 
           Et les elements 
                                                                         """
        self.affichage=('Specialité :','Region :','Concours:','Alternance')
        self.var_affichage=[StringVar(self.root) for aff in range(len(self.affichage))]
        self.labels_affichage= [ Label(self.root, text=aff) for aff in self.affichage ] 
        for i in range(1,4):
            self.var_affichage[i].set("Peu importe")
        self.ccs,self.ccp=model.renvoie_coefficient()
        """Les années de prepa"""
        self.anneeprepa=("3/2","5/2","7/2")
        self.annee=StringVar(self.root)
        self.annee.set("3/2")
        
        """Initalise les listes en utilisant les fonction du fichier model.py"""
        self.colonne_table=(("Nom","Specialite"),("Region","EcoleS"),("Admission","EcoleS"),("Alternance","EcoleSpe"))
        self.information_desirer=[model.renvoie_information(self.colonne_table[i][0],self.colonne_table[i][1]) for i in range(len(self.colonne_table))]
        
        """Permet d'afficher toutes les ecoles contenue dans la base de données"""
        self.listeecoles=[]
        
        textaffiche=""
        
        for cle in self.ccs:
            self.listeecoles+=list(set(model.filtre(None,None,None,None,cle,5000)))
        for cle in self.ccp:
            self.listeecoles+=list(set(model.filtre(None,None,None,None,cle,5000)))
            
        for texteaafficher in range(len(self.listeecoles)):
            textaffiche=textaffiche+"\n"+self.listeecoles[texteaafficher][0]+" "+self.listeecoles[texteaafficher][1]+" "+self.listeecoles[texteaafficher][2]
        self.entry_ecole.insert(0.0,textaffiche)
        
        """Pour eviter d'écrire dans le champs Ecole"""
        self.entry_ecole.configure(state="disabled")
         
        """On affiche les cases a cocher"""
        for specialite in range(len(self.information_desirer[0])):
            Radiobutton(self.root,variable=self.var_affichage[0],text=self.information_desirer[0][specialite], value=self.information_desirer[0][specialite],command=self.AffichageEcole).grid(row=specialite+1, column=2,sticky="w")
        for region in range(len(self.information_desirer[1])):
            Radiobutton(self.root,variable=self.var_affichage[1],text=self.information_desirer[1][region], value=self.information_desirer[1][region],command=self.AffichageEcole).grid(row=region+1, column=3,sticky="w")
        for concours in range(len(self.information_desirer[2])):
            Radiobutton(self.root,variable=self.var_affichage[2],text=self.information_desirer[2][concours], value=self.information_desirer[2][concours],command=self.AffichageEcole).grid(row=concours+1, column=4,sticky="w")
        for alternance in range(len(self.information_desirer[3])):
            Radiobutton(self.root,variable=self.var_affichage[3],text=self.information_desirer[3][alternance], value=self.information_desirer[3][alternance],command=self.AffichageEcole).grid(row=alternance+1, column=5,sticky="w")
        for annee in range(len(self.anneeprepa)):
             Radiobutton(self.root,variable=self.annee,text=self.anneeprepa[annee], value=self.anneeprepa[annee],command=self.AffichageEcole).grid(row=annee+1, column=6,sticky="w")
            
        """On place les élèments """
        for i, lab in enumerate(self.labels_matiere):
            lab.grid(row=i*2, column=1)
        for i,lab in enumerate(self.labels_affichage):
            lab.grid(row=0 ,column=i+2)
        for i, entry in enumerate(self.entries_matiere):
            entry.grid(row=i*2+1, column=1)
 
        self.entry_ecole.grid(row=1,rowspan=8,column=16) 
        Label(self.root,text='Ecole:').grid(row=0,column=16)
        Label(self.root,text='Année:').grid(row=0,column=6)
        
        self.root.mainloop()
 
    def callback(self, value_if_allowed):
        """Gerer tous les types de notes pour avoir le bon nombre de décimales dans les notes"""
        if value_if_allowed.replace(".", "", 1).isdecimal() and float(value_if_allowed)<=20.00 or value_if_allowed == "":
            try :
                if value_if_allowed[2]=="." and len(value_if_allowed)<6 :
                    return True
                elif value_if_allowed[1]=="." and len(value_if_allowed)<5 :
                    return True
            except IndexError:
                return True
        return False
    
    def renvoie_note_pointsdebonification(self,matiere):
        noteccp,noteccs,bonificationccs,bonificationccp={},{},{},{}
        for cle in self.ccp :
            noteccp[cle]=model.NoteCoefficient(self.ccp[cle],matiere)
            bonificationccp[cle]=self.ccp[cle][-1]
        for cle in self.ccs :
            noteccs[cle]=model.NoteCoefficient(self.ccs[cle],matiere)
            bonificationccs[cle]=self.ccs[cle][-1]
        return noteccs,noteccp,bonificationccs,bonificationccp    
    
    def Ecole(self,listenote,dictonnaire,choix_specialite,choix_region,choix_concours,choix_alternance):
        for cle in dictonnaire:
            self.listeecoles=self.listeecoles+model.filtre(choix_specialite,choix_region,choix_concours,choix_alternance,cle,listenote[cle])
        return self.listeecoles
        
    def AffichageEcole(self):
        """Recuperer les variables entrée par l'utilisateur"""
        self.listeecoles=[]
        textaffiche="" 
        matiere=[self.entries_matiere[0].get()+self.entries_matiere[2].get()]+[self.entries_matiere[i].get() for i in range(len(self.entries_matiere))]
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
            matiere=[20 for i in range (len(matiere))]
            
        else:
            matiere=[(float(self.entries_matiere[0].get())+float(self.entries_matiere[2].get()))/2]+[float(self.entries_matiere[i].get()) for i in range(len(self.entries_matiere))]
        
        """Boucles pour avoir les parametres choisi par l'utilisateur pour les mettres dans la fonction filtre """  
        noteccs,noteccp,bonificationccs,bonificationccp=self.renvoie_note_pointsdebonification(matiere) 
        
        if self.var_affichage[0].get()=="":
            choix_specialite=None
        else:
            choix_specialite=self.information_desirer[0].index(self.var_affichage[0].get())+1
            
        if  self.var_affichage[1].get()=="Peu importe":
            choix_region=None
        else :
            choix_region=self.var_affichage[1].get()
        
        if  self.var_affichage[2].get()=="Peu importe":
            choix_concours=None
        else :
            choix_concours=self.var_affichage[2].get()
            
        if self.var_affichage[3].get()=="Peu importe":
            choix_alternance=None
        else :
            choix_alternance=self.var_affichage[3].get()
        
        if self.annee.get()=="3/2":
            for cle in noteccp:
                noteccp[cle]=noteccp[cle]+bonificationccp[cle]
            for cle in noteccs:
                noteccs[cle]=noteccs[cle]+bonificationccs[cle]
                
        if choix_concours=="CCS":
            self.listeecoles=list(set(self.Ecole(noteccs,self.ccs,choix_specialite,choix_region,choix_concours,choix_alternance)))
        elif choix_concours=="CCP":
            self.listeecoles=list(set(self.Ecole(noteccp,self.ccp,choix_specialite,choix_region,choix_concours,choix_alternance)))
        else:
            self.listeecoles=list(set(self.Ecole(noteccp,self.ccp,choix_specialite,choix_region,choix_concours,choix_alternance)+self.Ecole(noteccs,self.ccs,choix_specialite,choix_region,choix_concours,choix_alternance)))
 
            
        """Permet de génerer le texte affiché"""
        for texteaafficher in range(len(self.listeecoles)):
            textaffiche=textaffiche+"\n"+self.listeecoles[texteaafficher][0]+" "+self.listeecoles[texteaafficher][1]+" "+self.listeecoles[texteaafficher][2]
           
        """Affiche le texte et evite de pouvoir écrire par dessus"""  
        self.entry_ecole.insert(0.0,textaffiche)
        self.entry_ecole.configure(state="disabled")
         
if __name__ == '__main__':
    ChoixEcole()