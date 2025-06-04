import string
import copy
import sys
#sys.path.append('../src')
#import src.Wordle_Engine as Wordle_Engine
import Wordle_Engine as Wordle_Engine

alphabet_list = list(string.ascii_lowercase)
All_Possible_Answers = Wordle_Engine.allowed_answers
All_Possible_Guesses = Wordle_Engine.allowed_guesses + Wordle_Engine.allowed_answers

#Return all valid guess given the hints 
def all_valid_guesses(Cur_Valid_Guesses, matching_characters, matching_indexes, non_matching_contained, non_matched_letters):
    removed_non_matching_letters = removed_letters_no_match(Cur_Valid_Guesses, non_matched_letters)
    matching_char_guesses = all_valid_guesses_matching_characters(removed_non_matching_letters, matching_characters, matching_indexes)
    non_matching_char_guesses = all_valid_guesses_non_matching_characters(matching_char_guesses, non_matching_contained)
    return non_matching_char_guesses

def removed_letters_no_match(Curr_valid_guesses, non_matched_letters):
    #non letters that are forbiden then just give back list
    if len(non_matched_letters) == 0:
        return Curr_valid_guesses

    Remaining_Guesses = []
    for possible_guess in Curr_valid_guesses:
        guess_list = list(possible_guess)
        do_add = True
        for char in non_matched_letters:
            if char in guess_list:
                do_add = False
                break
        if do_add:
            Remaining_Guesses.append(possible_guess)
    return Remaining_Guesses

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
#The word is constructed based on proabilites from the Answer list, and then used only if it is in the Guesses list which contains all answers
def greedy_naive_guesser(Curr_valid_answers, Curr_valid_guesses):
    word_length = len(Curr_valid_answers[0])
    master_index_to_char_probabilty= []
    for index in range(word_length):
        master_index_to_char_probabilty.append( probability_of_all_char_in_pos(Curr_valid_answers, index) )


    #Get most likely letter for each spot in word
    master_naive_word_chars = []
    for index in range(word_length):
        char_index = master_index_to_char_probabilty[index].index( max( master_index_to_char_probabilty[index]))
        master_naive_word_chars.append( alphabet_list[char_index] )

    naive_word = list(''.join(master_naive_word_chars))

    #need to make deep copy to make modification to this list not mess stuff up
    minor_index_to_char_prob = [[probs for probs in char_probs] for char_probs in master_index_to_char_probabilty]

    index_to_modify = 0 
    #If word not a valid guess then go letter by letter till good
    while (''.join(naive_word)) not in Curr_valid_guesses:
        #set the probability of current character to 0 and refind max, if need to go up an index
        #reset using master index list 
        minor_index_to_char_prob[index_to_modify][ alphabet_list.index(naive_word[index_to_modify])] = 0

        while sum(minor_index_to_char_prob[ index_to_modify]) == 0 :
            #reset letters probability 
            minor_index_to_char_prob[index_to_modify] = [probs for probs in master_index_to_char_probabilty[index_to_modify]]
            #reset letter in guess to to initial (maximal probability guess) aswell
            naive_word[index_to_modify] = master_naive_word_chars[index_to_modify]
            index_to_modify +=1
            #current letter is still broken as I haven't changed anything yet
            minor_index_to_char_prob[index_to_modify][ alphabet_list.index(naive_word[index_to_modify])] = 0

        #Get new max probability character
        char_index = minor_index_to_char_prob[index_to_modify].index( max( minor_index_to_char_prob[index_to_modify]))

        #Add to word
        naive_word[index_to_modify] = alphabet_list[char_index]

        #If messing with later letter skip back 
        if index_to_modify > 0:
            index_to_modify = 0

    return ''.join(naive_word)


#Goes for the letter with closest to 50% coverage of remaining letters in the guess word, otherwise identical to greedy_naive_guesser
#Major changes with this: abs(prob-0.5) and now reseting sends likelihood to 0.5 so a letter is not repeated, and 26*0.5 is a 'blank' likelhood array sum

#modify the left most letter possible untill on guess list [shouldn't be any different than right most and easier to index]
#The word is constructed based on proabilites from the Answer list, and then used only if it is in the Guesses list which contains all answers
def greedy_naive_guesser_mid_probability(Curr_valid_answers, Curr_valid_guesses):
    word_length = len(Curr_valid_answers[0])
    master_index_to_char_likelihood = []
    for index in range(word_length):
        likelihood_vect = [ abs(prob - 0.5) for prob in probability_of_all_char_in_pos(Curr_valid_answers, index)]
        master_index_to_char_likelihood.append(likelihood_vect)


    #Get most likely letter for each spot in word
    master_naive_word_chars = []
    for index in range(word_length):
        char_index = master_index_to_char_likelihood[index].index( min( master_index_to_char_likelihood[index]))
        master_naive_word_chars.append( alphabet_list[char_index] )

    naive_word = list(''.join(master_naive_word_chars))

    #need to make deep copy to make modification to this list not mess stuff up
    minor_index_to_char_prob = [[probs for probs in char_probs] for char_probs in master_index_to_char_likelihood]

    index_to_modify = 0 
    #If word not a valid guess then go letter by letter till good
    while (''.join(naive_word)) not in Curr_valid_guesses:
        #set the probability of current character to 0 and refind max, if need to go up an index
        #reset using master index list 
        minor_index_to_char_prob[index_to_modify][ alphabet_list.index(naive_word[index_to_modify])] = 0.5

        while sum(minor_index_to_char_prob[ index_to_modify]) == 26*0.5 :
            #reset letters probability 
            minor_index_to_char_prob[index_to_modify] = [probs for probs in master_index_to_char_likelihood[index_to_modify]]
            #reset letter in guess to to initial (maximal probability guess) aswell
            naive_word[index_to_modify] = master_naive_word_chars[index_to_modify]
            index_to_modify +=1
            #current letter is still broken as I haven't changed anything yet
            minor_index_to_char_prob[index_to_modify][ alphabet_list.index(naive_word[index_to_modify])] = 0.5

        #Get new max probability character
        char_index = minor_index_to_char_prob[index_to_modify].index( min( minor_index_to_char_prob[index_to_modify]))

        #Add to word
        naive_word[index_to_modify] = alphabet_list[char_index]

        #If messing with later letter skip back 
        if index_to_modify > 0:
            index_to_modify = 0

    return ''.join(naive_word)



