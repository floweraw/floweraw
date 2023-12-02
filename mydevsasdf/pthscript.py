import random
import csv

# Initialize player names and scores
players = []
scores = []

# Function to play hangman
def play_hangman(player_name):
    print(f"{player_name}, Time to play hangman!")
    
    words = ("apple", "banana", "carrot", "dog", "elephant", "furniture", "guitar", "happiness", "island", "jungle", "kangaroo", "lemon", "mountain", "notebook", "ocean", "penguin", "quartz", "rainbow", "sunny", "tiger", "umbrella", "violin", "waterfall", "xylophone", "yacht", "zebra", "astronomy", "butterfly", "candle", "dolphin", 'anime')
    
    word = random.choice(words)
    guesses = ''
    turns = 10

    while turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end="")
            else:
                print("_", end="")
                failed += 1

        if failed == 0:
            print("\nYou won")
            break

        guess = input("\nGuess a word:")

        guesses += guess

        if guess not in word:
            turns -= 1
            print("Wrong")
            print("You have", turns, 'more guesses')

            if turns == 0:
                print("You Lose")

    print(f'{player_name}, your score is', turns * 10)
    return turns * 10

# Get player names
for i in range(2):
    player_name = input(f"Player {i + 1}, what is your name? ")
    players.append(player_name)

# Play the game for each player
for player_name in players:
    score = play_hangman(player_name)
    scores.append(score)

# Specify the file name
file_name = "scorecard2p.csv"

# Open the CSV file in 'a' (append) mode to add data without replacing existing data
with open(file_name, 'a', newline='') as file:
    # Write data to the CSV file
    writer = csv.writer(file)
    writer.writerow(players)  # Write player names in a new row
    writer.writerow(scores)   # Write player scores in a new row

