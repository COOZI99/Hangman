########################
### helper functions ###

# fill correct_guesses with underscores to help print out later
def setup_game(secret_word, str_len, correct_guesses):
    for c in range (str_len):
        if secret_word[c] == " ":
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

### ONLY DO IF ENOUGH TIME ###
# # print out guesses
# def print_guesses(num_guesses, prev_guesses, correct_guesses):
#     # print out how many guesses are left
#     print_num_guesses(num_guesses)
#
#     # print out all letters guessed so far
#     print("This is what you have guessed so far: ", end="")
#     sorted_list = sorted(prev_guesses)
#     for c in prev_guesses:
#         print(c + " ", end="")
#     print()
#
#     # print out current word
#     print("This is the word so far: ")
#     for c in correct_guesses:
#         print(c, end="")
#     print("\n")
##############################


def main():
    # setup variables for keeping track of the state of game
    num_guesses = 6         # current number of guesses left
    prev_guesses = []       # store previous guesses
    correct_guesses = []    # store correct guesses
    num_correct_letters = 0 # store total numbers of correct letters

    # ask for word and setup game
    secret_word = input("\nEnter a word: ")
    str_len = len(secret_word)
    setup_game(secret_word, str_len, correct_guesses)
    print()

    while num_guesses > 0:
        # get letter guessed by player
        letter = input("Player, Guess a Letter: ")
        letter = letter.lower()

        # error check that a valid letter was inputted
        if letter < 'a' or letter > 'z':
            print("\nThat is not a letter. Please input a letter.\n")
            continue

        ### ONLY DO IF ENOUGH TIME ###
        # # check if user wants to know their progress so far
        # if letter == "?":
        #     # player wants to know what they have guessed so far
        #     print()
        #     print_guesses(num_guesses, prev_guesses, correct_guesses)
        #     continue
        ##############################

        # check if player has already guessed that letter
        if letter in prev_guesses:
            print("\nYou already guessed this letter!")
            print("Guess again!\n")
            continue

        # add guess to list of guesses
        prev_guesses.append(letter)

        # check if letter is in word
        if letter in secret_word.lower():
            # store the letter into all correct spots according to word
            for c in range (str_len):
                if secret_word.lower()[c] == letter:
                    # found where letter should go
                    correct_guesses[c] = letter
                    # update number of letters guessed correctly
                    num_correct_letters = num_correct_letters + 1
            print("\nCorrect!\n")

            if num_correct_letters == (str_len - secret_word.count(" ")):
                # the whole word has been guesses correctly
                print("You guessed the whole word correctly!")
                print(secret_word)
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
        print("Sorry, you did not guess the entire word.")
        print(secret_word)
        print()

main()
