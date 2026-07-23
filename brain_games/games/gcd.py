import random

rules = 'Find the greatest common divisor of given numbers.'

def run_game_gcd() -> None:
    first_number = random.randint(1, 100)
    second_number = random.randint(1,100)
    input_data = f'{first_number} {second_number}'
    correct_answer = str(get_gcd(first_number, second_number))
    return input_data, correct_answer

def get_gcd(first_number: int, second_number: int) -> int:
    divisible = first_number
    divider = second_number

    while divider != 0:
        remains = divisible % divider
        divisible = divider
        divider = remains

    return divisible