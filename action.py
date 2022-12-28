class Action:
    def __init__(self, nom, prix, benefice) -> None:
        self.nom = nom
        self.prix = prix
        self.benefice = benefice

    def __str__(self) -> str:
        """Affichage au print"""
        return f"{self.nom}: {self.prix} €, bénéfice: {self.benefice}"

    def obtenir_liste_actions(fichier):
        actions = []
        with open(fichier, "r+") as f:
            lines = f.readlines()
            for line in lines:
                nom, prix, benefice = line.split()
                nom = Action(nom, int(prix), benefice)
                actions.append(nom)
        return actions

    def obtenir_gain_action(action):
        gain = (int(action.prix) * int(action.benefice[:-1])) / 100
        return gain
