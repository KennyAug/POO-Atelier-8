import json
import mysql.connector

from models.voiture import Voiture
class DataVoiture:
    def connecter_db(self):
        with open("./data/config.json","r",encoding="utf-8") as j:
            config = json.load(j)
        connection = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        return connection
    def ajouter_voiture(self, voiture):
        con = self.connecter_db()
        crs = con.cursor()
        crs.execute("INSERT INTO voiture (id, marque, modele, annee, prix) VALUES (%s, %s, %s, %s, %s)",
                    (voiture.id, voiture.marque, voiture.modele, voiture.annee, voiture.prix)
        )
        con.commit()
        crs.close()
        crs.close()
