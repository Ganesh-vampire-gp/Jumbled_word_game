# Jumbled word game in Python

import random

# Function to choose a random word from the list of words
def choose(used_words):
    words = ['rainbow', 'computer', 'science', 'programming', 
             'mathematics', 'player', 'condition', 'reverse', 
             'water', 'board']
    available_words = [word for word in words if word not in used_words]
    if not available_words:
        return None  # No more words available
    pick = random.choice(available_words)
    used_words.add(pick)
    return pick

# Function for shuffling the characters of the word
def jumble(word):
    jumbled = "".join(random.sample(word, len(word)))
    return jumbled

# Function for showing final score
def thank(p1n, p2n, p1, p2):
    print(f"\n{p1n}, Your score is: {p1}")
    print(f"{p2n}, Your score is: {p2}")
    print("\nThanks for playing!")

# Function to play the game
def play():
    p1name = input("Player 1, Enter your name: ")
    p2name = input("Player 2, Enter your name: ")
    pp1 = 0
    pp2 = 0
    turn = 0
    used_words = set()

    while True:
        # Choose a new word
        picked_word = choose(used_words)
        if picked_word is None:
            print("No more words available. Game over!")
            break

        # Jumble the word
        qn = jumble(picked_word)
        print(f"Jumbled word is: {qn}")

        # Player's turn
        if turn % 2 == 0:
            print(f"{p1name}, it's your turn.")
            ans = input("What is your guess? ")
            if ans == picked_word:
                pp1 += 1
                print("Correct!")
            else:
                print(f"Wrong! The correct word was: {picked_word}")
            turn += 1
        else:
            print(f"{p2name}, it's your turn.")
            ans = input("What is your guess? ")
            if ans == picked_word:
                pp2 += 1
                print("Correct!")
            else:
                print(f"Wrong! The correct word was: {picked_word}")
            turn += 1

        # Ask if they want to continue
        cont = input("Do you want to continue? (y/n): ")
        if cont.lower() != 'y':
            break

    # Show final score
    thank(p1name, p2name, pp1, pp2)

# Start the game
if __name__ == "__main__":
    play()