
#Wordle engine 

answer_word = ""
guess = ""

allowed_answers = []
allowed_guesses = []

#load in allowed answers and guesses 
with open('wordle-answers-alphabetical.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        allowed_answers.append(line[:-1])

with open('wordle-allowed-guesses.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        allowed_guesses.append(line[:-1])

number_of_possible_answers = len(allowed_answers)
number_of_possible_guesses = len(allowed_guesses)

#print(allowed_guesses[-3:])
#print(number_of_possible_answers)
#print(number_of_possible_guesses)



#These letters and their locations match
def matching_character_indexes(answer, guess):
    if len(guess) != len(answer):
        raise Exception("answers and guesses must be same length")

    matching_indexes = []
    for index in range(len(answer)):
        if answer[index] == guess[index]:
            matching_indexes.append(index)
    return matching_indexes

#Now to check characters that are in the guess and the answer but locations do not match
def non_matching_contained_in_answer_indexes(answer, guess):
    if len(guess) != len(answer):
        raise Exception("answers and guesses must be same length")
    matching_indexes = matching_character_indexes(answer, guess)

    contained_in_answer_indexes = []
    for index in range(len(answer)):
        if guess[index] in answer and index not in matching_indexes:
            contained_in_answer_indexes.append(index)
    return contained_in_answer_indexes 


















