from collections.abc import Callable

from brain_games.cli import welcome_user


def run_game(rules: str, game: Callable[[], tuple[str, str]]) -> None:
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print(f'Hello, {name}!')
    print(rules)
    count = 0

    while count < 3:
        input_data, correct_answer = game()
        print(f'Question: {input_data}')
        answer = input('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            count += 1
        else:
            print(f'"{answer}" is wrong answer ;(. '
                  'Correct answer was "{correct_answer}".')
            print(f"Let's try again, {name}!")
            break

    if count == 3:
        print(f'Congratulations, {name}!')