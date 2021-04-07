# Name: Rehber
# Reg. #: SP19-BCS-024
# Assignment: Hangman Game
# Submitted to: Mr. Junaid Ali Khan
# Date: 11/6/2019

import random

lines = open("words.txt").readlines()
lines = lines[0]
words = lines.split()

guess_word = []
secret_Word = random.choice(words) # lets randomize single word from the list
length_word = len(secret_Word)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []
print("H A N G M A N")


def figure(guess_left):

       if guess_left==8:
           print(fig8)
       elif guess_left==7:
           print(fig7)
       elif guess_left==6:
           print(fig6)
       elif guess_left==5:
           print(fig5)
       elif guess_left==4:
           print(fig4)
       elif guess_left==3:
           print(fig3)
       elif guess_left==2:
           print(fig2)
       elif guess_left==1:
           print(fig1)
       else:
           print(fig0)

fig8=('''
        -------
        |/
        |
        |
        |
        |
        |
        |
     ___|___ ''')
fig7=('''
         
       -------
       |/    |
       |    (_) 
       |    
       |
       |
       |
       | 
   ____|____   
        ''')
fig6=('''
         
       -------
       |/    |
       |    (_) 
       |     |
       |     |
       |     
       |
       | 
   ____|____   
        ''')
fig5=('''
         
       -------
       |/    |
       |    (_)
       |    \|
       |     |
       |     
       |
       | 
   ____|____   
        ''')
fig4=('''
         
       -------
       |/    |  
       |    (_) 
       |    \|/
       |     |
       |     
       |
       | 
   ____|____   
        ''')
fig3=('''
         
       -------
       |/
       |     |
       |    (_)
       |    \|/
       |     |
       |    / 
       | 
   ____|____   
        ''')
fig2=('''
         
       -------
       |/    |
       |    (_) 
       |    \|/ 
       |     |
       |    / \ 
       |    
       | 
   ____|____   
        ''')
fig1=('''
         
       -------
       |/    |
       |    (_) 
       |    \|/
       |     |
       |   _/ \ 
       |   
       |    
   ____|____   
        ''')
fig0=('''
         
       -------
       |/    |   
       |    (_) 
       |    \|/
       |     |
       |   _/ \_ 
       |   
       |    
   ____|____   
        ''')


def beginning():
    print("Hello Buddy!")

    while True:
        global name
        name = input("Please enter your name:")
        print("Let's play HANGMAN")

        if name == '':
            print("Please enter only letters:")
        else:
            break

def change():

    for character in secret_Word: # printing blanks for each letter in secret word
        guess_word.append("-")

    print("Ok, so the word you need to guess has", length_word, "characters.")

    print("Be aware that you can enter only 1 letter from a-z.")

    print(guess_word)
    



def guessing():
    guess_left = 8
    global score
    score = 0
    while guess_left !=0:


        guess = input("Pick a letter").lower()

        if not guess in alphabet: #checking input
            print("Enter a letter from a-z alphabet:")
            print("Incorrect guesses left:", guess_left)
        elif guess in letter_storage: #checking if letter has been already used
            print("Hey buddy! You have already guessed that letter! Try another one.")
            print("Incorrect guesses left:", guess_left)
            print(guess_word)
            
        else: 

            letter_storage.append(guess)
            if guess in secret_Word:
                print("You guessed correctly!")
                print("Incorrect guesses left:", guess_left)
                figure(guess_left)
                for x in range(0, length_word): 
                    if secret_Word[x] == guess:
                        guess_word[x] = guess
                print(guess_word)

                if not '-' in guess_word:
                    print("You won! The secret word is", secret_Word)
                    figure(guess_left)
                    score+=1
                    break
            else:
                print("The letter", guess, "is not in the word. Try Again!")
                guess_left -= 1
                print("Incorrect guesses left:", guess_left)
                figure(guess_left)
                print(guess_word)
                if guess_left == 0:
                    figure(guess_left)

def play_again():

    while True:
        user_choice = input("Would You Like To Play? If yes then enter YES or Y else NO or N:").upper()

        if user_choice == "YES" or user_choice == "Y":
               print("Have a nice day.")
               file=open("record.txt","a")
               print("Name     Score")
               file.write(str(name)+"     "+str(score))
               file.close()
               print(name,"    ",score)
               main()
        elif user_choice == "NO" or user_choice == "N":
            print("Have a nice day.")
            file=open("record.txt","a")
            print("Name     Score")
            file.write(str(name)+"     "+str(score))
            file.close()
            print(name,"    ",score)
            break       
        else:
            print("Please answer only Yes or No:")
            continue
              


def main():
       beginning()
       change()
       guessing()
       play_again()
main()       
