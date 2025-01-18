# Define the Player class.
import random
class Player:

    # Define the constructor.
    def __init__(self, name,depart=None):
        self.name = name
        self.current_room =depart
        self.history = []
        self.inventory={}
        self.pv=5
        if self.current_room:
            self.history.append(self.current_room.name)
     

    # Define the move method.
    
    def move(self, direction):

        if direction not in self.current_room.exits or self.current_room.exits[direction] is None:
            print("Vous ne pouvez pas aller dans cette direction.")
            return False
        # Get the next room from the exits dictionary of the current room.
        next_room = self.current_room.exits.get(direction)

        # If the next room is None, print an error message and return False.
        if next_room is None:
            print("\nAucune porte dans cette direction !\n")
            return False
        # test
        if self.current_room and self.current_room.name not in self.history:
            self.history.append(self.current_room.name)
        # Set the current room to the next room.
        #print(f"Historique mis à jour : {self.history}")
        self.current_room = next_room
        #self.history.append(self.current_room)
        #print(self.current_room.get_long_description())
       

        return True 
    def get_history(self):
        if not self.history :
            return "le joueur n'a pas encore parcourue la piece"
        return "->".join(self.history)
    #def get_inventory(self):
    def get_inventory(self):
        if not self.inventory :
            return "votre inventaire est vide"
        return "\n->".join([str(item) for item in self.inventory.keys()])
    
    def take_damage(self, amount):
        """
        Fait perdre des points de vie au joueur.
        
        Args:
            amount (int): Le nombre de points de vie à perdre.
        """
        self.pv -= amount
        if self.pv <= 0:
            self.pv = 0
            self.die()

    def heal(self, amount):
        """
        Soigne le joueur en ajoutant des points de vie.
        
        Args:
            amount (int): Le nombre de points de vie à restaurer.
        """
        self.pv += amount
        if self.pv > 5:  # On ne veut pas dépasser les 100 PV
            self.pv = 5

    def die(self,game):
        """
        Gestion de la mort du joueur.
        """
        print(f"{self.name} est mort !")
        # Le jeu est terminé si le joueur meurt
        game.finished = True  # Terminer le jeu
    def attack(self, character):
        """Le joueur attaque un PNJ."""
        print(f"{self.name} attaque {character.name}!")
        success_chance = random.randint(1, 10)  # Un nombre entre 1 et 10 pour la chance de succès
        if success_chance >= 3:  # Si la chance est supérieure ou égale à 5, le joueur inflige des dégâts
            damage = random.randint(1, 5)  # Dégâts infligés par le joueur
            character.take_damage(damage)
            print(f"{self.name} inflige {damage} dégâts à {character.name}.")
            if character.hp == 0:
                print(f"{character.name} a été tué par {self.name}!")
        else:
            print(f"{self.name} échoue à attaquer {character.name}.")
        

