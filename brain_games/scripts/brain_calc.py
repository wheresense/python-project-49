from brain_games.engine import run_game
from brain_games.games import calc

def main() -> None:
    run_game(calc.rules, calc.run_game_calc)

if __name__ == "__main__":
    main()