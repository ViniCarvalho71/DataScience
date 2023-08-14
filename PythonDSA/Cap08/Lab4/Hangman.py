import random
from os import system, name

def clear_screen():
    #Windows
    if name == 'nt':
        _ = system('cls') # _ means I don't want to save the return of the func "system()"
    #Mac or Linux
    else:
        _ = system('clear')

def display_hangman(i):
    clear_screen()
    dummie = ["""
    -------------
    |           |
    |          ( )
    |          \\|/
    |           |
    |          / \\
    |            
    
    """,
    """
    -------------
    |           |
    |          ( )
    |          \\|/
    |           |
    |          / 
    |            
    
    """,
    """
    -------------
    |           |
    |          ( )
    |          \\|/
    |           
    |          
    |            
    
    """,
    """
    -------------
    |           |
    |          ( )
    |          \\|
    |          
    |            
    
    """,
    """
    -------------
    |           |
    |          ( )
    |          
    |           
    |          
    |            
    
    """,
    """
    -------------
    |           |
    |          
    |          
    |           
    |          
    |            
    
    """,
    """
    -------------
    |           
    |          
    |          
    |           
    |          
    |            
    
    """]
    return(dummie[i])
    
def game():

    clear_screen()
    print("\nWelcome to the Hangman!")
    print("Guess the word bellow:\n ")

    words = ['rice', 'bread', 'cherry', 'car', 'street', 'vinícius']

    word = random.choice(words)
    discovered_letters = ['_' for letter in word]
    chances = 6
    wrong_letters = []

    while(chances > 0):
        print(display_hangman(chances))
        print("Palavra: ",discovered_letters)
        print("\n Chances left: ", chances)
        print("Wrong letters: "," # ".join(wrong_letters))

        tries = input("\nInput a letter: ").lower()

        if tries in word:
            index = 0
            for letter in word:
                if letter == tries:
                    discovered_letters[index] = letter
                index += 1
        else:
            
            chances -= 1
            wrong_letters.append(tries)

        if '_' not in discovered_letters:
            print("\nYou won, the worrd was: ", word)
            break
    if '_' in discovered_letters:
        print(display_hangman(chances))
        print("\nYou loose, the word was: ", word)

if __name__ == '__main__':
    game()

