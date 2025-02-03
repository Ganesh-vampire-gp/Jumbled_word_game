# Jumbled Word Game

This is a simple Jumbled Word Game implemented in Python. The game selects a random word from a predefined list, jumbles the characters, and asks the players to guess the original word. The game ensures that a word that has already been used for one player does not come up again.

## How to Play

1. The game will prompt Player 1 and Player 2 to enter their names.
2. The game will then select a random word, jumble the characters, and display the jumbled word.
3. Players take turns guessing the original word.
4. If a player guesses correctly, they earn a point.
5. The game continues until there are no more words available or the players choose to stop.
6. The final scores are displayed at the end of the game.

## Features

- Randomly selects a word from a predefined list.
- Jumbles the characters of the selected word.
- Ensures that a word that has already been used does not come up again.
- Keeps track of the scores for both players.
- Displays the final scores at the end of the game.

## Requirements

- Python 3.x

## How to Run

1. Clone the repository or download the `Jumbled_game.py` file.
2. Open a terminal and navigate to the directory containing the `Jumbled_game.py` file.
3. Run the game using the following command:
   
   python Jumbled_game.py

##Example:
Player 1, enter your name: Alice
Player 2, enter your name: Bob
Jumbled word is: etrw
Alice, it's your turn.
What is your guess? water
Correct!
Do you want to continue? (y/n): y
Jumbled word is: cneices
Bob, it's your turn.
What is your guess? science
Correct!
Do you want to continue? (y/n): n

Alice, Your score is: 1
Bob, Your score is: 1

Thanks for playing!
