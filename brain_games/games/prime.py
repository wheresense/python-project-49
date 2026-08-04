import random

rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def run_game_prime() -> None:
    input_data = random.randint(1, 100)
    correct_answer = is_prime(input_data)
    return input_data, correct_answer


def is_prime(number: int) -> str:
    square_root = int(number ** 0.5)
    divisors = []

    for i in range(1, square_root + 1):
        if i > 2 and i % 2 != 0:
            divisors.append(i)

    if number < 2:
        return 'no'
    elif number > 2 and number % 2 == 0:
        return 'no'
    elif number == 3:
        return 'yes'
    else:
        if not divisors:
            return 'yes'
        else:
            for i in divisors:
                if number % i == 0:
                    return 'no'
            return 'yes'
            