########################
### helper functions ###

# fill correct_guesses with underscores to help print out later
def setup_game(secret_phrase, str_len, correct_guesses):
    for c in range (str_len):
        if secret_phrase[c] == " ":
            correct_guesses.append(" ")
            continue
        correct_guesses.append("_")


# print out how many guesses are left
def print_num_guesses(num_guesses):
    print("You have", num_guesses, end=" ")
    if num_guesses == 1:
        print("guess left.")
    else:
        print("guesses left.")


# print out guesses
def print_guesses(num_guesses, prev_guesses, correct_guesses):
    # print out how many guesses are left
    print_num_guesses(num_guesses)

    # print out all letters guessed so far
    print("This is what you have guessed so far: ", end="")
    sorted_list = sorted(prev_guesses)
    for c in prev_guesses:
        print(c + " ", end="")
    print()

    # print out current phase
    print("This is the phrase so far: ")
    for c in correct_guesses:
        print(c, end="")
    print("\n")


def main():
    # setup variables for keeping track of the state of game
    num_guesses = 6         # current number of guesses left
    prev_guesses = []       # store previous guesses
    correct_guesses = []    # store correct guesses
    num_correct_letters = 0 # store total numbers of correct letters

    # ask for phrase and setup game
    secret_phrase = input("\nEnter a phrase: ")
    str_len = len(secret_phrase)
    setup_game(secret_phrase, str_len, correct_guesses)
    print()

    while num_guesses > 0:
        # get letter guessed by player
        letter = input("Player, Guess a Letter: ")
        letter = letter.lower()

        if letter == "?":
            # player wants to know what they have guessed so far
            print()
            print_guesses(num_guesses, prev_guesses, correct_guesses)
            continue

        # check if player has already guessed that letter
        if letter in prev_guesses:
            print("\nYou already guessed this letter!")
            print("Guess again!\n")
            continue

        # add guess to list of guesses
        prev_guesses.append(letter)

        # check if letter is in phrase
        if letter in secret_phrase.lower():
            # store the letter into all correct spots according to phrase
            for c in range (str_len):
                if secret_phrase.lower()[c] == letter:
                    # found where letter should go
                    correct_guesses[c] = letter
                    # update number of letters guessed correctly
                    num_correct_letters = num_correct_letters + 1
            print("\nCorrect!\n")

            if num_correct_letters == (str_len - secret_phrase.count(" ")):
                # the whole phrase has been guesses correctly
                print("You guessed the whole phrase correct!")
                print(secret_phrase)
                print()
                break;
        else:
            num_guesses = num_guesses - 1
            print("\nIncorrect letter.")
            # print out how many guesses are left
            print_num_guesses(num_guesses)
            print()

    # if no guesses left, then player lost
    if (num_guesses == 0):
        print("Sorry, you did not correct the entire phrase.")
        print(secret_phrase)
        print()

main()
