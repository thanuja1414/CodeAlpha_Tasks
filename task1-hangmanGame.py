import random

words=["torch", "fruit", "juice", "color", "letter"]
word=random.choice(words)
guessed_word=["_"]*len(word)
attempts=6

print("Welcome to Hangman!")

while attempts>0:
    print("\nWord:", " ".join(guessed_word))
    print("Remaining Attempts:", attempts)
    guess=input("Enter a letter: ").lower()
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        attempts -= 1
        print("Wrong Guess!")

    if "_" not in guessed_word:
        print("\nCongratulations!")
        print("You guessed:", word)
        break

if "_" in guessed_word:
    print("\nGame Over!")
    print("Correct Word:", word)