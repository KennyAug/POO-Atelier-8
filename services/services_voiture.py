from data.crud_db import DataVoiture

class ServicesVoiture:

    def __init__(self):
        self.data = DataVoiture()
    def add_voiture(self, voiture):
        if voiture.id and voiture.marque and voiture.modele and voiture.annee and voiture.prix:
            self.data.ajouter_voiture(voiture)
    def retire_voiture(self, voiture):
        if voiture.id:
            self.data.supprimer_voiture(voiture)
    def appeller_voiture(self):
        return self.data.recuperer_voiture()
    def changer_voiture(self, voiture):
        if voiture.id and voiture.marque and voiture.modele and voiture.annee and voiture.prix:
            self.data.modifier_voiture(voiture)

























