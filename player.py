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
        """
        Déplace l'objet dans la direction spécifiée.

        Cette méthode modifie la position de l'objet en fonction de la direction donnée.
        La direction peut être une chaîne représentant une direction cardinale (par exemple : 'nord', 'sud', 'est', 'ouest') 
        ou d'autres valeurs possibles selon l'application.

        Args:
            direction (str): La direction vers laquelle déplacer l'objet. 
                            Les valeurs valides peuvent inclure 'nord', 'sud', 'est', 'ouest', etc.

        Returns:
            None

        Raises:
            ValueError: Si la direction fournie est invalide ou non reconnue.
        """

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
        
      
        self.current_room = next_room
       

        return True 
    def get_history(self):
        """
        Récupère l'historique des actions ou événements associés à l'objet.

        Cette méthode retourne une liste ou une autre structure contenant les actions
        ou événements passés qui ont été enregistrés dans l'objet. Cela peut inclure des
        mouvements, des décisions, ou tout autre type d'action selon l'application.

        Args:
            None

        Returns:
            list: Une liste contenant l'historique des actions sous forme de chaînes de caractères ou d'objets.
                L'ordre des éléments reflète l'ordre chronologique des événements.
        """

        if not self.history :
            return "le joueur n'a pas encore parcourue la piece"
        return "->".join(self.history)
    #def get_inventory(self):
    def get_inventory(self):
        """
        Récupère l'inventaire des objets ou éléments associés à l'objet.

        Cette méthode retourne une liste ou une autre structure représentant les éléments
        actuellement présents dans l'inventaire. Cela peut inclure des objets, des ressources
        ou toute autre forme de stockage d'items selon l'application.

        Args:
            None

        Returns:
            list: Une liste contenant les éléments de l'inventaire, où chaque élément
                peut être un objet, une chaîne de caractères, ou un autre type de donnée.
        """
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
        

