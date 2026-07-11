from . import brain_games
from brain_games.cli import welcome_user 
import random


def main():
    name = brain_games.main()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = input('Your answer: ')
        correct_answer = is_even(number)
        if (answer == 'yes' or answer == 'no') and correct_answer == answer:
            print('Correct!')
            count += 1
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}".')
            print(f"Let's try again, {name}!")
            break
    if count == 3:
        print(f'Congratulations, {name}!')

                
def is_even(number):
     if number % 2 == 0:
         return 'yes'
     else:
         return 'no'
     


if __name__ == "__main__":
    main()