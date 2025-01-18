import random
from config import DEBUG
from room import Room
class Character:
    def __init__(self,name,description,current_room,msgs) :
        self.name=name
        self.description=description
        self.current_room=current_room
        self.msgs=msgs
    def __str__(self):
        return f"{self.name}: {self.description} (msgs: {self.msgs})"
    def to_dict(self):
        """
        Convertit l'objet en un dictionnaire représentant ses attributs et leurs valeurs.

        Returns:
            dict: Un dictionnaire contenant les attributs de l'objet comme paires clé-valeur.
        """
        return {self.name: [self.description, self.msgs]}
    def get_msg(self):
        """
        Récupère le message associé à l'objet.

        Returns:
            str: Le message stocké ou généré par l'objet.
        """
        if not self.msgs :
            print(f"{self.name} n'a plus de message à dire.")
            return None
        msg=self.msgs[0]
        self.msgs.pop(0)
        return "\n->".join(msg)
        
        
    
        
    def move(self):
        """
        Déplace l'objet ou le joueur dans une direction spécifiée sur un certain nombre de pas.

        Args:
            direction (str): La direction du déplacement (ex: 'nord', 'sud', 'est', 'ouest').
            steps (int): Le nombre de pas à parcourir dans la direction donnée.

        Returns:
            bool: True si le déplacement a été effectué avec succès, False sinon.
        """
        # Le personnage a une chance sur deux de se déplacer
        if random.choice([True, False]):
            # Choisir une pièce adjacente au hasard
            exits = list(self.current_room.exits.values())
            if exits:
                new_room = random.choice(exits)
                if DEBUG:
                    print(f"DEBUG: {self.name} se déplace de {self.current_room.name} à {new_room.name}")
                self.current_room = new_room
                return True
            else:
                if DEBUG:
                    print(f"DEBUG: {self.name} ne peut pas se déplacer, aucune sortie.")
        else:
            if DEBUG:
                print(f"DEBUG: {self.name} reste dans {self.current_room.name}")
        return False


