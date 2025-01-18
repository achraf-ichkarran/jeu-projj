class Item :
    def __init__(self,name,description,weight) :
        self.name=name
        self.description=description
        self.weight=weight
    
    def __str__(self):
        return f"{self.name}: {self.description} (Weight: {self.weight} kg)"
    
    def to_dict(self):

        

        """
        Convertit l'objet en un dictionnaire représentant ses attributs et leurs valeurs.

        Cette méthode permet de sérialiser l'objet en un dictionnaire, où les clés correspondent
        aux noms des attributs de l'objet et les valeurs correspondent à leurs valeurs actuelles.

        Args:
            None

        Returns:
            dict: Un dictionnaire contenant les attributs de l'objet sous forme de paires clé-valeur.

        Example:
            >>> obj = MyClass()
            >>> obj.to_dict()
            {'attribute1': value1, 'attribute2': value2}
        """
        return {self.name: [self.description, self.weight]}
    

