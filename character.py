DEBUG= True
import random
from room import Room
class Character:
    def __init__(self,name,description,current_room,msgs,hp,can_move) :
        self.name=name
        self.description=description
        self.current_room=current_room
        self.msgs=msgs
        self.hp=hp
        self.can_move = can_move
    def __str__(self):
        return f"{self.name}: {self.description} (msgs: {self.msgs})"
    def to_dict(self):
        return {self.name: [self.description, self.msgs]}
    def get_msg(self):
        if not self.msgs :
            print(f"{self.name} n'a plus de message à dire.")
            return None
        msg=self.msgs[0]
        self.msgs.pop(0)
        return msg
        
    def move(self):
        # Le personnage a une chance sur deux de se déplacer
        if self.can_move:
            # Le personnage a une chance sur deux de se déplacer
            if random.choice([True, False]):
                # Choisir une pièce adjacente au hasard
                exits = list(self.current_room.exits.values())
                if exits:
                    new_room = random.choice(exits)
                    print(f"DEBUG: {self.name} se déplace de {self.current_room.name} à {new_room.name}")
                    self.current_room = new_room
                    return True
                else:
                    print(f"DEBUG: {self.name} ne peut pas se déplacer, aucune sortie.")
            else:
                print(f"DEBUG: {self.name} reste dans {self.current_room.name}")
        else:
            print(f"DEBUG: {self.name} reste dans {self.current_room.name} car il est statique.")
        return False
        

    def take_damage(self, amount):
        """Réduit les PV du PNJ lorsqu'il prend des dégâts."""
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            self.die()

    def die(self):
        """Le PNJ meurt, un message est affiché."""
        print(f"{self.name} est mort !")
        self.current_room.character_rooms.pop(self.name)  # Retirer le PNJ de la pièce

    def attack(self, player):
        """Le PNJ attaque le joueur."""
        print(f"{self.name} vous attaque !")
        damage = random.randint(1, 3)  # Dégâts infligés par le PNJ
        player.take_damage(damage)
        print(f"{self.name} vous inflige {damage} dégâts.")


