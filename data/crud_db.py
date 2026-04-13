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
        con.close()
    def supprimer_voiture(self, voiture):
        con = self.connecter_db()
        crs = con.cursor()
        crs.execute("DELETE FROM voiture WHERE id = %s",
                    (voiture.id,)

        )
        con.commit()
        crs.close()
        con.close()
    def recuperer_voiture(self, voiture):
        con = self.connecter_db()
        crs = con.cursor()
        crs.execute("Select * from voiture ")
        v = crs.fetchall()
        voitures = []
        for s in v:
            voitures.append(s)
        crs.close()
        con.close()
