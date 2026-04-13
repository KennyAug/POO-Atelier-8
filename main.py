from models.voiture import Voiture

from services.services_voiture import ServicesVoiture

service = ServicesVoiture()

liste_voitures = service.appeller_voiture()
for v in liste_voitures:
    print(v)





