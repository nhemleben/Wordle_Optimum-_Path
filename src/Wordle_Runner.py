import Wordle_Engine

length_of_answer = 5

max_number_guesses = 10
cheater_mode = True

def get_valid_guess():
    guess = input("Guess for Wordle: ")

    #special case for fat finger dumb inputs
    while len(guess) != 5:
        print("You are dumb, wrong length guess, fix:")
        guess = input("First guess for Wordle: ")

    #wrong size is also handled here but wanted to have fun above
    while not Wordle_Engine.guess_is_allowable(guess):
        print("Not an allowed guess")
        guess = input("Next guess for Wordle: ")

    return guess

def Main_Game():
    answer = Wordle_Engine.generate_random_answer()

    if cheater_mode:
        print(answer)

    guess = get_valid_guess()

    number_of_guesses = 1

    while number_of_guesses <= max_number_guesses:

        currect_indexes, non_matching_contained = Wordle_Engine.generic_wordle_round(answer, guess)

        print("The matching letter and their spot are:")
        print([guess[index] for index in currect_indexes] )
        print(currect_indexes)

        print("Matching letters but wrong spot:") #readabilty
        print([guess[index] for index in non_matching_contained] )

        if len(currect_indexes) == 5:
            print("Great job you win")
            break

        print("Currently on guess number: " + str(number_of_guesses))
        guess = get_valid_guess()
        number_of_guesses += 1
    

    




if __name__ == '__main__':
    Main_Game()