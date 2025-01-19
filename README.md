#Jeu d’aventure

Ce dépôt contient la première version du jeu d’aventure. L’objectif est de poser les bases d’un gameplay immersif tout en permettant des améliorations futures.
 **Description de la version actuelle:**

  *-Cette version initiale comprend les éléments suivants :*

        -Une structure de base avec plusieurs classes et modules interconnectés.
        -Un joueur peut interagir avec le jeu via des commandes simples.
        -Les lieux, objets, et personnages sont définis de manière rudimentaire pour permettre l’extension.

  *-Fonctionnalités actuelles :*

        -Navigation entre plusieurs salles.
        -Gestion de l’inventaire du joueur.
        -Définition de personnages non-joueurs (PNJ) avec des comportements simples.
        -Prise en charge de commandes textuelles pour interagir avec l’environnement.

  *-Limites :*

        -Les interactions avec les objets sont encore limitées.
        -Les comportements des PNJ sont simples et non personnalisables.
        -Peu d’éléments visuels ou audios sont intégrés.

 **Structuration :**
La base de code est organisée en plusieurs modules, chacun correspondant à une classe centrale du jeu :

[actions.py] / [Actions] : Gère les interactions entre le joueur et le jeu, comme les commandes de déplacement ou la prise d’objets.
[character.py] / [Character] : Définit les caractéristiques et comportements des PNJ.
[command.py] / [Command] : Analyse et exécute les commandes données par le joueur.
[game.py] / [Game] : Point central qui coordonne les éléments du jeu et gère la progression.
[item.py] / [Item] : Représente les objets interactifs du jeu.
[player.py] / [Player] : Modélise le joueur, son inventaire, et ses déplacements.
[room.py] / [Room] : Représente les lieux avec leurs descriptions et connexions.

**Installation**

  Clonez ce dépôt :

      ($ git clone <https://github.com/achraf-ichkarran/jeu-projj/tree/develop>)

  Lancez le jeu :

      $ python game.py

**À venir**

  -Ajout d’objets interactifs et d’événements dynamiques.
  -Implémentation d’une intelligence artificielle basique pour les PNJ.
  -Amélioration des graphismes et de l’interface utilisateur.
  -Développement de scénarios immersifs et personnalisés.



***Merci de votre intérêt pour ce projet ! Toutes les suggestions ou contributions sont les bienvenues. 😊***