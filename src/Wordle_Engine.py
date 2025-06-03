#Wordle engine 
import random
import os

allowed_answers = []
allowed_guesses = []

#load in allowed answers and guesses 
PATH = os.path.join(os.path.dirname(__file__), '../data/wordle-answers-alphabetical.txt')
with open(PATH, 'r') as file:
    lines = file.readlines()
    for line in lines:
        allowed_answers.append(line.strip('\n'))

PATH = os.path.join(os.path.dirname(__file__), '../data/wordle-allowed-guesses.txt')
with open(PATH,'r') as file:
    lines = file.readlines()
    for line in lines:
        allowed_guesses.append(line.strip('\n'))

number_of_possible_answers = len(allowed_answers)
number_of_possible_guesses = len(allowed_guesses)


def generate_random_answer():
    rand_index = random.randint(0,number_of_possible_answers-1)
    return allowed_answers[rand_index]

def generate_random_guess():
    rand_index = random.randint(0,number_of_possible_guesses-1)
    return allowed_guesses[rand_index]


#Guesses can either be in the guess list or the answer list, as otherwise no guess would ever be correct
def guess_is_allowable(guess):
    return len(guess) == 5 and (guess in allowed_guesses or guess in allowed_answers)

#These letters and their locations match
def matching_character_indexes(answer, guess):
    if len(guess) != len(answer):
        raise Exception("answers and guesses must be same length")

    matching_indexes = []
    for index in range(len(answer)):
        if answer[index] == guess[index]:
            matching_indexes.append(index)
    return matching_indexes

#These letters and their locations match
def matching_characters(answer, guess):
    if len(guess) != len(answer):
        raise Exception("answers and guesses must be same length")

    matching_characters = []
    for index in range(len(answer)):
        if answer[index] == guess[index]:
            matching_characters.append(answer[index])
    return matching_characters

#Now to check characters that are in the guess and the answer but locations do not match
def non_matching_contained_in_answer_indexes(answer, guess):
    if len(guess) != len(answer):
        raise Exception("answers and guesses must be same length")
    matching_indexes = matching_character_indexes(answer, guess)
    matching_chars = matching_characters(answer, guess)

    answer_as_list = list(answer)
    contained_in_answer_indexes = []
    for index in range(len(answer)):
        #Check if guess is in the answer, and that it is not a matching index (or was a matching index earlier)
        if guess[index] in answer_as_list and index not in matching_indexes and guess[index] not in matching_chars:
            contained_in_answer_indexes.append(index)
    return contained_in_answer_indexes 

#Now to check characters that are in the guess and the answer but locations do not match
def non_matched_non_duped(answer, guess):
    if len(guess) != len(answer):
        raise Exception("answers and guesses must be same length")
    matching_indexes = matching_character_indexes(answer, guess)
    matching_chars = matching_characters(answer, guess)

    answer_as_list = list(answer)
    non_matching_non_dup_indexes = []
    for index in range(len(answer)):
        #Check if guess letter is not in the answer, and that it is not a matching index (and was not a matching index earlier)
        if guess[index] not in answer_as_list and index not in matching_indexes and guess[index] not in matching_chars:
            non_matching_non_dup_indexes.append(index)
    return non_matching_non_dup_indexes


def generic_wordle_round(answer, guess):
    matches = matching_character_indexes(answer, guess)
    non_matches_contained = non_matching_contained_in_answer_indexes(answer, guess)

    #remove duplicate letters from the no_matched set
    no_matched = non_matched_non_duped(answer,guess)

    return matches, non_matches_contained, no_matched















