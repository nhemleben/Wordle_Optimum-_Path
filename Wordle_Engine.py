
#Wordle engine 

answer_word = ""
guess = ""

allowed_answers = []
allowed_guesses = []

with open('wordle-allowed-guesses.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        allowed_guesses.append(line)

print(allowed_guesses[:10])

 












