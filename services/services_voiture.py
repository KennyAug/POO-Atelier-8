from data.crud_db import DataVoiture

class ServicesVoiture:

    def __init__(self):
        self.data = DataVoiture()
    def add_voiture(self, voiture):
        if voiture.id and voiture.marque and voiture.modele and voiture.annee and voiture.prix:
            self.data.ajouter_voiture(voiture)