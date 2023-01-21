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
                if "price" not in line:
                    if "%" in line:
                        nom, prix, benefice = line.split()
                        prix = int(prix)
                        benefice = int(benefice[:-1])
                        gain = (benefice * int(prix)) / 100
                    else:
                        nom, prix, benefice = line.split(",")
                        prix = int(float(prix) * 100)
                        benefice = int(float(benefice) * 100)
                        gain = round(float((prix * benefice) / 10000), 2)
                    if prix > 0:
                        nom = Action(nom, prix, gain)
                        actions.append(nom)
        return actions
