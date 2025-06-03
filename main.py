import random
def get_choices():
    player_choice = input("Elige una opción(Piedra, Papel o Tijera): ")
    opciones = ["Piedra", "Papel", "Tijera"]
    computer_choice = random.choice(opciones)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def verificar_victoria(player, computer):
    if player == computer:
        return "Es un empate!"
    elif player == "Piedra":
        if computer == "Papel":
            return "Papel cubre Piedra, tu pierdes!"
        elif computer == "Tijera":
            return "Piedra rompe Tijera, tu ganas!"
    elif player == "Papel":
        if computer == "Piedra":
            return "Papel cubre Piedra, tu ganas!"
        elif computer == "Tijera":
            return "Tijera corta Papel, tu pierdes!"
    elif player == "Tijera":
        if computer == "Papel":
            return "Tijera corta Papel, tu ganas!"
        elif computer == "Piedra":
            return "Piedra rompe Tijera, tu pierdes!"
    else:
        return "Valor invalido"

choices = get_choices()
p_choice = choices["player"]
c_choice = choices["computer"]
result = verificar_victoria(choices["player"], choices["computer"])
print("El jugador eligió " + p_choice + " y la maquina eligió " + c_choice)
print(result)