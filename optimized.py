from datetime import datetime
from action import Action

temps_debut = datetime.now()

actions = Action.obtenir_liste_actions("dataset1_Python+P7.csv")


def algo_optimise(capital, actions):
    """Alogorithme optimisé.
    On crée une matrice de w (capital) colonnes et n (nb actions) lignes qui enregistre
    le meilleur gain pour chaque ajout d'action.
    Il ne reste qu'à comparer la ligne avec celle du dessus.
    On a ainsi w * n possibilités.
    """
    capital = capital * 100
    matrice = [[0 for x in range(capital + 1)] for x in range(len(actions) + 1)]
    for i in range(1, len(actions) + 1):
        for w in range(1, capital + 1):
            if actions[i - 1].prix <= w:

                matrice[i][w] = max(
                    actions[i - 1].benefice + matrice[i - 1][w - actions[i - 1].prix], matrice[i - 1][w]
                )
            else:
                matrice[i][w] = matrice[i - 1][w]
    w = capital
    n = len(actions)
    porte_feuille_ideal = []

    while w >= 0 and n >= 0:
        action = actions[n - 1]
        if matrice[n][w] == matrice[n - 1][w - action.prix] + action.benefice:
            porte_feuille_ideal.append(action)
            w -= action.prix
        n -= 1
    wallet = porte_feuille_ideal

    return (
        matrice[-1][-1],
        list([(action.nom, action.prix) for action in wallet]),
        sum([(action.prix) / 100 for action in wallet]),
    )


gain, porteFeuille, depense = algo_optimise(500, actions)


print("\nBlaise bought: ")
depense = 0
for action in porteFeuille:
    print(action)
    depense += action[1] / 100

print("Total cost: ", depense)
print("Profit: ", round((float(gain) / 100), 2))


temps_fin = datetime.now()
print("\ntemps d'éxécution: ", temps_fin - temps_debut, "\n")
