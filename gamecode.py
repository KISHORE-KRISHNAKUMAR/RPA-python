import random 

Score = 0
word_list = ["lap", "core", "intel", "bat", "lock", "amd", "volts", "score"]
play_count = 0
print("************************ Welcome to WORDLE ****************************")
print("Nice to meet you!")


def jumble_word(word):
    jumbled_word = ''.join(random.sample(word, len(word)))
    return jumbled_word

def update(word):
    global Score
    word_length = len(word)
    if word_length == 3:
        score = 1
    elif word_length == 4:
        score = 5
    elif word_length == 5:
        score = 10
    else:
        score = 0
    Score += score

while True:
    play_count += 1
    word = random.choice(word_list)
    jumbled_word = jumble_word(word)

    print("Jumbled word:", jumbled_word)
    guess = input("Guess the word: ")

    if guess == word:
        print("Correct!")
        update(word)
    else:
        print("Incorrect.")
    print("Play count:", play_count)
    print("Score:", Score)
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() != "y":
        print("YOUR TOTAL SCORE =",Score)
        break
print("************************ Thank You! Play Again! ****************************")
