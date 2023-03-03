from fonctions import *

tab = entree()
#tab = gen_rdm()
mots = mots_dans_grille(tab)
for i in range(len(mots)//10):
       print(mots[i*10:i*10+10])
print(mots[len(mots)//10*10:])
