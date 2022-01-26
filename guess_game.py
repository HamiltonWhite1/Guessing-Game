
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
    if play == "N": ###if player does not want to play, end the game
        playing == False
    elif play == "Y": ###if player does want to play the game...
        while playing:
            category_choice = input("There are three categories to choose from. 'Pokemon', 'Movies', 'Video Games' and 'Countries'. Type in which category you would like to use?: ").title() ###player chooses the category to grab the random word from
            if category_choice not in CATEGORY_DICT: ###if the 'choice' the player made is not a key in CAT_DICT above, end the game
                print("Sorry, that was not a choice. Try playing again.")
                playing = False ####ends loop
            elif category_choice in CATEGORY_DICT: ### if the choice is a key in CAT_DICT...
                print("Okay, a word has been selected for you. Time to Guess!")
                cat_key = category_choice ####sets the dict key for the above random_word function to pull the random word
                secret_word = random_word(category_choice) ####set variable secret_word to the randomly generated word from random_word function above
                secret_underscore = underscore_presentation(category_choice) ###generates and assigns a string of underscores to the secret_underscore variable. This will be presented to the player at every instance of the below while loop
                while tries < 7: ###while tries variable is less than 7
                    score_keep = "_" ###variable stored to check if any more underscores are in the secret word
                    print(secret_underscore)
                    guess = input("What is your guess?") ###player input to guess letter in word
                    if guess in secret_word:
                        replace_ind = secret_word.index(guess) ###assigns an integer to replace_ind to be used as an index
                        secret_underscore = secret_underscore.split() ###splits the string into a list
                        secret_underscore[replace_ind] = guess ####replaces the value at the index with the player guess
                        secret_underscore = ' '.join(secret_underscore) ###rejoins the list into a string with 1 less underscore, if an included letter was guessed
                    tries += 1 ###increment tries by 1 after every loop
                    if tries == 7: ###if tries is == 7, ask the player to make a final guess
                        first_final_guess = input(f"Please make a guess at which {category_choice} this is.: ").lower()
                        if first_final_guess == secret_word: ### if guess is correct
                            tries = 9
                        else: ### if guess wrong
                            tries = 8
                    if score_keep not in secret_underscore: ##if there are no more underscores in the secret word
                        tries = 9### tries = 9
                        playing = False ###end loop
                    if tries == 9: ###if tries == 9
                        playing = False ###end loop
                        print(f"Congratulations, you won! The secret word was {secret_word}") ###congrats, player wins
                    if tries == 8: ###if tries == 8
                        print("It looks like you ran out of tries. Better luck next time!") ###player loses
                        playing = False ###end loop
main()
