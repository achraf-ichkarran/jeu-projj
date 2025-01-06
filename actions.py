# Description: The actions module.

# The actions module contains the functions that are called when a command is executed.
# Each function takes 3 parameters:
# - game: the game object
# - list_of_words: the list of words in the command
# - number_of_parameters: the number of parameters expected by the command
# The functions return True if the command was executed successfully, False otherwise.
# The functions print an error message if the number of parameters is incorrect.
# The error message is different depending on the number of parameters expected by the command.


# The error message is stored in the MSG0 and MSG1 variables and formatted with the command_word variable, the first word in the command.
# The MSG0 variable is used when the command does not take any parameter.
MSG0 = "\nLa commande '{command_word}' ne prend pas de paramètre.\n"
# The MSG1 variable is used when the command takes 1 parameter.
MSG1 = "\nLa commande '{command_word}' prend 1 seul paramètre.\n"
from directions import centralise_direction
from player import Player
from room import Room
from character import Character

class Actions:
    def go(game, list_of_words, number_of_parameters):
        """
        Déplace le joueur dans la direction spécifiée.
        La direction peut être une direction cardinale ou une variante (ex: 'est').

        Args:
            game (Game): L'objet du jeu.
            list_of_words (list): La liste des mots de la commande.
            number_of_parameters (int): Le nombre de paramètres attendu.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.
        """
        # Vérifie que le bon nombre de paramètres est fourni
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False

        # Récupère la direction et la standardise
        input_direction = list_of_words[1]
        direction = centralise_direction(input_direction)

        if not direction:
            print(f"Direction '{input_direction}' inconnue.")
            return False

        # Vérifie si une sortie existe dans cette direction
        player = game.player

        # Déplace le joueur vers la pièce correspondante
        player.move(direction)
        #print(player.current_room.get_long_description())
        return True

    def quit(game, list_of_words, number_of_parameters):
        """
        Quit the game.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game, ["quit"], 0)
        True
        >>> quit(game, ["quit", "N"], 0)
        False
        >>> quit(game, ["quit", "N", "E"], 0)
        False

        """
        l = len(list_of_words)
        # If the number of parameters is incorrect, print an error message and return False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Set the finished attribute of the game object to True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True

    def help(game, list_of_words, number_of_parameters):
        """
        Print the list of available commands.

        Args:
            game (Game): The game object.
            list_of_words (list): The list of words in the command.
            number_of_parameters (int): The number of parameters expected by the command.

        Returns:
            bool: True if the command was executed successfully, False otherwise.

        Examples:

        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game, ["help"], 0)
        True
        >>> help(game, ["help", "N"], 0)
        False
        >>> help(game, ["help", "N", "E"], 0)
        False

        """

        # If the number of parameters is incorrect, print an error message and return False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Print the list of available commands.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

    def historik(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        player = game.player
        print("\nHistorique des pièces parcourues :")
        print(player.get_history())
        return True
    def back(game,list_of_words,number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        player=game.player
        game.current_room=player.history[-1]
        print(f"vous revenez à'{game.current_room}'")
        return True
       
       
    def inventorix(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        player = game.player
        print("\nvotre inventaire:")
        print(player.get_inventory())
        return True
    def look(game, list_of_words, number_of_parameters) :
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        player=game.player
        
        print(game.player.current_room.get_inventory())
       
        return True 
    def take(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        player=game.player
        inventaire=game.player.inventory
        inventaire_room=game.player.current_room.inventory_rooms
        item_to_take = list_of_words[1]
        if inventaire_room == set() :
            print("piece est vide")
            return False
        
        for item in inventaire_room.copy():
            if item.name == item_to_take:
                inventaire[item] = inventaire.get(item, 0) + 1
                inventaire_room.remove(item)
                print(f"{item.name} a été ajouté à votre inventaire.")
        return  True
    def drop(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        player=game.player
        inventaire=game.player.inventory
        inventaire_room=game.player.current_room.inventory_rooms
        item_to_drop = list_of_words[1]
        if not inventaire :
            print("inventaire vide")
            return False
        
        for item in inventaire.copy():
            if item.name == item_to_drop:
                inventaire_room.add(item) 
                inventaire.pop(item)
                print(f"{item.name} a été depose dans {game.player.current_room.name}.")
        return  True
    def talk(game, list_of_words, number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG1.format(command_word=command_word))
            return False
        player = game.player
        character=list_of_words[1]
        return True

    

    
    

        
