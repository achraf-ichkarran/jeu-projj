# Define the Player class.

class Player:

    # Define the constructor.
    def __init__(self, name,depart=None):
        self.name = name
        self.current_room =depart
        self.history = []
        self.inventory={}
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
        # Set the current room to the next room.
        #print(f"Historique mis à jour : {self.history}")
        self.current_room = next_room
        #self.history.append(self.current_room)
        print(self.current_room.get_long_description())
       

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
        

