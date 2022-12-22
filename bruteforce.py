from itertools import chain, combinations
from datetime import datetime

temps_debut = datetime.now()

actions = []
with open("actions.txt", "r+") as f:
    lines = f.readlines()
    for line in lines:
        nom, prix, rendement = line.split()
        actions.append((nom, int(prix), rendement))


def powerset():
    """Fonction utilisant le module itertools"""
    money = 500

    d = 0

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


def nb_possibilite(nombre):
    if nombre == 1:
        return 1
    else:
        return nombre * nb_possibilite(nombre - 1)


nb = nb_possibilite(20)
print(nb)


def bruteforce(montant_max, actions, best_porte_feuille=[]):
    """Algo du sac a dos"""
    if actions:
        val1, lstVal1 = bruteforce(montant_max, actions[1:], best_porte_feuille)
        val = actions[0]
        if val[1] <= montant_max:
            val2, lstVal2 = bruteforce(montant_max - val[1], actions[1:], best_porte_feuille + [val])
            if val1 < val2:
                return val2, lstVal2

        return val1, lstVal1
    else:
        return sum([((int(i[1]) * int(i[2][:-1])) / 100) for i in best_porte_feuille]), best_porte_feuille


# best_wallet = bruteforce(500, actions)
# print(best_wallet)
time_wallet = datetime.now()
print("temps d'éxécution bruteforce: ", time_wallet - temps_debut, "\n")


# powerset()
time_powerset = datetime.now()
print("temps d'éxécution powerset: ", time_powerset - time_wallet, "\n")
comb = all_combinations(0, actions)


temps_fin = datetime.now()
print("temps d'éxécution algo_perso: ", temps_fin - time_powerset, "\n")
print("temps d'éxécution total: ", temps_fin - temps_debut, "\n")
