""" 
This module holds the game where you can measure your typing speed when 
given a random sentence. 
"""
from argparse import ArgumentParser
import time
import random
import sys

class Game:
    """ 
    Contains functions that are required to run the game/type test.
    
    Attributes:
        sentence(a string of words): that will be formed using a csv file at
        random

        scores(dict): Contains the top scores in the game.
    """

    def __init__(self, words, path, time_used, nickname, wpm):
        self.words = words
        self.path = path
        self.time_used = time_used
        self.nickname = nickname
        self.wpm = wpm
        
    
    def get_sentence(words, path):
        """
        Obtains random words of a csv file and creates a sentence.

        Args:
            words(int): User inputted number
            path(.csv): contains a bunch of words that can be read

        Side Effects:
            Modifies the values inside sentence
        """
        wordlist = []
        newList=[]
        count = 0
        

        with open(path, 'r') as f:
            for line in f:
                wordlist += line.split()

        while(count < words):
            rand_index = random.randint(0, len(wordlist)-1)
            rand_word = str(wordlist[rand_index])
            newList.append(rand_word)
            count = count + 1
        print(newList)

        sentence = ' '.join(newList)
        return sentence
        


    def get_results(time_used, words):
        """
        Calculates and prints out the results of the game just played

        Args:
            time_used(int): A number of how long the user took to finish
            words(int): See above

        """
        score = int(words) / time_used

        return score

    def store_results(nickname, wpm):
        """
        Stores the results with a nickname that will stored with it inside 
        a dictionary that will be sorted by score and print into a text file.

        Side Effects: 
            Modifies leaderboard
        """
        if score >= 0 and score <= 60:
            return "Newb"
        if score >= 61 and score <= 80:
            return "Basic"
        if score >= 81 and score <= 99:
            return "Speedy"
        if score >= 100 and score <= 120:
            return "Flashster"
        if score >= 121 and score <= 140:
            return "Master Typer"
        if score >= 141 and score <= 160:
            return "Demi-God Typer"
        if score >= 161 and score <= 180:
            return "Ascended Typer"
        if score >= 181:
            return "Grandmaster Typer"
        
    def get_top_scores():
        """
        Gets the top scores that are stored into the text file and prints them
        out in sorted order.
        """
        tierlist = []
        with open(txt, 'r') as t:
            for line in t:
                for word in line.split("\n"):
                    tierlist.append(word)
        sortedlist = tierlist.sorted(word, key = len)
        return sortedlist
    
def main(filename):
    """
    Runs the game by prompting the user to start the game.
    """
    new_game = Game(None, filename, 0.0, None, 0.0)
    print("The speed type test has booted up")
    menu_choice = input("Please select one of the following:\n"\
        "1) Start a New Game \n2) Show Top Scores\n3) Exit\n")
    menu_choice = int(menu_choice)

    if menu_choice == 3:
        exit()
    elif menu_choice == 2:
        new_game.get_top_scores()
    elif menu_choice == 1:
        words = input("How many words would you like to type?\n")
        sentence = Game.get_sentence(int(words), filename)
        input("Press Enter to start")
        start_time = time.time()
        print(sentence)
        user_sentence = input()
        while str(sentence) != str(user_sentence):
            user_sentence = input("User sentence was wrong. "\
                "Please type it again.\n")
        end_time = time.time()
        total_time = (end_time - start_time)/60
        print("Your wpm is " + str(Game.get_results(total_time,words)))



def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("filename", help = "Name/ path to text file for words")
    return parser.parse_args(arglist)


if __name__ == "__main__":
        args = parse_args(sys.argv[1:])
        main(args.filename)
