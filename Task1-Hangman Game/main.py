import random

animals = ['lion', 'tiger', 'elephant', 'kangaroo', 'zebra', 'wolf']
birds = ['parrot', 'peacock', 'crow', 'pigeon', 'swan', 'sparrow']
fruits = ['orange', 'apple', 'banana', 'grapes', 'cherry', 'watermelon']
colors = ['green', 'black', 'white', 'purple', 'violet', 'orange']
sports = ['cricket', 'badminton', 'hockey', 'football', 'basketball', 'volleyball']
themes = [animals, fruits, birds, colors, sports]
hangman = [
    '''  
 +---+
     |
     |
     |''',
    ''' 
 +---+
 O   |
     |
     |''',
    '''  
 +---+
 O   |
 |   |
     |''',
    '''  
 +---+ 
 O   |
/|   |
     |''',
    '''  
 +---+
 O   |
/|\  |
     |''',
    '''   
 +---+
 O   |
/|\  |
/    |''',
    '''  
 +---+
 O   |
/|\  |
/ \  |'''

]
print("WELCOME TO THE HANGMAN GAME")
pts = 0
k = 1
while k > 0:
    print(
        "-------------------------------------------------------------------------------------------------------------------")
    print("Choose the theme from the list below by giving the appropriate number...For exiting the game choose 6")
    print("1.Animals\n"
          "2.Fruits\n"
          "3.Birds\n"
          "4.Colors\n"
          "5.Sports\n"
          "6.Exit\n"
          )
    j = int(input("Enter your choice: "))
    if j > 6 or j < 1:
        print("Enter proper choice:")
    elif j == 6:
        print(f"FINAL SCORE={pts}")
        print("THANK YOU:)")
        exit(0)
    else:
        display = []
        miss = []
        hang = 0

        word_list = themes[j - 1]

        ch = random.choice(word_list)
        # Display the random word chosen
        # print(f"The word is: {ch.title()}")
        # create an empty list called display
        # for each letter in the choosen word add an _ ...number of '_' should be the length of the word chosen
        print(f"The number of letters in the word is {len(ch)}")
        for i in range(len(ch)):
            display.append("_")
        print(*display)
        print("\n")
        print(hangman[hang])
        # Ask the user for the letter he is guessing and save it in guess and make them all into lowercase
        # Choose a random word from word_list and save it in ch
        for i in range(15):
            guess = input("Guess the Letter: ").lower()

            # see if the guess is in ch
            if guess in ch:
                print("You are right")
                print("--------------------------------------------------------------------------------")
                pts += 1
            else:
                miss.append(guess)
                hang += 1
                print("Go again!!")
                print("--------------------------------------------------------------------------------")
            print(f"Missed guesses:{miss}")
            print(hangman[hang])
            if hang == 6:
                print(f"YOU HAVE LOST THE GAME!!..THE WORD IS {ch}")
                print(f"POINTS:{pts}")
                print("GAME OVER")
                break
            # Loop through each position, if the guessed letter and the letter match then display the word at that position
            for v in range(len(ch)):
                if ch[v] == guess:
                    display[v] = guess
            print(*display)
            if '_' not in display:
                print("YOU HAVE WON:)!!")
                print(f"POINTS:{pts}")
                print("GAME OVER")
                break
        if '_' in display:
            pass
