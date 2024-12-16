# -*- coding: utf-8 -*-
fichier_ics = 'ADE_RT1_Septembre2023_Decembre2023.ics'

try:
    with open(fichier_ics, 'r', encoding='utf-8') as f:
        contenu = f.read()
        print(contenu)
except FileNotFoundError:
    print(f"Le fichier {fichier_ics} na pas été trouvé.")   
"""
Created on Mon Dec 16 08:49:35 2024

@author: GUEYE
"""

