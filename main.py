hangman = ['''
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
import random
print("Welcome to guessing game.\n")
sequence= ["One", "Two", "Three", "Four", "Five", "Six","Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen","Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen","Nineteen","Twenty"]
word=(random.choice(sequence)).lower()
list_word=list(word)
blank_list=[]
for i in list_word:
  blank_list.append('_')
blank_word=' '.join(blank_list)
print(blank_word+"\n")
guess=True
i=0
while(guess==True):
  input_letter=input("Enter Your Guess : ").lower()
  if input_letter in word:
    list_word[word.index(input_letter)]='_'
    blank_list[word.index(input_letter)]=input_letter
    blank_word=' '.join(blank_list)
    print(blank_word)  
    word=''.join(list_word)
    if blank_word.find('_')== -1:
      print("You Win")
      guess=False
  else:
    print(blank_word)  
    print(hangman[i])
    i+=1
    if i==7:
      print("You are Lost.")
      guess=False