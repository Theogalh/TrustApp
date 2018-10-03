from app import db, app
from app.models.list import list_char
import datetime
import requests

CLASS = {
    1: "Warrior",
    2: "Paladin",
    3: "Hunter",
    4: "Rogue",
    5: "Priest",
    6: "Death Knight",
    7: "Shaman",
    8: "Mage",
    9: "Warlock",
    10: "Monk",
    11: "Druid",
    12: "Demon Hunter"
}

COLOR = {
    1: "#C79C6E",
    2: "#F58CBA",
    3: "#ABD473",
    4: "#FFF569",
    5: "#FFFFFF",
    6: "#C41F3B ",
    7: "#0070DE",
    8: "#40C7EB",
    9: "#8787ED",
    10: "#00FF96",
    11: "#FF7D0A",
    12: "#A330C9"
}

RACE = {
    1: "Humain",
    2: "Orc",
    3: "Nain",
    4: "Elfe de la nuit",
    5: "Mort vivant",
    6: "Tauren",
    7: "Gnome",
    8: "Troll",
    9: "Gobelin",
    10: "Elfe de sang",
    11: "Draenei",
    22: "Worgen",
    24: "Pandaren N",
    25: "Pandaren A",
    26: "Pandaren H",
    27: "Sacrenuit",
    28: "Tauren de Haut Roc",
    29: "Elfe du vide",
    30: "Draenei Sancteforge",
    34: "Nain sombrefer",
    36: "Orc mag'har",
}

char_item = db.Table('char_item',
                     db.Column('char_id', db.Integer, db.ForeignKey('character.id')),
                     db.Column('item_id', db.Integer, db.ForeignKey('item.id'))
                     )


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lists = db.relationship("List",
                            secondary=list_char,
                            back_populates='characters',
                            lazy='dynamic')
    items = db.relationship("Item",
                            secondary=char_item,
                            back_populates='characters',
                            lazy='dynamic')

    name = db.Column(db.String(64), index=True, unique=True)
    server = db.Column(db.String(64))
    region = db.Column(db.String(64))
    armory_link = db.Column(db.String(256))
    ilvl = db.Column(db.Integer, index=True)
    race = db.Column(db.String(64))
    classe = db.Column(db.String(64))
    raiderio = db.Column(db.Integer)
    raiderio_link = db.Column(db.String(256))
    color = db.Column(db.String(20))
    last_update = datetime.datetime.now()

    def __repr__(self):
        return '<Character {}>'.format(self.name)

    def refresh(self, index=0):
        if index > 3:
            return 404
        url = "https://{}.api.battle.net/wow/character/{}/{}?locale=fr_FR&apikey={}".format(
            self.region,
            self.server,
            self.name,
            app.config["BNET_APIKEY"]
        )
        r = requests.get(url + "&fields=items")
        if r.status_code != 200:
            return self.refresh(index+1)
        # TODO Creer les items
        r = r.json()
        self.ilvl = int(r["items"]['averageItemLevelEquipped'])
        self.classe = CLASS[int(r["class"])]
        self.color = COLOR[int(r["class"])]
        self.race = RACE[int(r["race"])]
        self.armory_link = "https://worldofwarcraft.com/fr-fr/character/{}/{}".format(
            self.server,
            self.name
        )
        url = 'https://raider.io/api/v1/characters/profile?region={}&realm={}&name={}&fields=mythic_plus_scores'.format(
            self.region,
            self.server,
            self.name
        )
        r = requests.get(url)
        if r.status_code != 200:
            self.raiderio = 0
        else:
            r = r.json()
            self.raiderio = r["mythic_plus_scores"]["all"]
            self.raiderio_link = r["profile_url"]
        self.last_update = datetime.datetime.now()
        db.session.commit()
        return 200


