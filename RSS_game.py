import random

print("Let's play rock, paper, or scissors")

player_wins = 0
computer_wins = 0

while player_wins < 2 and computer_wins < 2:
  player_choice = input("\nChoose rock, paper, or scissors: ").lower()
  choices = ["rock", "paper", "scissors"]
  computer_choice = random.choice(choices)
  print(f"Computer chose: {computer_choice}")

  if (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
    winner = "Player"
    player_wins += 1
  elif player_choice == computer_choice:
    winner = "Tie"
  else:
    winner = "Computer"
    computer_wins += 1

  if winner == "Player":
    print("You won")
  elif winner == "Computer":
    print("Computer won")
  else:
    print("It's a tie")


  if player_wins == 3:
    print("Player won")
  elif computer_wins == 3:
    print("Computer won")

  current_score = f"Player: {player_wins}, Computer: {computer_wins}" 
  print(current_score)

  if player_wins > computer_wins:
    print("Congratulations! You won!")
  elif computer_wins > player_wins:
    print("Computer won")
