# AlgoInvest&Trade

ALgortihmes permettant d'obtenir le meilleur choix d'investissement avec un portefeuille d'action pour un montant donné.
L'agortihme de forcebrute (bruteforce.py) calcule toutes les possibilités et donne le meilleur choix mais peut très vite devenir inutilisable quand le nombre d'actions augmente (temps de calcul exponentiel, il ne fonctionne qu'avec le fichier actions.txt)
L'algorithme optimisé (optimized.py) permet de trouver le compromis entre fiabilité et temps de calcul.(utilisation possible avec dataset1_Python+P7.csv et dataset2_Python+P7.csv)
Le fichier action.py permet de traiter les fichiers de données(nettoyage + formatage)

## Utilisation du programme:

Créez un répertoire dédié et placez-vous dedans:

```
mkdir AlgoInvest&Trade
cd /AlgoInvest&Trade
```

Importez le projet:

```
git clone https://github.com/Bl4is3/AlgoInvest-Trade.git
```

Pour obtenir le meilleur rendement avec le portefeuille de 20 actions, utilisez le fichier bruteforce.py:

```
python bruteforce.py
```

Pour obtenir le meilleur choix avec les datasets, 
Commencez par choisir le dataset testé à la ligne 6 du programme puis:

```
python optimized.py
```




