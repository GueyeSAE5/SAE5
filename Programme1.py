# -*- coding: utf-8 -*-
fichier_ics = 'evenementSAE_15.ics'

try:
    with open(fichier_ics, 'r', encoding='utf-8') as f:
        contenu = f.read()
        print(contenu)
except FileNotFoundError:
    print(f"Le fichier {fichier_ics} na pas été trouvé.")        
"""
Created on Fri Dec  6 11:44:15 2024

@author: GUEYE
"""

