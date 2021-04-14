""" 
This module holds the game where you can measure your typing speed when 
given a random sentence. 
"""

class Game:
    """ 
    Contains functions that are required to run the game/type test.
    
    Attributes:
        sentence(a string of words): that will be formed using a csv file at
        random

        time_used(int): The time that the player takes to type the sentence

        leaderboard(dict): Contains the top scores in the game.
    """

    def get_sentence(words):
        """
        Obtains random words of a csv file and creates a sentence.

        Args:
            words(.csv): contains a bunch of words that can be read

        Side Effects:
            Modifies the values inside sentence
        """

    def timer():
        """
        Keeps track of how long the player takes to type out the sentence

        Side Effects:
            Modifies the value time_used
        """

    def get_results(time_used, sentence)
        """
        Calculates and prints out the results of the game just played

        Args:
            time_used(int): See above
            sentence(string): See above

        """

    def store_results()
        """
        Stores the results with a nickname that will stored with it inside 
        a dictionary that will be sorted by score.

        Side Effects: 
            Modifies leaderboard
        """

    if __name__ == "__main__":