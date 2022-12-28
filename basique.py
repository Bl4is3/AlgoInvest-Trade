from itertools import chain, combinations
from action import Action, get_actions


def powerset():
    """Fonction utilisant le module itertools"""
    money = 500

    d = 0

    actions = get_actions()

    def powerset(list_name):
        s = list(list_name)
        return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

    best_comb_cout = 0
    best_gain = 0
    for x in powerset(actions):
        d += 1
        l = len(x)
        cout = 0
        gain = 0
        for i in range(0, l):
            taux = int(x[i][2].replace("%", "")) / 100
            cout += int(x[i][1])
            gain += int(x[i][1]) * taux
        if cout <= money:
            if gain > best_gain:
                k = i
                best_comb_cout = cout
                best_gain = gain
                best_comb = x
    print("nb de possibilités: ", d)
    e = 0
    f = 0
    print("Meilleur choix: ")
    for c in best_comb:
        print(c)
        taux_rendement = int(c[2].replace("%", ""))
        e += c[1]
        f += c[1] * (taux_rendement / 100)

    print("somme dépensée: ", best_comb_cout)
    print("Gain:", best_gain)


def nb_possibilite(nombre):
    if nombre == 1:
        return 1
    else:
        return nombre * nb_possibilite(nombre - 1)


def all_combinations(i, actions, combinaisons=[]):
    """Fonction perso"""
    if i >= 16:
        return combinaisons
    else:
        if i == 0:
            for action in actions:
                combinaisons.append(action[0][7:])
                # with open("results.txt", "a") as r:
                #     r.write(action[0][7:])
                #     r.write("\n")
            all_combinations(i + 1, actions, combinaisons)

        else:
            for combinaison in combinaisons:
                if "," not in combinaison:
                    dernier_indice = int(combinaison)
                else:
                    dernier_indice = int(combinaison.split(",")[-1])
                for d in range(dernier_indice, len(actions)):
                    combi = combinaison + "," + str(actions[d][0][7:])
                    combinaisons.append(combi)
                    # combi = []
                    # with open("results.txt", "a") as r:
                    #     r.write(str(combi))
                    #     r.write("\n")
            all_combinations(i + 1, actions, combinaisons)


nb = nb_possibilite(20)
print(nb)
