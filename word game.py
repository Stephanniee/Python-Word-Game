import random

name = input("What is your name? ")

print("Welcome & Good Luck!", name)

word_list = ['aladdin', 'hercules', 'pocahontas', 'cinderella',
             'mulan', 'dumbo', 'tarzan', 'bambi',
             'tangled', 'brave', 'frozen', 'moana', 'maleficent']

word = random.choice(word_list)
# This will choose one random word from this list of words

spaces = ['_'] * len(word)
# Show spaces

incorrect_guesses = 0  
# Counter for incorrect guesses

max_attempts = 10  
# Maximum number of attempts allowed

def get_letter_position(guess, word, spaces):
    index = word.find(guess)
    while index != -1:
        spaces[index] = guess
        index = word.find(guess, index + 1)
    return spaces
# Created and set a variable called index to be -1
# Created a loop to continue to look through the word for every single position where that letter exists
# This is the special character that will let us know that the character is removed from the word

def win_check():
    if '_' not in spaces:
        return True
    return False
# Checks if the player has guessed the right word

while incorrect_guesses < max_attempts:
    guess = input('Guess a letter: ')

    if guess in word:
        spaces = get_letter_position(guess, word, spaces)
        print(spaces)
        if win_check():
            print('Congratulations, you won!')
            break
# This will show the player that they have won

    else:
        print('Sorry, that letter is not in the word.')
        incorrect_guesses += 1
# This will show the player has not got the right word

if incorrect_guesses == max_attempts:
    print('Sorry, you lost. The word was:', word)
# This will show no attempts left anf tells the player has lost 