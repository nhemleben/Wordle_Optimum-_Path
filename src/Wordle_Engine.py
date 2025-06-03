#Wordle engine 
import random

allowed_answers = []
allowed_guesses = []

#load in allowed answers and guesses 
with open('wordle-answers-alphabetical.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        allowed_answers.append(line.strip('\n'))

with open('wordle-allowed-guesses.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        allowed_guesses.append(line.strip('\n'))

number_of_possible_answers = len(allowed_answers)
number_of_possible_guesses = len(allowed_guesses)


def generate_random_answer():
    rand_index = random.randint(0,number_of_possible_answers)
    return allowed_answers[rand_index]

def generate_random_guess():
    rand_index = random.randint(0,number_of_possible_guesses)
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


def generic_wordle_round(answer, guess):
    matches = matching_character_indexes(answer, guess)
    non_matches = non_matching_contained_in_answer_indexes(answer, guess)
    return matches, non_matches















