import sys
sys.path.append('../src')
import src.Wordle_Engine as Wordle_Engine

All_Possible_Answers = Wordle_Engine.allowed_answers
All_Possible_Guesses = Wordle_Engine.allowed_guesses + Wordle_Engine.allowed_answers

#Return all valid guess given the hints 
def all_valid_guesses(Cur_Valid_Guesses, matching_characters, matching_indexes, non_matching_contained):
    matching_char_guesses = all_valid_guesses_matching_characters(Cur_Valid_Guesses, matching_characters, matching_indexes)
    non_matching_char_guesses = all_valid_guesses_non_matching_characters(matching_char_guesses, non_matching_contained)
    return non_matching_char_guesses

#Return all valid guess given the matching characters
def all_valid_guesses_matching_characters(Curr_valid_guesses, matching_characters, matching_indexes):
    Remaining_Guesses = []

    for possible_guess in Curr_valid_guesses:
        #Check all matching characters match in word
        index = 0
        while index < len(matching_characters):
            if possible_guess[matching_indexes[index]] == matching_characters[index]:
                index+= 1
            else:
                break

        #if exited early this condition will not be true
        if index == len(matching_characters):
            Remaining_Guesses.append(possible_guess)

    return Remaining_Guesses


#Return all valid guess given the non matching contained characters
def all_valid_guesses_non_matching_characters(Curr_valid_guesses, non_matching_contained):
    Remaining_Guesses = []

    for possible_guess in Curr_valid_guesses:
        possible_guess_list = list(possible_guess)

        index = 0
        while index < len(non_matching_contained):
            if non_matching_contained[index] in possible_guess_list:
                index+= 1
            else:
                break

        #if exited early this condition will not be true
        if index == len(non_matching_contained):
            Remaining_Guesses.append(possible_guess)

    return Remaining_Guesses



