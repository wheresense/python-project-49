from brain_games.engine import run_game
from brain_games.games import prime


def main() -> None:
    run_game(prime.rules, prime.run_game_prime)
    

if __name__ == "__main__":
    main()