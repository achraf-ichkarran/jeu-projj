# Define the Room class.

class Room:

    # Define the constructor. 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.inventory_rooms=set()
        self.exits = {}
        self.character_rooms={}
    
    # Define the get_exit method.
    def get_exit(self, direction):
        """
        Récupère la sortie associée à la direction spécifiée.

        Cette méthode retourne la sortie dans la direction donnée, ce qui peut représenter
        un changement de lieu, une porte, une zone de transition, ou tout autre type de 
        sortie dans l'application, selon la logique du programme.

        Args:
            direction (str): La direction vers laquelle on cherche une sortie.
                            Cela pourrait être une direction cardinale ('nord', 'sud', etc.) 
                            ou une autre forme de direction spécifique à l'application.

        Returns:
            Exit: L'objet représentant la sortie dans la direction spécifiée, ou `None` si aucune sortie n'existe dans cette direction.

        Raises:
            ValueError: Si la direction est invalide ou non reconnue.
        """


        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        """
        Récupère une chaîne de caractères représentant les sorties disponibles.

        Cette méthode retourne une chaîne formatée qui décrit les directions possibles pour quitter
        l'endroit actuel, sous forme de texte lisible pour l'utilisateur. Cela peut inclure les directions 
        cardinales ('nord', 'sud', etc.) et d'autres informations liées aux sorties accessibles.

        Args:
            None

        Returns:
            str: Une chaîne de caractères listant les directions des sorties disponibles.
        """
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        """
        Récupère une description longue et détaillée de l'objet.

        Cette méthode retourne une chaîne de caractères qui fournit une description complète
        de l'objet, incluant des détails supplémentaires qui ne sont pas présents dans une
        description courte ou sommaire. Cela peut inclure des informations sur les caractéristiques
        spécifiques, l'historique, ou d'autres éléments pertinents.

        Args:
            None

        Returns:
            str: Une chaîne de caractères contenant la description détaillée de l'objet.
        """
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
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
        inventory_list = "\n".join(str(item) for item in self.inventory_rooms)
        characters_list = "\n".join(f"{details.name}: {details.description}"  for details in self.character_rooms.values())

        resultat=[]
        if not self.inventory_rooms and self.character_rooms:
            return "piece vide"
        
        resultat.append(f"Objets présents :\n{inventory_list}")
        
        resultat.append(f"Personnages présents :\n{characters_list}")
        
        return "\n\n".join(resultat)