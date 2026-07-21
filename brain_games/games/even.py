import random

rules = 'Answer "yes" if the number is even, otherwise answer "no".'

def run_game_even() -> None:
    input_data = random.randint(1, 100)
    correct_answer = is_even(input_data)
    return input_data, correct_answer

def is_even(number: int) -> str:
     if number % 2 == 0:
         return 'yes'
     else:
         return 'no'