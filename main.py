from models.voiture import Voiture

from services.services_voiture import ServicesVoiture

service = ServicesVoiture()


sv1 = Voiture("", "", "","", 202)
service.retire_voiture(sv1)





