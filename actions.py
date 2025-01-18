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

from player import Player
from room import Room
from character import Character
import random

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
            print(f"Erreur : Commande '{command_word}' mal formée.")
            return False
        # Récupère la direction et la standardise
        input_direction = list_of_words[1]
        direction = game.centralise_direction(input_direction)
        if not direction:
            print(f"Direction '{input_direction}' inconnue.")
            return False
        player = game.player
        current_room = player.current_room
        # Vérifie si la sortie existe dans la direction spécifiée
        if input_direction in current_room.exits:
            exit_or_door = current_room.exits[input_direction]
            # Si la sortie est un tuple (porte, salle)
            if isinstance(exit_or_door, tuple):
                next_room, door = exit_or_door  # Extraction de la salle et de la porte
                # Si la porte est verrouillée
                if door.is_locked():
                    print(f"La porte {door.name} est verrouillée. Entrez le code pour l'ouvrir :")
                    input_code = input("Code : ")
                    # Vérification du code
                    if door.unlock(input_code):
                        print("La porte est maintenant déverrouillée.")
                        player.move(input_direction)  # Déplace le joueur vers la salle suivante
                        player.current_room = next_room
                        print(player.current_room.get_long_description())
                    else:
                        print("Code incorrect. La porte reste verrouillée.")
                        return False
                else:
                    # Si la porte n'est pas verrouillée
                    player.move(input_direction)
                    player.current_room = next_room
                    print(player.current_room.get_long_description())
                    if next_room.character_rooms:
                        for character in next_room.character_rooms.values():
                            print(f"({character.name}) est ici.")
                            atak = input("Voulez-vous attaquer ce PNJ ? (oui/non): ")
                            if atak == 'oui':
                                player.attack(character)
                            else:
                                character.talk()
            else:
                # Si la sortie n'est pas un tuple (porte, salle), déplace simplement le joueur
                player.move(input_direction)
                print(player.current_room.get_long_description())
            if player.current_room == game.victory_room:
                print(f"Félicitations {player.name} ! Vous avez gagné.")
                game.finished = True  # Fin du jeu
        else:
            print(f"Il n'y a pas de sortie dans la direction '{input_direction}'.")
            return False
        return True




    def quit(game, list_of_words, number_of_parameters):
        """
        Quitter le jeu.

        Arguments :
            game (Game) : L'objet du jeu.
            list_of_words (list) : La liste des mots dans la commande.
            number_of_parameters (int) : Le nombre de paramètres attendus par la commande.

        Retourne :
            bool : True si la commande a été exécutée avec succès, False sinon.

        Exemples :
        """

        """
        l = len(list_of_words)
        # Si le nombre de paramètres est incorrect, afficher un message d'erreur et retourner False.
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Définir l'attribut finished de l'objet game à True.
        player = game.player
        msg = f"\nMerci {player.name} d'avoir joué. Au revoir.\n"
        print(msg)
        game.finished = True
        return True
        """
    def help(game, list_of_words, number_of_parameters):
        """
        Afficher la liste des commandes disponibles.

        Arguments :
            game (Game) : L'objet du jeu.
            list_of_words (list) : La liste des mots dans la commande.
            number_of_parameters (int) : Le nombre de paramètres attendus par la commande.

        Retourne :
            bool : True si la commande a été exécutée avec succès, False sinon.

        Exemples :
        """

        # Si le nombre de paramètres est incorrect, afficher un message d'erreur et retourner False.
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False

        # Afficher la liste des commandes disponibles.
        print("\nVoici les commandes disponibles:")
        for command in game.commands.values():
            print("\t- " + str(command))
        print()
        return True

    def historik(game, list_of_words, number_of_parameters):
        """
        Affiche l'historique des actions du joueur.

         Args:
            game (Game): L'objet du jeu contenant les informations sur le joueur et l'environnement.
            list_of_words (list): La liste des mots de la commande.
            number_of_parameters (int): Le nombre de paramètres attendu.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.
        """
        # Vérifie si le nombre d'arguments est correct
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            # Affiche un message d'erreur si le nombre d'arguments est incorrect
            print(MSG0.format(command_word=command_word))
            return False

         # Récupère le joueur actuel
        player = game.player
         # Affiche l'historique des pièces visitées
        print("\nHistorique des pièces parcourues :")
        print(player.get_history())
        return True
    def back(game,list_of_words,number_of_parameters):
        """
        Ramène le joueur à sa position précédente en utilisant l'historique des déplacements.

        Args:
            game (Game): L'objet du jeu contenant les informations sur le joueur et l'environnement.
            list_of_words (list): La liste des mots de la commande.
            number_of_parameters (int): Le nombre de paramètres attendu.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.
        """
        # Vérifie si le nombre d'arguments est correct
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            # Affiche un message d'erreur si le nombre d'arguments est incorrect
            print(MSG0.format(command_word=command_word))
            return False

        # Récupère le joueur actuel et met à jour la pièce actuelle avec la dernière pièce visitée
        player=game.player
        game.current_room=player.history[-1]
         # Affiche la pièce à laquelle le joueur revient
        print(f"vous revenez à'{game.current_room}'")
        return True
       
       
    def inventorix(game, list_of_words, number_of_parameters):
        """
        Affiche le contenu de l'inventaire du joueur.

        Args:
            game (Game): L'objet du jeu contenant les informations sur le joueur et l'environnement.
            list_of_words (list): La liste des mots de la commande.
            number_of_parameters (int): Le nombre de paramètres attendu.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.
        """
        # Vérifie si le nombre d'arguments est correct
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            # Affiche un message d'erreur si le nombre d'arguments est incorrect
            print(MSG0.format(command_word=command_word))
            return False

        # Récupère et affiche l'inventaire du joueur
        player = game.player
        print("\nvotre inventaire:")
        print(player.get_inventory())
        return True
    def look(game, list_of_words, number_of_parameters) :
        """
        Permet au joueur d'examiner son environnement ou un objet spécifique.

        Args:
            game (Game): L'objet du jeu contenant les informations sur le joueur et l'environnement.
            list_of_words (list): La liste des mots de la commande.
            number_of_parameters (int): Le nombre de paramètres attendu.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.
        """
        # Vérifie si le nombre d'arguments est correct
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
             # Affiche un message d'erreur si le nombre d'arguments est incorrect
            print(MSG0.format(command_word=command_word))
            return False
        player=game.player
        # Affiche l'inventaire des objets présents dans la pièce actuelle 
        print(game.player.current_room.get_inventory())
        return True 
    def attack(game, list_of_words,number_of_parameters):
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            print(MSG0.format(command_word=command_word))
            return False
        player = game.player
        current_room = player.current_room
        character_name = list_of_words[1]
        
        atk = random.choice([True,False])
        if character_name in player.current_room.character_rooms:
            if atk==True :
                current_room.character_rooms
            
            if player.pv == 1:
                print(f"\n {player.name} vient de mourrir")
                game.finished =True
            else:
                player.pv=player.pv - 1
                game.finished = False
                return True
    
    def take(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de ramasser un objet.

        Args:
            game (Game): L'objet du jeu contenant les informations sur le joueur et l'environnement.
            list_of_words (list): La liste des mots de la commande.
            number_of_parameters (int): Le nombre de paramètres attendu.

        Returns:
            bool: True si l'objet est ramassé avec succès, False sinon.
        """
        # Vérifie si le nombre d'arguments est correct
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
             # Affiche un message d'erreur si le nombre d'arguments est incorrect
            print(MSG0.format(command_word=command_word))
            return False

        # Récupère les inventaires du joueur et de la pièce
        player=game.player
        inventaire=game.player.inventory
        inventaire_room=game.player.current_room.inventory_rooms
         # Récupère l'objet que le joueur veut prendre
        item_to_take = list_of_words[1]
        if inventaire_room == set() :
             # Si la pièce est vide, affiche un message
            print("piece est vide")
            return False
         # Parcourt les objets dans la pièce et ajoute l'objet à l'inventaire si trouvé
        for item in inventaire_room.copy():
            if item.name == item_to_take:
                inventaire[item] = inventaire.get(item, 0) + 1
                inventaire_room.remove(item)
                print(f"{item.name} a été ajouté à votre inventaire.")
        return  True
    def drop(game, list_of_words, number_of_parameters):
        """
        Permet au joueur de déposer un objet de son inventaire dans l'environnement.

        Args:
            game (Game): L'objet du jeu contenant les informations sur le joueur et l'environnement.
            list_of_words (list): La liste des mots de la commande.
            number_of_parameters (int): Le nombre de paramètres attendu.

        Returns:
            bool: True si l'objet est déposé avec succès, False sinon.
        """
         # Vérifie si le nombre d'arguments est correct
        l = len(list_of_words)
        if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            # Affiche un message d'erreur si le nombre d'arguments est incorrect
            print(MSG0.format(command_word=command_word))
            return False

        # Récupère les inventaires du joueur et de la pièce
        player=game.player
        inventaire=game.player.inventory
        inventaire_room=game.player.current_room.inventory_rooms
        # Récupère l'objet que le joueur veut déposer
        item_to_drop = list_of_words[1]
        if not inventaire :
            # Si l'inventaire du joueur est vide, affiche un message
            print("inventaire vide")
            return False
        # Parcourt les objets dans l'inventaire et dépose l'objet dans la pièce si trouvé
        for item in inventaire.copy():
            if item.name == item_to_drop:
                inventaire_room.add(item) 
                inventaire.pop(item)
                print(f"{item.name} a été depose dans {game.player.current_room.name}.")
        return  True
    def talk(game, list_of_words, number_of_parameters):
         """
        Permet au joueur de parler à un PNJ (Personnage Non Joueur).

        Args:
            game (Game): L'objet du jeu contenant les informations sur le joueur et l'environnement.
            list_of_words (list): La liste des mots de la commande.
            number_of_parameters (int): Le nombre de paramètres attendu.

        Returns:
            bool: True si la commande est exécutée avec succès, False sinon.
        """
        # Vérifie si le nombre d'arguments est correct
         l = len(list_of_words)
         if l != number_of_parameters + 1:
            command_word = list_of_words[0]
            # Affiche un message d'erreur si le nombre d'arguments est incorrect
            print(MSG1.format(command_word=command_word))
            return False
         player = game.player
         current_room = player.current_room
         character_name = list_of_words[1]
         if character_name in player.current_room.character_rooms:
            print(player.current_room.character_rooms[character_name].get_msg())
            return True
         else:
            print(f"Il n'y a pas de personnage nommé {character_name} ici.")
            return False

        



    

    
    

        
