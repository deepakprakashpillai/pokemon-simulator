from pokemon import Game

while True:
    game = Game()
    game.choose_starter()
    game.generate_opponent()
    game.battle(game.starter_pokemon, game.opponent_pokemon)
    game.check_winner(game.starter_pokemon, game.opponent_pokemon)
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break