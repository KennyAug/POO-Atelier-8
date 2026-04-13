from models.voiture import Voiture

from services.services_voiture import ServicesVoiture

service = ServicesVoiture()
mv1 = Voiture("Ferrari", "Spider", 1999, 345000.00,212)
service.changer_voiture(mv1)




