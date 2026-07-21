from brain_games.scripts import brain_games
from collections.abc import Callable


def run_game(rules: str, game: Callable[[], tuple[str, str]]) -> None:
    name = brain_games.main()
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
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}".')
            print(f"Let's try again, {name}!")
            break

    if count == 3:
        print(f'Congratulations, {name}!')