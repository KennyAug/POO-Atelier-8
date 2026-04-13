from models.voiture import Voiture

from services.services_voiture import ServicesVoiture
service = ServicesVoiture()
#les ajouts que j'ai fait
v1 = Voiture("Lamborghini", "Urus", 2017, 60000.00, 202)
v2 = Voiture("Toyota", "Camry", 2007, 60000.00, 293)
v3 = Voiture("Bugatti", "Chiron", 2010, 3000000.00, 264)
v4 = Voiture("BMW", "M3", 2024, 250000.00, 212)

service.add_voiture(v1)
service.add_voiture(v2)
service.add_voiture(v3)
service.add_voiture(v4)

#supprimer un objet avec l'id
sv1 = Voiture("", "", "", "", 212)
service.retire_voiture(sv1)

#reccuperer les objet et les mettre dans une liste
voitures = service.appeller_voiture()
for voiture in voitures:
    print(voiture)

#pour modifier des objet
mv1 = Voiture("Ferrari", "Spider", 1999, 345000.00,212)
service.changer_voiture(mv1)