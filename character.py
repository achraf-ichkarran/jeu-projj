

class Character:
    def __init__(self,name,description,current_room,msgs) :
        self.name=name
        self.description=description
        self.current_room=current_room
        self.msgs=msgs
    def __str(self):
        return f"{self.name}: {self.description} (msgs: {self.msgs})"
    def to_dict(self):
        return {self.name: [self.description, self.msgs]}
from room import Room
corridor_infini = Room(
    "Corridor Infini",
    "Un couloir interminable avec des néons grésillants et un sol carrelé beige.")
Léo = Character("Léo", "le Vagabond mystérieux",corridor_infini , ["Je suis Léo ","Welcome to the backrooms where there is no begining ot ending !"])
chambre_rouge = Room(
    "Chambre Rouge",
    "Une pièce rouge oppressante avec des symboles cryptiques sur les murs.")
Sylvia = Character("Sylvia ", "la Mystique énigmatique", chambre_rouge, [" Les murs parlent, mais seuls les esprits éveillés peuvent entendre leur secret."])
labyrinthe_de_portes = Room(
    "Labyrinthe de Portes",
    "Un labyrinthe avec des portes qui mènent à différents endroits.")
Igor = Character("Igor", "le Gardien grincheux",labyrinthe_de_portes, ["Ah, encore des visiteurs. Vous voulez sortir ? Trouvez la porte, ou restez à jamais ! "])
chambre_du_gardien = Room(
    "Chambre du Gardien",
    "Une grande salle avec un trône au centre, occupée par un boss imposant.")
Kragnra = Character("Kragnar", "le Colosse impitoyable",chambre_du_gardien, ["Vous voulez le dernier chiffre ? Alors prouvez votre valeur, faibles créatures !"])