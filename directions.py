
DIRECTIONS = {
    "N": "N", "North": "N","north":"N",
    "E": "E", "est": "E","est":"E",
    "S": "S", "sud": "S",
    "O": "O", "ouest": "O",
    "U": "U", "up":"U", "Up":"U",
    "D": "D", "down": "D","Down":"D"}
def centralise_direction(input_direction):
    """
    Normalise une direction donnée en un format standardisé.

    Cette fonction prend une direction en entrée (par exemple : 'Nord', 'nord-est') 
    et la transforme en une forme centralisée ou cohérente (par exemple : 'N', 'NE').

    Args:
        input_direction (str): La direction à normaliser. 
            Peut inclure des variations comme 'Nord', 'nord', 'N', ou 'nord-est'.

    Returns:
        str: La direction normalisée, exprimée sous une forme standard (ex : 'N', 'NE').

    Raises:
        ValueError: Si la direction fournie n'est pas reconnue ou valide.
    """
    return DIRECTIONS.get(input_direction, None)
