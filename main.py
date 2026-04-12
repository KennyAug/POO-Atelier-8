from models.voiture import Voiture

from services.services_voiture import ServicesVoiture

service = ServicesVoiture()
v1 = Voiture("Lamborghini", "Urus", "2017", 60000.00, 202)
service.add_voiture(v1)