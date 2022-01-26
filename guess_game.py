from dataclasses import replace
import random

CATEGORY_DICT = {
    "Pokemon": ["pikachu", "pidgey", "ivysaur"],
    "Movies": ["irobot", "starwars", "interstellar"],
    "Countries": ["germany", "norway", "denmark"],
    "Video Games": ['pokemon', "dota", 'csgo'],
}
value_ind = random.randint(0,2) ###creating a random indice within the range of my lists

###simple introductory instructions to the program
def instructions():
    print("""Welcome to the random word guessing game. There are 4 categories, and 3 potential words from each category you can guess.
Good luck!""")
instructions()

###function that utilizes the "random" Python package assigned to value_ind above, and the player choice as the categorical key for above dictionary, to choose
### which word from the dict will be used in the guessing game
def random_word(a): 
    cat_key = a
    secret_word = CATEGORY_DICT[f"{cat_key}"][value_ind]
    return secret_word

###function that creates a string of underscores (1 space between each) to represent the length of the secret word
def underscore_presentation(a):
    secret_underscore = "_ "*len(random_word(a))
    return secret_underscore

###main function of the program
def main():
    tries = 0 ##first condition for the loop to run
    playing = True ###second condition for the loop to run
    play = input("Would you like to play? Y/N: ").upper() ###asking user if they would like to play
    if play == "N":
        playing == False
    elif play == "Y":
        while playing:
            category_choice = input("There are three categories to choose from. 'Pokemon', 'Movies', 'Video Games' and 'Countries'. Type in which category you would like to use?: ").title()
            if category_choice not in CATEGORY_DICT:
                print("Sorry, that was not a choice. Try playing again.")
                playing = False
            elif category_choice in CATEGORY_DICT:
                print("Okay, a word has been selected for you. Time to Guess!")
                cat_key = category_choice
                secret_word = random_word(category_choice)
                secret_underscore = underscore_presentation(category_choice)
                while tries < 7:
                    score_keep = "_"
                    print(secret_underscore)
                    guess = input("What is your guess?")
                    if guess in secret_word:
                        replace_ind = secret_word.index(guess)
                        secret_underscore = secret_underscore.split()
                        secret_underscore[replace_ind] = guess
                        secret_underscore = ' '.join(secret_underscore)
                    tries += 1
                    if tries == 7:
                        first_final_guess = input(f"Please make a guess at which {category_choice} this is.: ").lower()
                        if first_final_guess == secret_word:
                            tries = 9
                        else:
                            tries = 8
                    if score_keep not in secret_underscore:
                        tries = 9
                        playing = False
                    if tries == 9:
                        playing = False
                        print(f"Congratulations, you won! The secret word was {secret_word}")
                    if tries == 8:
                        print("It looks like you ran out of tries. Better luck next time!")
                        playing = False           
main()
