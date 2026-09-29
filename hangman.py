import random
from english_words import english_words_lower_set


def penalties(number):
    if number >= 12:
        print("You lose!")
        return True
    return False


def random_number():
    return random.randint(1, 6)


def get_word(length):
    words = []

    for item in english_words_lower_set:
        if item.isalpha() and len(item) == length:
            words.append(item)

    return random.choice(words)


def underscore(word, guessed_letters):
    hidden_word = ""

    for letter in word:
        if letter in guessed_letters:
            hidden_word += letter
        else:
            hidden_word += "_"

    print(" ".join(hidden_word))
    return hidden_word


def play_game():
    word_length = random_number()
    word = get_word(word_length)

    guessed_letters = ""
    penalty_count = 0

    print("Welcome to Hangman!")

    while True:
        hidden_word = underscore(word, guessed_letters)

        if "_" not in hidden_word:
            print("You win! The word was:", word)
            break

        print("Penalties:", penalty_count)
        guess = input("Guess a letter or the whole word: ").lower().strip()

        if not guess.isalpha():
            print("Please enter letters only.")
            continue

        if len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter.")
                continue

            guessed_letters += guess

            if guess in word:
                print("Correct!")
            else:
                penalty_count += 1
                print("Wrong letter! You get 1 penalty.")

        else:
            if guess == word:
                print("You win! The word was:", word)
                break
            else:
                penalty_count += 5
                print("Wrong word! You get 5 penalties.")

        if penalties(penalty_count):
            print("The word was:", word)
            break


play_game()
