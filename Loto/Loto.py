# -*- coding: utf-8 -*-

"""
# Script Name : Loto.py
# Author : Frédéric Puren
# Date : Novembre 2022
# Version 1.0

Mon tout premier script en python :)

Code basé sur la vidéo Youtube "APPRENDRE LE PYTHON #9 ? INTERFACE GRAPHIQUE (avec Tkinter)" de Graven - Développement
Le logiciel créé dans la vidéo génère des mots de passe aléatoire
Lien : https://www.youtube.com/watch?v=N4M4W7JPOL4


"""


from tkinter import *
import random

# fonction avec random.sample qui génere des nombres random entre 1 et 49 et entre 1 et 10
def generer_numero():
	resultat1 = random.sample(range(1,50),5)
	resultat_entry.delete(0, END)
	resultat_entry.insert(0, resultat1)

	resultat2 = random.sample(range(1,11),1)
	resultat_entry2.delete(0, END)
	resultat_entry2.insert(0, resultat2)
	

# créer une fenetre
fenetre = Tk()

# personnaliser la fenetre
fenetre.title("Générateur de tirage LOTO")
fenetre.geometry("720x480")
fenetre.minsize(620, 360)
fenetre.iconbitmap("boule_loto.ico")
fenetre.config(background='#C1C4F1')

# créer la frame (nouveau bloc ou sera le texte)
frame = Frame(fenetre, bg='#C1C4F1' )

# .pack pour afficher la frame dans la fenetre et le texte dans la frame (defini plus haut) - expand YES pour la mettre au milieu
frame.pack(expand=YES)

# création d'image, width et height : taille du canvas ou s'integre le .png
width = 300
height = 300
image = PhotoImage(file="bingo256.png")
#bd : bordure du canvas
canvas = Canvas(frame, width=width, height=height, bg='#C1C4F1', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
# au lieu de .pack pour afficher .grid pour afficher dans une grille
# row=0 : ligne 0 de la grille , column : colonne 0 de la grille, sticky : placement de l'image par rapport a la grille : W : West
canvas.grid(row=0, column=0, sticky=W)

# création d'une sous boite
frame_droite = Frame(frame, bg='#C1C4F1')
#la sous boite frame_droite est placé à droite de la frame principale (frame)
frame_droite.grid(row=0, column=1, sticky=W)

# ajouter un boutton qui sera dans la frame2
boutton = Button(frame_droite, text="Générer les numéros", font=("calibri", 20), bg='white', fg='#636BD9',command=generer_numero)
# afficher le bouton
boutton.pack(fill=X)

# ajouter un premier texte
	# font : police du texte
	# 40 taille de la police
	# bg pour background pour régler la couleur idem que celle de la fenetre
	# fg pour forground couleur du texte
texte_1 = Label(frame_droite, text="Numéros Gagnants", font=("calibri", 15), bg='#C1C4F1', fg='black')
texte_1.pack()

# creation d'un champ/entrée (input) pour rentré du texte, qui servira en l'occurence a afficher la réponse qd le bouton sera cliqué
resultat_entry = Entry(frame_droite, justify="center",font=("calibri", 15), bg='#C1C4F1', fg='black')
resultat_entry.pack()

texte_vide = Label(frame_droite, text="", font=("calibri", 15), bg='#C1C4F1', fg='black' )
texte_vide.pack()

texte_2 = Label(frame_droite, text="Numéro chance", font=("calibri", 15), bg='#C1C4F1', fg='black' )
texte_2.pack()

resultat_entry2 = Entry(frame_droite, justify="center", font=("calibri", 15), bg='#C1C4F1', fg='black')
resultat_entry2.pack()



#afficher la fenetre
fenetre.mainloop()
