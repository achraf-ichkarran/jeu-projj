
DIRECTIONS = {
    "N": "N", "North": "N","north":"N",
    "E": "E", "est": "E","est":"E",
    "S": "S", "sud": "S",
    "O": "O", "ouest": "O",
    "U": "U", "up":"U", "Up":"U",
    "D": "D", "down": "D","Down":"D"}
def centralise_direction(input_direction):
    return DIRECTIONS.get(input_direction, None)
