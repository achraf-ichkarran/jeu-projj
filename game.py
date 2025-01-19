# Description: Game class

# Import modules

from character import Character
from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item
from doors import Door





class Game:

    # Constructor
    def __init__(self):    
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        self.victory_room=None
        self.DIRECTIONS = {
        "N": "N", "North": "N", "north": "N",
        "E": "E", "Est": "E", "est": "E",
        "S": "S", "Sud": "S", "sud": "S",
        "O": "O", "Ouest": "O", "ouest": "O",
        "U": "U", "Up": "U", "up": "U",
        "D": "D", "Down": "D", "down": "D"
        }  

    def centralise_direction(self, input_direction):
        
       """
    Standardise une direction donnée en une forme uniforme.

    Cette fonction prend une direction en entrée (ex : 'Nord', 'nord-est') 
    et la convertit en une représentation standardisée (ex : 'N', 'NE') 
    pour une utilisation cohérente dans le système.

    Args:
        input_direction (str): La direction à standardiser. 
            Peut inclure des variations comme 'Nord', 'nord', 'N', ou 'nord-est'.

    Returns:
        str: La direction standardisée, exprimée sous un format court (ex : 'N', 'NE').

    Raises:
        ValueError: Si la direction fournie n'est pas reconnue comme valide.
    """
       return self.DIRECTIONS.get(input_direction, None)
  
    
    # Setup the game
    def setup(self):
         """
        Configure ou initialise les composants nécessaires de l'objet.

        Cette méthode est utilisée pour préparer l'objet à son utilisation, en configurant
        les paramètres, en initialisant les ressources ou en effectuant toute autre
        étape d'installation requise.

        Args:
            None

        Returns:
            None
        """


        # Setup commands

         help = Command("help", " : afficher cette aide", Actions.help, 0)
         self.commands["help"] = help
         quit = Command("quit", " : quitter le jeu", Actions.quit, 0)
         self.commands["quit"] = quit
         go = Command("go", " <direction> : se déplacer dans une direction cardinale (N, E, S, O)", Actions.go, 1)
         self.commands["go"] = go
         historique = Command("historique", " : afficher l'historique", Actions.historik, 0)
         self.commands["historique"] = historique
         back=Command("back"," : retour en arriere",Actions.back,0)
         self.commands["back"] = back
         inventaire=Command("inventaire"," : voir l'inventaire",Actions.inventorix,0)
         self.commands["inventaire"] = inventaire
         inspecter=Command("inspecter"," : inspecter la piece",Actions.look,0)
         self.commands["inspecter"] = inspecter
         prendre=Command("prendre"," : prendre un objet",Actions.take,1)
         self.commands["prendre"] = prendre
         poser=Command("poser"," : poser un objet",Actions.drop,1)
         self.commands["poser"] = poser
         parler=Command("parler"," : parler a un PNJ",Actions.talk,1)
         self.commands["parler"] = parler
         attaque = Command("attaquer", " <nom_du_PNJ> : attaquer un PNJ dans la pièce", Actions.attack, 1)
         self.commands["attaquer"] = attaque
       
        # Setup items
         indice=Item("indice","note laisser par un survivant:\n le code de la porte est le numero de bureau du meilleur prof de l'ESIEE","5")

        
         porte_1=Door("bureau","5454")
         porte_2=Door("bureau","5454")

        # Setup rooms
         corridor_infini = Room("Corridor Infini","Un couloir interminable avec des néons grésillants et un sol carrelé beige.",)
         self.rooms.append(corridor_infini)
         bureau_abandonne = Room("Bureau Abandonné","Un espace de bureaux désordonné où des téléphones sonnent sporadiquement.",)
         self.rooms.append(bureau_abandonne)
         souterrain_inonde = Room("Souterrain Inondé","Une pièce immergée avec des conduites rouillées et des reflets inquiétants.",)
         self.rooms.append(souterrain_inonde)
         chambre_rouge = Room("Chambre Rouge","Une pièce rouge oppressante avec des symboles cryptiques sur les murs.",)
         self.rooms.append(chambre_rouge)
         labyrinthe_de_portes = Room("Labyrinthe de Portes","Un labyrinthe avec des portes qui mènent à différents endroits.",)
         self.rooms.append(labyrinthe_de_portes)
         chambre_du_gardien = Room("Chambre du Gardien","Une grande salle avec un trône au centre,.",)
         self.rooms.append(chambre_du_gardien)
         piege= Room("piege","",)
         self.rooms.append(piege)
  
        
        # Create invontory for rooms
         corridor_infini.inventory_rooms.add(indice)

        #creation de PNJ
         vagabond=Character("vagabond", "homme perdue",bureau_abandonne , ["vous etes qui !!!","je me cache ici depuis 11 ans","vous trouverais une porte bloquer vers le sud","un indice est cachée dans le couloir j'ai trop peur d'aller le chercher"],5,can_move=False)
         calamitee_1=Character("calamitée", "créature nauséabond",souterrain_inonde , ["aaaaggghhh"],5,can_move=False)
         calamitee_2=Character("calamitée", "créature nauséabond",chambre_rouge , ["aaaaggghhh"],5,can_move=False)
         calamitee_3=Character("calamitée", "créature nauséabond" ,labyrinthe_de_portes, ["aaaaggghhh"],5,can_move=True)
         calamitee_4=Character("calamitée", "créature nauséabond",souterrain_inonde , ["aaaaggghhh"],5,can_move=True)
        
        #initialisation des sorties
         corridor_infini.exits = {"E": bureau_abandonne}
         bureau_abandonne.exits = {"E": souterrain_inonde, "O": corridor_infini}
         souterrain_inonde.exits = {"S": chambre_rouge, "O": bureau_abandonne}
         chambre_rouge.exits = {"N": souterrain_inonde, "S": labyrinthe_de_portes}
         labyrinthe_de_portes.exits = {"N": chambre_rouge, "E": (chambre_du_gardien,porte_1),"S":(piege,porte_2)}
         chambre_du_gardien.exits = {"__": corridor_infini}
         piege.exits={"__":corridor_infini}

        # Ajout de personnages aux salles
         bureau_abandonne.character_rooms["vagabond"] = vagabond
         souterrain_inonde.character_rooms["calamitée"] = calamitee_1
         labyrinthe_de_portes.character_rooms["calamitée"] = calamitee_3
         chambre_rouge.character_rooms["calamitée"] = calamitee_2
         
    
    
        #Ajout des pieces de victoire et de defaite
         self.victory_room=chambre_du_gardien
         self.loose_room=piege



        








        


        # Setup player and starting room

         self.player = Player(input("\nEntrez votre nom: "))
         self.player.current_room = corridor_infini

    # Play the game
    def play(self):
        """
        Lance l'action principale associée à l'objet.

        Cette méthode démarre ou exécute une fonctionnalité clé, comme le lancement d'un jeu,
        la lecture d'un média, ou l'activation d'une séquence d'actions.

        Args:
            None

        Returns:
            None
        """
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            for room in self.rooms:
                for character in room.character_rooms.values():
                    character.move()
            # Get the command from the player 
            self.process_command(input("> "))
        return None


    # Process the command entered by the player
    def process_command(self, command_string) -> None:
        """
        Traite une commande donnée sous forme de chaîne de caractères.

        Cette méthode analyse et exécute l'action associée à la commande fournie par l'utilisateur.
        Elle peut inclure la validation, l'analyse syntaxique, et l'exécution de la commande.

        Args:
            command_string (str): La commande à traiter. 
                Doit être une chaîne valide correspondant à une action reconnue.

        Returns:
            None

        Raises:
            ValueError: Si la commande est vide ou invalide.
            NotImplementedError: Si la commande est valide mais non encore implémentée.
        """
            
                

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")
        

        command_word = list_of_words[0]
        if command_word=="":
            return
        if command_word == "go":
            if len(list_of_words) < 2:
                print("Vous devez préciser une direction après 'go'.")
                return
            direction = self.centralise_direction(list_of_words[1])
            if not direction:
                print(f"Direction '{list_of_words[1]}' non reconnue.")
                return

        # If the command is not recognized, print an error message
        if command_word not in self.commands.keys():
            print(f"\nCommande '{command_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
        # If the command is recognized, execute it
       
        else:
            command = self.commands[command_word]
            command.action(self, list_of_words, command.number_of_parameters)

    # Print the welcome message
    def print_welcome(self):
        """
        Affiche un message de bienvenue ou d'introduction.

        Cette méthode est utilisée pour accueillir l'utilisateur et l'informer sur
        le contexte ou l'état actuel de l'application, généralement au démarrage.

        Args:
            None

        Returns:
            None
        """
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        print(self.player.current_room.get_long_description())
    # test

def main():
    """
    Point d'entrée principal du programme.

    Cette fonction initialise les ressources, configure les paramètres nécessaires,
    et lance les processus principaux de l'application. Elle peut inclure 
    des étapes comme le traitement des arguments de ligne de commande,
    la configuration des logs ou l'exécution du flux principal du programme.

    Args:
        None

    Returns:
        None
    """
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
