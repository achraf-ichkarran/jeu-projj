
DIRECTIONS = {
    "N": "N", "North": "N","north":"N",
    "E": "E", "est": "E","est":"E",
    "S": "S", "sud": "S",
    "O": "O", "ouest": "O",
    "H": "H", "haut":"H", "Haut":"H",
    "D": "D", "bas": "D","Bas":"B"}
def centralise_direction(input_direction):
    return DIRECTIONS.get(input_direction, None)
