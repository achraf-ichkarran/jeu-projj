# Description: Game class

# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from directions import (DIRECTIONS,centralise_direction)
from item import Item

def standardize_direction(input_direction):
    return DIRECTIONS.get(input_direction, None)

class Game:

    # Constructor
    def __init__(self):    
        self.finished = False
        self.rooms = []
        self.commands = {}
        self.player = None
        
        
    
    # Setup the game
    def setup(self,name,Character):
        self.name=name
        self.Character=Character
    def __str__(self):
        return f"{self.name}: {self.charcater}"
    
    def to_dict(self):
        return {self.name: [self.charcater]}
  
        

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
       
       
        # Setup items
        hache=Item("hache","une hache qui tranche ta mere","5")
        cle=Item("cle","une cle qui ouvre les portes","0.5")
        lampe=Item("lampe","une lampe qui fait de la lumiere","1")
        
        # Setup rooms
self.corridor_infini = Room(
    "Corridor Infini",
    "Un couloir interminable avec des néons grésillants et un sol carrelé beige.",
)
self.rooms.append(corridor_infini)
bureau_abandonne = Room(
    "Bureau Abandonné",
    "Un espace de bureaux désordonné où des téléphones sonnent sporadiquement.",
)
self.rooms.append(bureau_abandonne)
souterrain_inonde = Room(
    "Souterrain Inondé",
    "Une pièce immergée avec des conduites rouillées et des reflets inquiétants.",
)
self.rooms.append(souterrain_inonde)
chambre_rouge = Room(
    "Chambre Rouge",
    "Une pièce rouge oppressante avec des symboles cryptiques sur les murs.",
)
self.rooms.append(chambre_rouge)
labyrinthe_de_portes = Room(
    "Labyrinthe de Portes",
    "Un labyrinthe avec des portes qui mènent à différents endroits.",
)
self.rooms.append(labyrinthe_de_portes)
chambre_du_gardien = Room(
    "Chambre du Gardien",
    "Une grande salle avec un trône au centre, occupée par un boss imposant.",
)
self.rooms.append(chambre_du_gardien)
        # Create invontory for rooms
        corridor_infini.inventory_rooms = set()
        bureau_abandonne.inventory_rooms = set()
        souterrain_inonde.inventory_rooms = set()
        chambre_rouge.inventory_rooms = set()
        labyrinthe_de_portes.inventory_rooms= set()
        chambre_du_gardien.inventory_rooms = set()

corridor_infini.exits = {"E": bureau_abandonne}
bureau_abandonne.exits = {"E": souterrain_inonde, "O": corridor_infini}
souterrain_inonde.exits = {"S": chambre_rouge, "O": bureau_abandonne}
chambre_rouge.exits = {"N": souterrain_inonde, "S": labyrinthe_de_portes}
labyrinthe_de_portes.exits = {"N": chambre_rouge, "E": chambre_du_gardien}
chambre_du_gardien.exits = {"O": labyrinthe_de_portes}
        

        # Setup player and starting room

        self.player = Player(input("\nEntrez votre nom: "))r
        self.player.current_room = corridor_infini

    # Play the game
    def play(self):
        self.setup()
        self.print_welcome()
        # Loop until the game is finished
        while not self.finished:
            # Get the command from the player
            self.process_command(input("> "))
        return None

    # Process the command entered by the player
    def process_command(self, command_string) -> None:
            
                

        # Split the command string into a list of words
        list_of_words = command_string.split(" ")
        

        command_word = list_of_words[0]
        if command_word=="":
            return
        if command_word == "go":
            if len(list_of_words) < 2:
                print("Vous devez préciser une direction après 'go'.")
                return
            direction = standardize_direction(list_of_words[1])
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
        print(f"\nBienvenue {self.player.name} dans ce jeu d'aventure !")
        print("Entrez 'help' si vous avez besoin d'aide.")
        print(self.player.current_room.get_long_description())
    # test

def main():
    # Create a game object and play the game
    Game().play()
    

if __name__ == "__main__":
    main()
