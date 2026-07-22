import random

rules = 'What is the result of the expression?'

def run_game_calc() -> None:
    first_number = random.randint(0, 100)
    second_number = random.randint(0,100)
    mathematical_action = random.choice(['+', '-', '*'])
    input_data = f'{first_number} {mathematical_action} {second_number}'
    match mathematical_action:
        case '+':
            correct_answer = str(first_number + second_number)
        case '-':
            correct_answer = str(first_number - second_number)
        case '*':
            correct_answer = str(first_number * second_number)
    return input_data, correct_answer

