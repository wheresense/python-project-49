import random

rules = 'What number is missing in the progression?'

def run_game_progression() -> None:
    input_data, correct_answer = get_sequence()
    return input_data, correct_answer

def get_sequence() -> list:
    len_sequence = random.randint(5, 10)
    first_element_sequence = random.randint(0, 20)
    step_sequence = random.randint(2, 5)
    sequence = [first_element_sequence]
    current_element = first_element_sequence
    count = 0 

    while count != len_sequence:
         current_element = current_element + step_sequence
         sequence.append(current_element)
         count += 1

    hidden_element = str(sequence[step_sequence])
    sequence[step_sequence] = '..'
    result = ' '.join(map(str, sequence))
    return result, hidden_element