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

        # Return the room in the given direction if it exists.
        if direction in self.exits.keys():
            return self.exits[direction]
        else:
            return None
    
    # Return a string describing the room's exits.
    def get_exit_string(self):
        exit_string = "Sorties: " 
        for exit in self.exits.keys():
            if self.exits.get(exit) is not None:
                exit_string += exit + ", "
        exit_string = exit_string.strip(", ")
        return exit_string

    # Return a long description of this room including exits.
    def get_long_description(self):
        return f"\nVous êtes {self.description}\n\n{self.get_exit_string()}\n"
    def get_inventory(self):
        inventory_list = "\n".join(str(item) for item in self.inventory_rooms)
        characters_list = "\n".join(f"{details.name}: {details.description}"  for details in self.character_rooms.values())

        resultat=[]
        if not self.inventory_rooms and self.character_rooms:
            return "piece vide"
        
        resultat.append(f"Objets présents :\n{inventory_list}")
        
        resultat.append(f"Personnages présents :\n{characters_list}")
        
        return "\n\n".join(resultat)