#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 19:59:28 2018
@author: samir
"""
from tkinter import Tk,StringVar, Label,Entry,filedialog,Menu,Listbox,Scrollbar
import model
import tkinter.scrolledtext as tkscrolled
from fpdf import FPDF
class ChoixEcole:
     
    def __init__(self):
        
        """Initialise l'application et change le titre et la positionne """
  
        self.root = Tk()
        self.root.title("ChoixEcole")
        self.root.resizable(False, False)
        
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
 
        """Initialise les variables et listebox des informations contenu dans self.affichage """
                                                                        
        self.affichage=('Specialité','Region','Concours','Alternance','Année')
        self.labels_affichage= [ Label(self.root, text=aff) for aff in self.affichage ] 
        self.listbox_affichage=[Listbox(self.root,selectmode='extended',exportselection=0, width=20, height=10) for aff in range(len(self.affichage)-1)]+[Listbox(self.root,exportselection=0, width=20, height=10)]
        self.scrollbar =[Scrollbar(self.root, orient="vertical") for aff in self.affichage]
        
        """Initalise les listes en utilisant les fonction du fichier model.py"""
        self.colonne_table=(("Nom","Specialite"),("Region","EcoleS"),("Admission","EcoleS"),("Alternance","EcoleSpe"))
        self.information_desirer=[model.renvoie_information(self.colonne_table[i][0],self.colonne_table[i][1]) for i in range(len(self.colonne_table))]+[["3/2","5/2"]]
        
        """Permet d'afficher toutes les ecoles contenue dans la base de données"""
        self.concours=model.renvoie_coefficient()
        self.choixuseur("<<ListboxSelect>>")
              
        """On affiche les ListeBoxs et on y  ajoute les données"""
        for i in range(len(self.listbox_affichage)):
            for donnees in self.information_desirer[i]:
                self.listbox_affichage[i].insert("end",donnees)
                
        """On place les élèments et on affecte une scrollbar a la listbox """
        for i,listbox in enumerate(self.listbox_affichage):
            listbox.grid(row=1,column=i+2,padx=20,rowspan=10)
            listbox.bind("<<ListboxSelect>>",self.choixuseur)
            self.scrollbar[i].config(command=listbox.yview)
            self.scrollbar[i].grid(row=1,column=i+2,rowspan=10,sticky='e')
            listbox.config(yscrollcommand=self.scrollbar[i].set)
        for i, lab in enumerate(self.labels_matiere):
            lab.grid(row=i*2, column=0)
        for i,lab in enumerate(self.labels_affichage):
            lab.grid(row=0,column=i+2)
        for i, entry in enumerate(self.entries_matiere):
            entry.grid(row=i*2+1, column=0)
            entry.bind("<KeyPress>",self.choixuseur)
            entry.bind("<KeyRelease>",self.choixuseur)
            
        self.entry_ecole.grid(row=1,column=10,rowspan=10) 
        Label(self.root,text='Ecole:').grid(row=0,column=10)
        
        self.root.mainloop()
    def choixuseur(self,event):
        """Met a jour les variables en fonction des clics de l'utilisateur"""
        self.choix_utilisateur={"Specialite":self.listbox_affichage[0].curselection(),"Region":tuple(self.listbox_affichage[1].get(0,"end")[i] for i in self.listbox_affichage[1].curselection()),"Concours":tuple(self.listbox_affichage[2].get(i) for i in self.listbox_affichage[2].curselection()),"Alternance":tuple(self.listbox_affichage[3].get(i) for i in self.listbox_affichage[3].curselection())}
        for cle in self.choix_utilisateur:
                if "Peu importe" in self.choix_utilisateur[cle] or 0 in self.choix_utilisateur[cle] or self.choix_utilisateur[cle]==() :
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
            except TypeError:
                return
        
    def returntext(self):
        """Affiche le nom de l'école et a cote Refuse ou admis"""
        ecoleamoi=self.Ecole({choix:None for choix in self.choix_utilisateur})
        listeecoles=list(set(model.filtre({choix:None for choix in self.choix_utilisateur},None,None)))
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
        """Renvoie la note en forme de point pour tout les groupes"""
        
        self.noteconcours={noteconcours:{} for noteconcours in self.concours}
        for nom in self.concours :
            for cle in self.concours[nom]:
                if  0 in self.listbox_affichage[4].curselection():
                    self.noteconcours[nom][cle]=model.NoteCoefficient(self.concours[nom][cle],self.notematiere)+self.concours[nom][cle][-1]
                else :
                     self.noteconcours[nom][cle]=model.NoteCoefficient(self.concours[nom][cle],self.notematiere)
        return self.noteconcours
    
    def Ecole(self,choixutilisateur):
        """Retourne la liste des ecoles"""
        self.listeecoles=[]
        for nom in self.noteconcours:
            for cle in self.noteconcours[nom]:
                self.listeecoles+=model.filtre(choixutilisateur,cle,self.noteconcours[nom][cle])
        return list(set(self.listeecoles))
        
    def AffichageEcole(self):
        self.textaffiche="" 
        """Active le champs Ecole et supprime ce qu'il y avait écrit avant"""
        self.entry_ecole.configure(state="normal")
        self.entry_ecole.delete(0.7,'end');
        self.listeecoles=self.Ecole(self.choix_utilisateur)

        """Permet de génerer le texte affiché"""
        for texteaafficher in range(len(self.listeecoles)):
            self.textaffiche=self.textaffiche+"\n"+self.listeecoles[texteaafficher][0]+" "+self.listeecoles[texteaafficher][1]+" "+self.listeecoles[texteaafficher][2]
           
        """Affiche le texte et evite de pouvoir écrire par dessus"""  
        self.entry_ecole.insert(0.0,self.textaffiche)
        self.entry_ecole.configure(state="disabled")
         
if __name__ == '__main__':
    ChoixEcole()