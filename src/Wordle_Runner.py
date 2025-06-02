import Wordle_Engine

length_of_answer = 5

max_number_guesses = 10
cheater_mode = True

def Main_Game():
    answer = Wordle_Engine.generate_random_answer()

    if cheater_mode:
        print(answer)

    guess = input("First guess for Wordle: ")

    while len(guess) != 5:
        print("You are dumb, wrong length guess, fix:")
        guess = input("First guess for Wordle: ")

    number_of_guesses = 1

    while number_of_guesses <= max_number_guesses:
        currect_indexes = Wordle_Engine.matching_character_indexes(answer, guess)
        non_matching_contained = Wordle_Engine.non_matching_contained_in_answer_indexes(answer, guess)

        print("The matching indexes are:")
        print(currect_indexes)
        print("The non matching but contained indexes are:")
        print(non_matching_contained)
        if len(currect_indexes) == 5:
            print("Great job you win")
            break

        print("Currently on guess number: " + str(number_of_guesses))
        guess = input("Next guess for Wordle: ")
        number_of_guesses += 1
    

    




if __name__ == '__main__':
    Main_Game()