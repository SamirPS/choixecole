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
        x_cordinate = int((self.root.winfo_screenwidth()/2) - (630/2))
        y_cordinate = int((self.root.winfo_screenheight()/2) - (273/2))
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
        
        vcmd = (self.root.register(self.valider),  '%P')
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
        self.information_desirer=[model.renvoie_information(self.colonne_table[i][0],self.colonne_table[i][1]) for i in range(len(self.colonne_table))]+[["3/2","5/2"]]
        
        """Permet d'afficher toutes les ecoles contenue dans la base de données"""
        self.concours=model.renvoie_coefficient()
        self.notematiere=[20]*7
        self.noteconcours=self.renvoie_note()
        self.choix_utilisateur={"Specialite":None,"Region":None,"Concours":None,"Alternance":None}
        self.AffichageEcole()

        """affiche le texte et pour eviter d'écrire dans le champs Ecole"""
        self.entry_ecole.insert(0.0,self.textaffiche)
        self.entry_ecole.configure(state="disabled")
        """On affiche les combobox et on les lie a Affichage Ecole"""
        
        for i,combo in enumerate(self.affichage):
            combo=ttk.Combobox(self.root,state="readonly",textvariable=self.var_affichage[i],values=self.information_desirer[i],height="4")
            combo.grid(row=i*2+1,column=2,sticky="w",padx=10)
            combo.bind("<<ComboboxSelected>>",self.choixuseur)
            
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
    def choixuseur(self,event):
        self.choix_utilisateur={"Specialite":self.information_desirer[0].index(self.var_affichage[0].get()),"Region":self.var_affichage[1].get(),"Concours":self.var_affichage[2].get(),"Alternance":self.var_affichage[3].get()}
        for cle in self.choix_utilisateur:
            if self.choix_utilisateur[cle]=="Peu importe" or self.choix_utilisateur[cle]==0:
                self.choix_utilisateur[cle]=None
        self.notematiere=[self.entries_matiere[0].get()+self.entries_matiere[2].get()]+[self.entries_matiere[i].get() for i in range(len(self.entries_matiere))]
        
        for i in range(len(self.notematiere)):
            if "" in self.notematiere : 
                self.notematiere[i]=20
            else:
                self.notematiere[i]=float(self.notematiere[i])
        self.notematiere[0]=(float(self.notematiere[1])+float(self.entries_matiere[3].get()))/2
        
        if 0.0 in self.notematiere :
             self.entry_ecole.configure(state="normal")
             self.entry_ecole.delete(0.7,'end');
             self.entry_ecole.insert(0.0,"Soit pas aussi pessimiste")
             self.entry_ecole.configure(state="disabled")
             return 
         
        self.noteconcours=self.renvoie_note()
        self.AffichageEcole()
        
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
            except  TypeError:
                return
        
    def returntext(self):
        """Affiche le nom de l'école et a cote Refuse ou admis"""
     
        ecoleamoi=[]
        for nom in self.noteconcours:
                ecoleamoi+=list(set(self.Ecole(self.noteconcours[nom],self.concours[nom],self.choix_utilisateur)))
        
        listeecoles=[]
        for cle in self.concours:
                for nom in self.concours[cle]:
                    listeecoles+=list(set(model.filtre(None,None,None,None,nom,None)))
        
        admission=["Admis"]*len(listeecoles)
        for i in range(len(listeecoles)):
            if listeecoles[i] not in ecoleamoi  :
                admission[i]="Refuse"
        return admission,listeecoles
      
    def save_file(self, whatever = None):
        if (self.filename ==()):
            self.save_file_as()
            
        self.convertpdf()

    def save_file_as(self, whatever = None):
        self.filename =filedialog.asksaveasfilename(defaultextension='.pdf',
                                                             filetypes = [
        ('PDF', '*.pdf'),

            ])
   
        self.convertpdf()
      
    def valider(self, value_if_allowed):
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
    
    def renvoie_note(self):
        self.noteconcours={}
        for nom in self.concours:
            self.noteconcours[nom]={}
            for cle in self.concours[nom]:
               self.noteconcours[nom][cle]=model.NoteCoefficient(self.concours[nom][cle],self.notematiere)
        return self.noteconcours
    
    def Ecole(self,listenote,dictonnaire,choix_utilisateur):
        
        self.listeecoles=[]
        for cle in dictonnaire:
            self.listeecoles=self.listeecoles+model.filtre(choix_utilisateur["Specialite"],choix_utilisateur["Region"],choix_utilisateur["Concours"],choix_utilisateur["Alternance"],cle,listenote[cle])
        return self.listeecoles
        
    def AffichageEcole(self):
        self.listeecoles=[]
        self.textaffiche="" 
        """Active le champs Ecole et supprime ce qu'il y avait écrit avant"""
        self.entry_ecole.configure(state="normal")
        self.entry_ecole.delete(0.7,'end');
     
        if self.var_affichage[4]=="3/2":
            for nom in self.noteconcours:
                for cle in self.noteconcours[nom]:
                    self.noteconcours[nom][cle]=self.noteconcours[nom][cle]+self.concours[nom][cle][-1]
                    
        for nom in self.noteconcours:
            if self.choix_utilisateur["Concours"]==None:
                self.listeecoles+=list(set(self.Ecole(self.noteconcours[nom],self.concours[nom],self.choix_utilisateur)))
            elif self.choix_utilisateur["Concours"]==nom:
                self.listeecoles=list(set(self.Ecole(self.noteconcours[nom],self.concours[nom],self.choix_utilisateur)))
                break
                
        """Permet de génerer le texte affiché"""
        for texteaafficher in range(len(self.listeecoles)):
            self.textaffiche=self.textaffiche+"\n"+self.listeecoles[texteaafficher][0]+" "+self.listeecoles[texteaafficher][1]+" "+self.listeecoles[texteaafficher][2]
           
        """Affiche le texte et evite de pouvoir écrire par dessus"""  
        self.entry_ecole.insert(0.0,self.textaffiche)
        self.entry_ecole.configure(state="disabled")
         
if __name__ == '__main__':
    ChoixEcole()