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
    """
        
    def get_sentence(self, words, path):
        """
        Obtains random words of a csv file and creates a sentence.

        Args:
            words(int): User inputted number
            path(.csv): contains a bunch of words that can be read
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

        sentence = ' '.join(newList)
        return sentence
        


    def get_results(self, time_used, words):
        """
        Calculates and prints out the results of the game just played

        Args:
            time_used(int): Time converted into minutes of how long the user 
            took to finish
            words(int): See above

        """
        score = int(words) / time_used

        return score

    def store_results(self, nickname, score):
        """
        Stores the results with a nickname that will stored inside a text file.
        
        Args:
            nickname(str): A name that associates with the score.
            score(float): The score that the player has achieved.
        """

        f = open("TopScores.txt", "a+")
        print(str(nickname) + ", " + str(score), file = f)
        f.close()


    def get_rank(self, score):
        """
        Takes the users score and returns them their rank based on their score.

        Args:
            score(float): see above.

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
        

    def get_top_scores(self):
        """
        Gets the top scores that are stored into from text file and prints them
        out in sorted order.
        """
        topscores = []
        with open("TopScores.txt", 'r') as f:
            for line in f:
                temp = line.split(",")
                topscores.append((temp[0], temp[1].strip()))
        
        sortedlist = sorted(topscores, key = lambda x: x[1], reverse=True)
        return sortedlist[0:10]
    
    
def main(filename):
    """
    Runs the game by prompting the user to start the game.
    """
    new_game = Game()
    print("The speed type test has booted up.\n")
    menu_choice = input("Please select one of the following:\n"\
        "1) Start a New Game \n2) Show Top Scores\n3) Exit\n")
    menu_choice = int(menu_choice)

    if menu_choice == 3:
        exit()
    elif menu_choice == 2:
        print(*new_game.get_top_scores(), sep='\n')
    elif menu_choice == 1:
        words = input("How many words would you like to type?\n")
        sentence = new_game.get_sentence(int(words), filename)
        input("Press Enter to start")
        print(sentence)
        start_time = time.time()
        user_sentence = input()
        while str(sentence) != str(user_sentence):
            user_sentence = input("User sentence was wrong. "\
                "Please type it again.\n")
        end_time = time.time()
        total_time = (end_time - start_time)/60
        score = new_game.get_results(total_time,words)
        print("Your wpm is " + str(score))
        answer = input("Would you like to store your results? (Y/N)\n").upper()
        if(answer == "N"):
            input("Would you like to see your rank? (Y/N)\n")
            if(answer == "N"):
                exit()
            elif(answer == "Y"):
                print(new_game.get_rank(score))
                exit()
        elif(answer == "Y"): 
            nickname = input("Please enter a nickname: ")
            new_game.store_results(nickname, score)
            print("Results stored.")
            exit()




def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("filename", help = "Name/ path to text file for words")
    return parser.parse_args(arglist)


if __name__ == "__main__":
        args = parse_args(sys.argv[1:])
        main(args.filename)
    
