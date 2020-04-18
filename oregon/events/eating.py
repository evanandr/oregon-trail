from oregon.utilities.user_prompts import ask_numeric


def eating(inv, turn_state):
    response = ask_numeric("DO YOU WANT TO EAT (1) POORLY  (2) MODERATELY\nOR (3) WELL", 1, 3)
    food_eaten = 8 + 5 * response
    if inv.food.value < food_eaten:
        print("YOU CAN'T EAT THAT WELL")
        return eating(inv, turn_state)
    turn_state.eating_state = response
    inv.food.subtract(food_eaten)
