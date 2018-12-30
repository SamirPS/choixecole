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
        
        """Initialise les variables et met 20 comme valeur par defaut """
        self.var_maths=StringVar(self.root)
        self.var_physique=StringVar(self.root)
        self.var_si=StringVar(self.root)
        self.var_info=StringVar(self.root)
        self.var_francais=StringVar(self.root)
        self.var_anglais=StringVar(self.root)
        self.var_specialite = StringVar(self.root)
        self.var_commune=StringVar(self.root)
        self.var_concours=StringVar(self.root)
        self.var_alternance=StringVar(self.root)
        
        self.var_maths.set(20)
        self.var_physique.set(20)
        self.var_si.set(20)
        self.var_info.set(20)
        self.var_francais.set(20)
        self.var_anglais.set(20)
        
        """Initialise les labels et entry et vcmd est une fonction qui verifie si l'utilisateur entre les bonnes informations"""
        vcmd = (self.root.register(self.callback),'%P','%S' )
        self.entry_maths = Entry(self.root, textvariable=self.var_maths,validate = 'key', validatecommand = vcmd)
        self.entry_physique = Entry(self.root, textvariable=self.var_physique,validate = 'key', validatecommand = vcmd)
        self.entry_si = Entry(self.root, textvariable=self.var_si,validate = 'key', validatecommand = vcmd)
        self.entry_info = Entry(self.root, textvariable=self.var_info,validate = 'key', validatecommand = vcmd)
        self.entry_francais = Entry(self.root, textvariable=self.var_francais,validate = 'key', validatecommand = vcmd)
        self.entry_anglais = Entry(self.root, textvariable=self.var_anglais,validate = 'key', validatecommand = vcmd)
        self.entry_ecole=tkscrolled.ScrolledText(self.root, width=30, height=10,)
        
        self.label_maths=Label(self.root,text='Rentre ta moyenne de Maths')
        self.label_physique=Label(self.root,text='Rentre ta moyenne de Physique')
        self.label_si=Label(self.root,text='Rentre ta moyenne de SI')
        self.label_info=Label(self.root,text='Rentre ta moyenne en Informatique')
        self.label_francais=Label(self.root,text='Rentre ta moyenne de Francais')
        self.label_anglais=Label(self.root,text='Rentre ta moyenne d"Anglais')
        self.label_commune = Label(self.root, text='Commune :')
        self.label_spe = Label(self.root, text='Specialité :' )
        self.label_concours=Label(self.root,text='Concours:')
        self.label_ecole=Label(self.root,text='Ecole:')
        self.label_alternance=Label(self.root,text='Alternance')
        
        
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
            choix_specialite = Radiobutton(self.root,variable=self.var_specialite,text=self.specialite[specialite], value=self.specialite[specialite],command=self.AffichageEcole)
            choix_specialite.grid(row=specialite+1, column=2,sticky="w")
            
        for commune in range(len(self.commune)):
            choix_commune = Radiobutton(self.root,variable=self.var_commune,text=self.commune[commune], value=self.commune[commune],command=self.AffichageEcole)
            choix_commune.grid(row=commune+1, column=3,sticky="w")
        
        for concours in range(len(self.concours)):
            choix_concours= Radiobutton(self.root,variable=self.var_concours,text=self.concours[concours], value=self.concours[concours],command=self.AffichageEcole)
            choix_concours.grid(row=concours+1, column=4,sticky="w")
            
        for alternance in range(len(self.alternance)):
            choix_alternance = Radiobutton(self.root,variable=self.var_alternance,text=self.alternance[alternance], value=self.alternance[alternance],command=self.AffichageEcole)
            choix_alternance.grid(row=alternance+1, column=5,sticky="w")
        
            
            """On place les élèments """
        
        self.label_maths.grid(row=0,column=1)
        self.label_physique.grid(row=2,column=1)
        self.label_si.grid(row=4,column=1)
        self.label_info.grid(row=6,column=1)
        self.label_francais.grid(row=8,column=1)
        self.label_anglais.grid(row=10,column=1)
        self.label_spe.grid(row=0, column=2)
        self.label_commune.grid(row=0,column=3)
        self.label_concours.grid(row=0,column=4)
        self.label_ecole.grid(row=0,column=10)
        self.label_alternance.grid(row=0,column=5)
        
        
        self.entry_maths.grid(row=1,column=1)
        self.entry_physique.grid(row=3,column=1)
        self.entry_si.grid(row=5,column=1)
        self.entry_info.grid(row=7,column=1)
        self.entry_francais.grid(row=9,column=1)
        self.entry_anglais.grid(row=11,column=1)
        self.entry_ecole.grid(row=1, rowspan=8,column=10)  
        
        self.root.mainloop()

        
    def callback(self, P,S):
        """Permet de savoir si on rentre des bon floats """
        if S=="²":
            return False
        elif P.replace(".", "", 1).isdigit() and float(P)<1.00  and P[0]=="0" or  P=="" :
            try : 
                if  P[1]=="." and len(P)<5 and P!="00":
                    return True
                elif P[1]=="0" and len(P)<6 and P!="000":
                    return True
                else :
                    return False
            except IndexError:
                return True
            
        elif  P.replace(".", "", 1).isdigit() and float(P)<10.00 and P[0]!="0" and len(P)<5 :
            return True
        elif  P.replace(".", "", 1).isdigit() and 1.00<=float(P)<10.00 and P[0]=="0":
            try : 
                if  P[1]=="0" and len(P)<5 and float(P)<1.00:
                    return True
                elif P[1]!="0" and len(P)<6 and P!="000":
                    return True
                else :
                    return False
            except IndexError:
                return True
        elif P.replace(".", "", 1).isdigit() and 10.00<=float(P)<=20.00 and len(P)<6 and P[0]!="0":
            return True
        
        else:
            return False
    
    def AffichageEcole(self):
        """Recuperer les variables entrée par l'utilisateur"""
        ecoleintermediare=[]
        textaffiche=""
        note=0
        specialiteid=""
        communeid=""
        concoursid=""
        alternanceid=""
        matiere=[self.entry_maths.get()+self.entry_si.get(),self.entry_maths.get(),self.entry_physique.get(),self.entry_si.get(),self.entry_francais.get(),self.entry_anglais.get(),(self.entry_info.get())]
        """Active le champs Ecole et supprime ce qu'il y avait écrit avant"""
        self.entry_ecole.configure(state="normal")
        self.entry_ecole.delete(0.7,'end');
        """Pour éviter les erreurs dans la console python"""
        
        if matiere[0]=="" or matiere[1]=="" or matiere[2]=="" or matiere[3]=="" or matiere[4]=="" or matiere[5]=="" or matiere[6]=="":
            for samir in range(len(matiere)):
                matiere[samir]=20
        elif float((float(matiere[1])+float(matiere[3]))/2)==0.0 or matiere[1]==0.0 or matiere[2]==0.0 or matiere[3]==0.0 or matiere[4]==0.0 or matiere[5]==0.0 or matiere[6]==0.0 :
            self.entry_ecole.insert(0.0,"Soit pas aussi pessimiste")
            self.entry_ecole.configure(state="disabled")
            return
        else:
            matiere[0]=(float(self.entry_maths.get())+float(self.entry_si.get()))/2
            for i in range(1,len(matiere)):
                matiere[i]=float(matiere[i])
        """Boucles pour avoir les parametres choisi par l'utilisateur pour les mettres dans la fonction filtre """   
       
        noteconcours=[sum((self.coeffccp[k]*matiere[k] for k in range (len(matiere))))/sum(self.coeffccp)]+[sum((self.coeffccs[j]*matiere[j] for j in range (len(matiere))))/sum(self.coeffccs)]
        
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
                     self.listeecoles=list(set(ecoleintermediare))# Evite les doublons
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