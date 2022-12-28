from datetime import datetime
from action import Action


temps_debut = datetime.now()

actions = Action.obtenir_liste_actions("actions.txt")


def bruteforce(montant_max, actions, best_porte_feuille=[]):
    """Algo du sac a dos"""
    if actions:
        profit_1, listeActions1 = bruteforce(montant_max, actions[1:], best_porte_feuille)
        action = actions[0]
        if action.prix <= montant_max:
            profit_2, listeActions2 = bruteforce(montant_max - action.prix, actions[1:], best_porte_feuille + [action])
            if profit_1 < profit_2:
                return profit_2, listeActions2

        return profit_1, listeActions1
    else:
        return sum([(Action.obtenir_gain_action(action)) for action in best_porte_feuille]), list(
            [action.nom for action in best_porte_feuille]
        )


best_wallet = bruteforce(500, actions)
print(best_wallet)
temps_fin = datetime.now()
print("temps d'éxécution: ", temps_fin - temps_debut, "\n")
