


class Door:
    """
    Représente une porte entre deux pièces, qui peut être verrouillée et nécessite un code pour être déverrouillée.

    Attributes:
        code (str): Le code nécessaire pour déverrouiller la porte.
        locked (bool): Indique si la porte est verrouillée ou non.
    """

    def __init__(self,name, code):
        """
        Initialise une porte avec un code et verrouille la porte par défaut.

        Args:
            code (str): Le code nécessaire pour déverrouiller la porte.
        """
        self.name=name
        self.code = code
        self.locked = True

    def unlock(self, input_code):
        """
        Tente de déverrouiller la porte avec un code donné.

        Args:
            input_code (str): Le code fourni par le joueur.

        Returns:
            bool: True si le code est correct et la porte est déverrouillée, False sinon.
        """
        if input_code == self.code:
            self.locked = False
            return True
        return False

    def is_locked(self):
        """
        Vérifie si la porte est verrouillée.

        Returns:
            bool: True si la porte est verrouillée, False sinon.
        """
        return self.locked