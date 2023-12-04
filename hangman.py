import random

# Note the double \\ to avoid invalid escape sequence errors

import hangman_assets

# Select Game Word
gameword = random.choice(hangman_assets.word_list)
gameword = gameword.upper()
gamelength = len(gameword)

# Generate Game State
gamestate = []
for x in range(gamelength):
    gamestate.append("_")
wincon = "".join(gamestate) == gameword
lives = len(hangman_assets.stages)
valid = False

# debug
# print(f"Chosen Word: {gameword}")
print(f"Word Length: {gamelength}")

# UI
print("Hangman Simulator Part 3")


# Render Game State
print(f"Game State: {gamestate}")


while (not wincon) and (lives > 0):
    # Collect User Input
    user = input("Guess a letter: ")
    user = user.upper()

    # Letter Checking
    valid = False
    for x in range(gamelength):
        if gameword[x] == user:
            gamestate[x] = gameword[x]
            valid = True
    if not valid:
        lives -= 1
        print(f"Remaining Lives: {lives}")
        print(hangman_assets.stages[lives])
    # Re-render
    print(f"New Game State: {gamestate}")
    wincon = "".join(gamestate) == gameword
    # print(f"Wincon: {wincon}")


print("Game Over!")
