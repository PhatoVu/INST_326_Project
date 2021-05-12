# INST_326_Project

Files:

    ramdomwords.txt - A text document that contains 2000 randomly generated
        words and is used to create a random sentence using type_test_game and
        its get_sentence().
    
    test_game.py - The pytest script that tests functions for type_test_game

    TopScores.txt - A text file that holds the scores of those who want their
    scores to be stored. It includes a nickname and the associated score.

    type_test_game.py - The main file that includes the Game class and the main
    function that runs the game.

CMD Run Instructions:

    To properly run the game you must run the type_test_game.py file which needs
    a single parameter which will be the file name for the text file of words
    used to help create your sentence. For this case use:

        python type_test_game.py randomwords.txt

How to operate the game:

    When you first launch the game you are greeted with a menu of things to do.
    There are 3 options. One option is to exit the game which will close just
    close out the game. The second is a show top scores option which will return
    the top 10 scores inside the TopScores.txt file. The last is running the 
    actual game itself. Once it starts you are asked for an input of how many 
    words you want to type. It will pause and wait for you to press enter before
    the sentence is showed and the timer starts. When the input is wrong it will
    ask you to try again until you get it right. It will take the time you've
    taken and words typed to calculate you wpm or words per minute. You will
    then be asked to store the results which you can input Y/N. If Y is said
    then it'll ask for a nickname. If you say N you are allowed to see your rank
    that is associated with your wpm. If you say N then the program will exit.