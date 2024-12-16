

class Character:
    def __init__(self,name,description,current_room,msgs) :
        self.name=name
        self.description=description
        self.current_room=current_room
        self.msgs=msgs
    def __str(self):
        return f"{self.name}: {self.description} (msgs: {self.msgs})"
    def to_dict(self):
        return {self.name: [self.description, self.msgs]}