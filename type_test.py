""" 
This module holds the game where you can measure your typing speed when 
given a random sentence. 
"""
import timer
import random

class Game:
    """ 
    Contains functions that are required to run the game/type test.
    
    Attributes:
        sentence(a string of words): that will be formed using a csv file at
        random

        scores(dict): Contains the top scores in the game.
    """

def __init__():
    leaderboard = {}
    
    def get_sentence(words, path):
        """
        Obtains random words of a csv file and creates a sentence.

        Args:
            words(int): User inputted number
            path(.csv): contains a bunch of words that can be read

        Side Effects:
            Modifies the values inside sentence
        """

        with open(path, 'r') as f:
            for line in f:
                for word in line.split("\n"):
                    wordlist.append(word)
        sentence = random.choice(wordlist)
        return sentence


    def get_results(time_used, words):
        """
        Calculates and prints out the results of the game just played

        Args:
            time_used(int): A number of how long the user took to finish
            words(int): See above

        """
        score = words / time_used

        return score

    def store_results(nickname, wpm):
        """
        Stores the results with a nickname that will stored with it inside 
        a dictionary that will be sorted by score and print into a text file.

        Side Effects: 
            Modifies leaderboard
        """

        leaderboard.add()

    def get_top_scores():
        """
        Gets the top scores that are stored into the text file and prints them
        out in sorted order.
        """
 
def main(filename):
    """
    Runs the game by prompting the user to start the game.
    """
    new_game = Game()
    print("The speed type test has booted up")
    menu_choice = input("Please select one of the following: \n \
        1) Start a New Game \n 2) Show Top Scores \n 3) Exit")
    menu_choice = int(menu_choice)

    if menu_choice == 3:
        exit()
    elif menu_choice == 2:
        new_game.get_top_scores()
    elif menu_choice == 1:
        words = input("How many words would you like to type?\n")
        sentence = new_game.get_sentence(filename, int(words))
        input("Press Enter to start")
        start_time = time.time()
        user_sentence = input()
        while sentence != user_sentence:
            user_sentence = input("User sentence was wrong. \
                Please type it again.")
        end_time = time.time()
        total_time = (end_time - start_time)/60
        new_game.get_results(total_time,words)




if __name__ == "__main__":
        args = parse_args(sys.argv[1:])
        main(args.filename, args.word, args.time_used, args.sentence)
