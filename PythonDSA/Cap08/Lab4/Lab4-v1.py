# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
from os import system, name
# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
     def __init__(self, hangman, word,tries):
          self.hangman = hangman
          self.word = word
          self.trace_list = ["-" for x in self.word]
          self.tries = tries
          self.wrong_letters = []
          print("Welcome to hangaman game!")
	# Método para adivinhar a letra
     def guess(self,letter):
          cont = 0
          self.letter = letter
          if self.letter in self.word:
               for x in self.word:
                    if self.letter == x:
                         self.trace_list[cont] = x
                    cont += 1
               return [self.trace_list, True]
          else:
               self.tries -= 1
               self.wrong_letters.append(self.letter)
               return [self.trace_list, False]

	# Método para verificar se o jogo terminou

     def finish(self, win_or_loose):
          if win_or_loose == True :
               return True
          else:
               return False
          
	# Método para verificar se o jogador venceu
     def win(self):
          print(self.trace_list)
          if '-' not in self.trace_list:
               print("You won!")
               return True
          elif self.tries == 0:
               print("You loose")
               return True
          else:
               return False
               
	# Método para não mostrar a letra no board
     def clear(self):
          if name == 'nt':
               _ = system('cls') # _ means I don't want to save the return of the func "system()"
          #Mac or Linux
          else:
               _ = system('clear')
          	
	# Método para checar o status do game e imprimir o board na tela
     def check(self):
          tries = self.tries + 1
          print(self.hangman[-tries])
          print("Palavra: ", self.trace_list)
          print("\n Chances left: ", self.tries)
          print("Wrong letters: "," # ".join(self.wrong_letters))
          
words = ["arroz","bife", "cenoura", "uva"]
word_sorted = random.choice(words)
game = Hangman(board,word_sorted, 6)

finish = False
while(finish != True):
     guess = input("Type a letter: ")
     var = game.guess(guess)
     finish = game.finish(game.win())
     game.clear()
     game.check()
     
game.win()
print("The word was: ", word_sorted)

