import sys
import copy
sys.path.append('../src')
#import src.Wordle_Engine as Wordle_Engine
#import src.Wordle_Player as Wordle_Player
import Wordle_Engine
import Wordle_Player

length_of_answer = 5

max_number_guesses = 100
cheater_mode = True

num_games = 100



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

def Manual_Game():
    answer = Wordle_Engine.generate_random_answer()

    if cheater_mode:
        print(answer)

    guess = get_valid_guess()

    number_of_guesses = 1

    while number_of_guesses <= max_number_guesses:

        currect_indexes, non_matching_contained, non_matched = Wordle_Engine.generic_wordle_round(answer, guess)

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
    

def Observed_Agent_Main_Game(Guesser):
    answer = Wordle_Engine.generate_random_answer()
    answer = "antic"#5
    #answer = "joker" #10
#    answer = "delta" #7
    #answer = "yield" #10

    if cheater_mode:
        print(answer)

    Cur_Valid_Answers = Wordle_Player.All_Possible_Answers
    Cur_Valid_Guesses = Wordle_Player.All_Possible_Guesses
    guess = Guesser(Cur_Valid_Answers, Cur_Valid_Guesses)

    print("guess: ", guess)

    number_of_guesses = 1

    while number_of_guesses <= max_number_guesses:

        currect_indexes, non_matching_contained_indexes, not_matched_indexes = Wordle_Engine.generic_wordle_round(answer, guess)

        #remove most recent guess from possible answers and guesses to prevent duplicates
        if guess in Cur_Valid_Answers:
            Cur_Valid_Answers.remove(guess)
        Cur_Valid_Guesses.remove(guess)

        if len(currect_indexes) == 5:
            print("Great job you win")
            break

        print("The matching letter and their spot are:")
        matching_characters = [guess[index] for index in currect_indexes] 
        print(matching_characters)
        print(currect_indexes)

        print("Matching letters but wrong spot:") #readabilty
        non_matching_contained_chars = [guess[index] for index in non_matching_contained_indexes] 
        print(non_matching_contained_chars)

        print("Currently on guess number: " + str(number_of_guesses))
        
        Cur_Valid_Answers = Wordle_Player.all_valid_guesses(Cur_Valid_Answers, matching_characters, currect_indexes, non_matching_contained_chars, non_matching_contained_indexes, not_matched_indexes)
        Cur_Valid_Guesses = Wordle_Player.all_valid_guesses(Cur_Valid_Guesses, matching_characters, currect_indexes, non_matching_contained_chars, non_matching_contained_indexes, not_matched_indexes)

        guess = Guesser(Cur_Valid_Answers, Cur_Valid_Guesses)
        print("guess: ", guess)
        number_of_guesses += 1



#For simulating agent repeatedly, no prints to avoid cloging terminal
def Agent_Main_Game(Guesser):
    Answer_log = []
    Num_guess_log = []
#    Guess_log = []

    for x in range(num_games):
        if x % 10 ==0: #Progress bar
            print(x)

        answer = Wordle_Engine.generate_random_answer()
        #print(answer)
        Answer_log.append(answer)

        Cur_Valid_Answers = [word for word in Wordle_Player.All_Possible_Answers]
        Cur_Valid_Guesses = [word for word in Wordle_Player.All_Possible_Guesses]
        guess = Guesser(Cur_Valid_Answers, Cur_Valid_Guesses)

        number_of_guesses = 1

        while number_of_guesses <= max_number_guesses:

            currect_indexes, non_matching_contained_indexes, not_matched_indexes = Wordle_Engine.generic_wordle_round(answer, guess)

            if len(currect_indexes) == 5:
                #print('win')
                break

            #remove most recent guess from possible answers and guesses to prevent duplicates
            if guess in Cur_Valid_Answers:
                Cur_Valid_Answers.remove(guess)
            Cur_Valid_Guesses.remove(guess)

            matching_characters = [guess[index] for index in currect_indexes] 
            non_matching_contained_chars = [guess[index] for index in non_matching_contained_indexes] 

            Cur_Valid_Answers = Wordle_Player.all_valid_guesses(Cur_Valid_Answers, matching_characters, currect_indexes, non_matching_contained_chars, non_matching_contained_indexes, not_matched_indexes)
            Cur_Valid_Guesses = Wordle_Player.all_valid_guesses(Cur_Valid_Guesses, matching_characters, currect_indexes, non_matching_contained_chars, non_matching_contained_indexes, not_matched_indexes)

            guess = Guesser(Cur_Valid_Answers, Cur_Valid_Guesses)
            number_of_guesses += 1

        Num_guess_log.append(number_of_guesses)
    print(sum(Num_guess_log))





if __name__ == '__main__':
    #Manual_Game()
    Guesser_boy = Wordle_Player.greedy_naive_guesser_mid_probability
    Agent_Main_Game(Guesser_boy)
    #Observed_Agent_Main_Game(Guesser_boy)