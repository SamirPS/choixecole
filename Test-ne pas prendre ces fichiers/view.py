#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 19:59:28 2018
@author: samir
"""
from tkinter import Tk,StringVar, Label,Entry,ttk,filedialog,Menu
import model
import tkinter.scrolledtext as tkscrolled
from fpdf import FPDF
class ChoixEcole:
     
    def __init__(self):
        
        """Initialise l'application et change le titre et la positionne """
  
        self.root = Tk()
        self.root.title("ChoixEcole")
        self.root.resizable(False, False)
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (630/2))
        y_cordinate = int((screen_height/2) - (273/2))
        self.root.geometry("630x273+{}+{}".format( x_cordinate, y_cordinate))
        
        """Ajoute un menu"""
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        menufichier = Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Fichier", menu=menufichier) 
        menufichier.add_command(label="Enregistrer ",command=self.save_file)
        menufichier.add_command(label="Enregistrer sous",command=self.save_file_as)
        self.filename =() 
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
        self.affichage=('Specialité','Region','Concours','Alternance','Année')
        self.var_affichage=[StringVar(self.root) for aff in range(len(self.affichage))]
        self.labels_affichage= [ Label(self.root, text=aff) for aff in self.affichage ] 
        for i in range(0,4): self.var_affichage[i].set("Peu importe")
        self.var_affichage[4].set("3/2")
        
        """Initalise les listes en utilisant les fonction du fichier model.py"""
        self.colonne_table=(("Nom","Specialite"),("Region","EcoleS"),("Admission","EcoleS"),("Alternance","EcoleSpe"))
        self.information_desirer=[model.renvoie_information(self.colonne_table[i][0],self.colonne_table[i][1]) for i in range(len(self.colonne_table))]+[["3/2","5/2","7/2"]]
        
        """Permet d'afficher toutes les ecoles contenue dans la base de données"""
        self.listeecoles=[]
        self.concours=model.renvoie_coefficient()    
        self.textaffiche=""
        self.note=None
        if self.concours!={}:
            for cle in self.concours:
                for nom in self.concours[cle]:
                    self.listeecoles+=list(set(model.filtre(None,None,None,None,nom,self.note)))
                    
            for texteaafficher in range(len(self.listeecoles)):
                self.textaffiche=self.textaffiche+"\n"+self.listeecoles[texteaafficher][0]+" "+self.listeecoles[texteaafficher][1]+" "+self.listeecoles[texteaafficher][2]
            
        """affiche le texte et pour eviter d'écrire dans le champs Ecole"""
        self.entry_ecole.insert(0.0,self.textaffiche)
        self.entry_ecole.configure(state="disabled")
        """On affiche les combobox et on les lie a Affichage Ecole"""
        
        for i,combo in enumerate(self.affichage):
            combo=ttk.Combobox(self.root,state="readonly",textvariable=self.var_affichage[i],values=self.information_desirer[i],height="4")
            combo.grid(row=i*2+1,column=2,sticky="w",padx=10)
            combo.bind("<<ComboboxSelected>>",self.AffichageEcole)

        
        """On place les élèments """
        for i, lab in enumerate(self.labels_matiere):
            lab.grid(row=i*2, column=1)
        for i,lab in enumerate(self.labels_affichage):
            lab.grid(row=i*2,column=2)
        for i, entry in enumerate(self.entries_matiere):
            entry.grid(row=i*2+1, column=1)
            
        self.entry_ecole.grid(row=1,rowspan=8,column=3) 
        Label(self.root,text='Ecole:').grid(row=0,column=3)
        
        self.root.mainloop()
    
    def convertpdf(self):
            """Converti en PDF """   
            try:
                
                pdf=FPDF()
                pdf.add_page()
                pdf.set_font("Arial",size=12)
                admission,listeecoles=self.returntext()
                for texteaafficher in range(len(admission)):
                    pdf.cell(200,10,txt=listeecoles[texteaafficher][0]+" "*15+admission[texteaafficher] ,ln=1,align="L")
                pdf.output(self.filename)
            except TypeError:
                return
        
    def returntext(self):
        """Affiche le nom de l'école et a cote Refuse ou admis"""
        listeecoles,ecoleamoi,admission=[],[],[]
        choix_utilisateur={"Specialite":None,"Region":None,"Concours":None,"Alternance":None}
        matiere=[self.entries_matiere[0].get()+self.entries_matiere[2].get()]+[self.entries_matiere[i].get() for i in range(len(self.entries_matiere))]
        
        
        if "" in matiere : 
            matiere=[20]*7
        elif 0.0 in map(float,matiere) :
            matiere=[0]*7
        else:
            matiere=[(float(self.entries_matiere[0].get())+float(self.entries_matiere[2].get()))/2]+[float(self.entries_matiere[i].get()) for i in range(len(self.entries_matiere))]
        
        """Boucles pour avoir les parametres choisi par l'utilisateur pour les mettres dans la fonction filtre """  
        noteconcours=self.renvoie_note(matiere) 
        for nom in noteconcours:
                ecoleamoi+=list(set(self.Ecole(noteconcours[nom],self.concours[nom],choix_utilisateur)))
            
        for cle in self.concours:
                for nom in self.concours[cle]:
                    listeecoles+=list(set(model.filtre(None,None,None,None,nom,None)))
        for i in range(len(listeecoles)):
            if listeecoles[i] in ecoleamoi  :
                admission.append("Admis")
            else:
                admission.append("Refuse")
        return admission,listeecoles
        
    def save_file(self, whatever = None):
        if (self.filename ==()):
            self.save_file_as()
        else:
            self.convertpdf()

    def save_file_as(self, whatever = None):
        self.filename =filedialog.asksaveasfilename(defaultextension='.pdf',
                                                             filetypes = [
        ('PDF', '*.pdf'),

            ])
   
        self.convertpdf()
      
    def callback(self, value_if_allowed):
        """Gerer tous les types de notes pour avoir le bon nombre de décimales dans les notes et entre 00.00 a 20.00 """
        if value_if_allowed.replace(".", "", 1).isdecimal() and float(value_if_allowed)<=20.00 or value_if_allowed == "":
            try :
                if value_if_allowed[2]=="." and len(value_if_allowed)<6 :
                    return True
                elif value_if_allowed[1]=="." and len(value_if_allowed)<5 :
                    return True
            except IndexError:
                return True
        return False
    
    def renvoie_note(self,matiere):
        noteconcours={}
        for nom in self.concours:
            noteconcours[nom]={}
            for cle in self.concours[nom]:
                noteconcours[nom][cle]=model.NoteCoefficient(self.concours[nom][cle],matiere)
        return noteconcours 
    
    def Ecole(self,listenote,dictonnaire,choix_utilisateur):
        
        self.listeecoles=[]
        for cle in dictonnaire:
            self.listeecoles=self.listeecoles+model.filtre(choix_utilisateur["Specialite"],choix_utilisateur["Region"],choix_utilisateur["Concours"],choix_utilisateur["Alternance"],cle,listenote[cle])
        return self.listeecoles
        
    def AffichageEcole(self,event):
        """Recuperer les variables entrée par l'utilisateur"""
        self.listeecoles=[]
        self.textaffiche="" 
        matiere=[self.entries_matiere[0].get()+self.entries_matiere[2].get()]+[self.entries_matiere[i].get() for i in range(len(self.entries_matiere))]
        choix_utilisateur={"Specialite":self.information_desirer[0].index(self.var_affichage[0].get()),"Region":self.var_affichage[1].get(),"Concours":self.var_affichage[2].get(),"Alternance":self.var_affichage[3].get()}
        """Active le champs Ecole et supprime ce qu'il y avait écrit avant"""
        self.entry_ecole.configure(state="normal")
        self.entry_ecole.delete(0.7,'end');
        
        """Pour éviter les erreurs dans la console python"""
        
        if "" in matiere : 
            matiere=[20]*7
        elif 0.0 in map(float,matiere) :
            self.entry_ecole.insert(0.0,"Soit pas aussi pessimiste")
            self.entry_ecole.configure(state="disabled")
            return 
        else:
            matiere=[(float(self.entries_matiere[0].get())+float(self.entries_matiere[2].get()))/2]+[float(self.entries_matiere[i].get()) for i in range(len(self.entries_matiere))]
        
        """Boucles pour avoir les parametres choisi par l'utilisateur pour les mettres dans la fonction filtre """  
        noteconcours=self.renvoie_note(matiere)  
        for cle in choix_utilisateur:
            if choix_utilisateur[cle]=="Peu importe" or choix_utilisateur[cle]==0:
                choix_utilisateur[cle]=None
        
        
        if self.var_affichage[4]=="3/2":
            for nom in noteconcours:
                for cle in noteconcours[nom]:
                    noteconcours[nom][cle]=noteconcours[nom][cle]+self.concours[nom][cle][-1]
                    
        for nom in noteconcours:
            if choix_utilisateur["Concours"]==None:
                self.listeecoles+=list(set(self.Ecole(noteconcours[nom],self.concours[nom],choix_utilisateur)))
            elif choix_utilisateur["Concours"]==nom:
                self.listeecoles=list(set(self.Ecole(noteconcours[nom],self.concours[nom],choix_utilisateur)))
                break
                
           
 
        """Permet de génerer le texte affiché"""
        for texteaafficher in range(len(self.listeecoles)):
            self.textaffiche=self.textaffiche+"\n"+self.listeecoles[texteaafficher][0]+" "+self.listeecoles[texteaafficher][1]+" "+self.listeecoles[texteaafficher][2]
           
        """Affiche le texte et evite de pouvoir écrire par dessus"""  
        self.entry_ecole.insert(0.0,self.textaffiche)
        self.entry_ecole.configure(state="disabled")
         
if __name__ == '__main__':
    ChoixEcole()