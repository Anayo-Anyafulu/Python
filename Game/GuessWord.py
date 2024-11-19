import random

word_bank = ['algorithm', 'binary', 'cache', 'debug', 'encryption', 'firewall', 'gigabyte', 'hash', 'interface', 'kernel']

word = random.choice(word_bank)

guessedWord = ['_'] * len(word)

attempts = 8

while attempts > 0:
    print("\nCurrent word: " + " ".join(guessedWord))
    print(f"Attempts left: {attempts}")
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in word:
        if guess not in guessedWord:
            for i in range(len(word)):
                if word[i] == guess:
                    guessedWord[i] = guess
            print("Correct guess!")
        else:
            print("You've already guessed this letter correctly.")
    else:
        if guess not in guessedWord:
            attempts -= 1
            print(f"Wrong guess. You have {attempts} attempts left.")
        else:
            print("You've already guessed this letter incorrectly.")

    if '_' not in guessedWord:
        print("Congratulations! You guessed the word:", word)
        break

if attempts == 0:
    print("You have run out of attempts. The word was:", word)



