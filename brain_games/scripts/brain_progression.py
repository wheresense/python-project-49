from brain_games.engine import run_game
from brain_games.games import progression

def main() -> None:
    run_game(progression.rules, progression.run_game_progression)

if __name__ == "__main__":
    main()