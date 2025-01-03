import random
import time
from typing import Tuple

class RockPaperScissors:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.player_score = 0
        self.computer_score = 0
        self.rules = {
            'rock': {'beats': 'scissors', 'loses_to': 'paper'},
            'paper': {'beats': 'rock', 'loses_to': 'scissors'},
            'scissors': {'beats': 'paper', 'loses_to': 'rock'}
        }

    def display_welcome(self):
        """Display welcome message and game rules"""
        print("\n" + "="*50)
        print("Welcome to Rock, Paper, Scissors!")
        print("="*50)
        print("\nRules:")
        print("- Rock crushes Scissors")
        print("- Scissors cuts Paper")
        print("- Paper covers Rock")
        print("\nFirst to win 3 rounds is the champion!")
        print("\nType 'quit' to exit the game")
        print("="*50 + "\n")

    def get_player_choice(self) -> str:
        """Get and validate player's choice"""
        while True:
            choice = input("\nEnter your choice (rock/paper/scissors): ").lower().strip()
            if choice == 'quit':
                return choice
            if choice in self.choices:
                return choice
            print("Invalid choice! Please choose rock, paper, or scissors.")

    def get_computer_choice(self) -> str:
        """Generate computer's choice"""
        return random.choice(self.choices)

    def determine_winner(self, player_choice: str, computer_choice: str) -> Tuple[str, str]:
        """Determine the winner of the round"""
        if player_choice == computer_choice:
            return "Tie", "It's a tie!"
        
        if computer_choice == self.rules[player_choice]['beats']:
            self.player_score += 1
            return "Player", f"{player_choice.capitalize()} beats {computer_choice}! You win!"
        else:
            self.computer_score += 1
            return "Computer", f"{computer_choice.capitalize()} beats {player_choice}! Computer wins!"

    def display_round_result(self, player_choice: str, computer_choice: str, result_message: str):
        """Display the results of the round"""
        print("\n" + "-"*30)
        print(f"Your choice: {player_choice.capitalize()}")
        print(f"Computer's choice: {computer_choice.capitalize()}")
        print(f"\n{result_message}")
        print(f"\nScore - You: {self.player_score} | Computer: {self.computer_score}")
        print("-"*30)

    def display_final_score(self):
        """Display the final game score"""
        print("\n" + "="*50)
        print("Game Over!")
        print(f"Final Score - You: {self.player_score} | Computer: {self.computer_score}")
        if self.player_score > self.computer_score:
            print("🎉 Congratulations! You are the champion! 🎉")
        elif self.computer_score > self.player_score:
            print("Better luck next time! Computer wins the game!")
        else:
            print("It's a tie game!")
        print("="*50 + "\n")

    def play_game(self):
        """Main game loop"""
        self.display_welcome()
        
        while True:
            player_choice = self.get_player_choice()
            
            if player_choice == 'quit':
                break
                
            print("\nRock...")
            time.sleep(0.5)
            print("Paper...")
            time.sleep(0.5)
            print("Scissors...")
            time.sleep(0.5)
            print("Shoot!")
            
            computer_choice = self.get_computer_choice()
            winner, result_message = self.determine_winner(player_choice, computer_choice)
            self.display_round_result(player_choice, computer_choice, result_message)
            
            # Check if someone has won 3 rounds
            if self.player_score == 3 or self.computer_score == 3:
                self.display_final_score()
                
                play_again = input("Would you like to play again? (yes/no): ").lower().strip()
                if play_again != 'yes':
                    break
                # Reset scores for new game
                self.player_score = 0
                self.computer_score = 0
                print("\nStarting new game...")

def main():
    game = RockPaperScissors()
    game.play_game()
    print("Thanks for playing!")

if __name__ == "__main__":
    main()