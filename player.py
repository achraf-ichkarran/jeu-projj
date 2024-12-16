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
        if not self.history :
            return "le joueur n'a pas encore parcourue la piece"
        return "->".join(self.history)
    #def get_inventory(self):
    def get_inventory(self):
        if not self.inventory :
            return "votre inventaire est vide"
        return "\n->" .join(self.inventory)
        

