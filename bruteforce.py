from datetime import datetime
from action import Action


temps_debut = datetime.now()

actions = Action.obtenir_liste_actions("dataset1_Python+P7.csv")


def bruteforce(capital, actions, best_porte_feuille=[]):
    """Algo du sac a dos
    Pour chaque action, on prend en compte la meileure option entre l'utiliser ou pas.
    On a donc 2^n(nb actions)  possibilités
    """
    if actions:
        profit_1, listeActions1 = bruteforce(capital, actions[1:], best_porte_feuille)
        action = actions[0]
        if action.prix <= capital:
            profit_2, listeActions2 = bruteforce(capital - action.prix, actions[1:], best_porte_feuille + [action])
            if profit_1 < profit_2:
                return profit_2, listeActions2

        return profit_1, listeActions1
    else:
        return sum([action.benefice for action in best_porte_feuille]), list(
            [action.nom for action in best_porte_feuille]
        )


best_wallet = bruteforce(500, actions)
print(best_wallet)
temps_fin = datetime.now()
print("temps d'éxécution: ", temps_fin - temps_debut, "\n")
