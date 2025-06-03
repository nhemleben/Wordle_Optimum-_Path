import string
import sys
#sys.path.append('../src')
#import src.Wordle_Engine as Wordle_Engine
import Wordle_Engine as Wordle_Engine

alphabet_list = list(string.ascii_lowercase)
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


#probability a certian character is in the position_int position given the currently possible answers
def probability_of_character_in_pos(Curr_valid_answers, char_in_question, position_int):
    matching_words = [word for word in Curr_valid_answers if word[position_int] == char_in_question]
    number_with_character_at_position = len(matching_words)
    return number_with_character_at_position/ len(Curr_valid_answers )


#probability of all characters in the position_int position given the currently possible answers
def probability_of_all_char_in_pos(Curr_valid_answers , position_int):
    char_to_prob = []
    for char in alphabet_list:
        char_to_prob.append(probability_of_character_in_pos(Curr_valid_answers, char, position_int) )
    return char_to_prob


#Goes for highest probability of each letter in the guess word, if the highest probiablity is not in allowable guesses
#modify the left most letter possible untill on guess list [shouldn't be any different than right most and easier to index]
#The word is constructed based on proabilites from the Answer list, and then used only if it is in the Guesses list
def greedy_naive_guesser(Curr_valid_answers, Curr_valid_guesses):
    word_length = len(Curr_valid_answers[0])
    master_index_to_char_probabilty = []
    for index in range(word_length):
        master_index_to_char_probabilty.append( probability_of_all_char_in_pos(Curr_valid_answers, index) )


    #Get most likely letter for each spot in word
    master_naive_word_chars = []
    for index in range(word_length):
        char_index = master_index_to_char_probabilty[index].index( max( master_index_to_char_probabilty[index]))
        master_naive_word_chars.append( alphabet_list[char_index] )

    naive_word = ''.join(master_naive_word_chars)

    #need to make deep copy to make modification to this list not mess stuff up
    minor_index_to_char_prob = master_index_to_char_probabilty.copy()

    index_to_modify = 0 
    #If word not a valid guess then go letter by letter till good
    while naive_word not in Curr_valid_guesses:
    
        #set the probability of current character to 0 and refind max, if need to go up an index
        #reset using master index list 
        minor_index_to_char_prob[index_to_modify][ alphabet_list.index(naive_word[index_to_modify])] = 0

        while sum(minor_index_to_char_prob[ index_to_modify]) == 0 :
            #reset letters probability 
            minor_index_to_char_prob[index_to_modify]= master_index_to_char_probabilty[index_to_modify].copy()
            #reset letter in guess to to initial (maximal probability guess) aswell
            naive_word_list = list(naive_word)
            naive_word_list[index_to_modify] = master_naive_word_chars[index_to_modify]
            naive_word = ''.join(naive_word_list)

            index_to_modify +=1
            #current letter is still broken as I haven't changed anything yet
            minor_index_to_char_prob[index_to_modify][ alphabet_list.index(naive_word[index_to_modify])] = 0

        char_index = minor_index_to_char_prob[index_to_modify].index( max( minor_index_to_char_prob[index_to_modify]))
        naive_word_list = list(naive_word)
        #print(naive_word_list)
        naive_word_list[index_to_modify] = alphabet_list[char_index]
        naive_word = ''.join(naive_word_list)

        if index_to_modify > 0:
            index_to_modify = 0

    return naive_word





