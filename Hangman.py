import os
import random 
import time
os.system('cls')

# Your program code here
# Define categories and corresponding word lists
categories = {
    "animal": ["dog", "cat", "lion", "bird", "snake"],
    "food": ["pizza", "apple", "cake", "pasta", "sandwich"],
    "object": ["chair", "book", "phone", "computer", "car"], }
def choose_word():
    global TheCategorie
    category = random.choice(list(categories.keys()))
    word = random.choice(categories[category])
    TheCategorie = category
    return word


#-------------------Game Method--------------------------
def game() :
    secret_word = choose_word()
    guessed_letters = []
    Attempts = 6
    guessed =False
    word_completion ='_'*len(secret_word)
    time.sleep(1)
    print("Welcome to Hangman! You have 7 lives to guess.")
    time.sleep(2)
    print('Category : ', TheCategorie)
    time.sleep(1)
    draw_hanged_man(Attempts)
    time.sleep(1)
    print(word_completion)
    print ('\n')
    while guessed !=True and Attempts >0 :
        time.sleep(1)
        print('----------***--------------')
        UserGuess = input("Guess a letter: ").lower()

        if len(UserGuess) != 1 or not UserGuess.isalpha():
            print('Invalid guess. Please enter a single letter.')
            time.sleep(1)
            
        else:
            if UserGuess in guessed_letters:
              print('You already guessed that letter.')
              continue
            elif UserGuess in secret_word :
                time.sleep(1)
                print('Good guess!\n{} in the word'.format(UserGuess))
                guessed_letters.append(UserGuess)
                word_as_list = list(word_completion)
                indices = [i for i , letter in enumerate(secret_word) if letter == UserGuess]
                for index in indices:
                    word_as_list[index] = UserGuess
                word_completion = ''.join(word_as_list)
                if '_' not in word_completion:
                    guessed = True
            else :
                print('{} is not in the word' .format(UserGuess) )
                Attempts -= 1
                guessed_letters.append(UserGuess)
        
        time.sleep(1)
        draw_hanged_man(Attempts)
        time.sleep(1)
        print(word_completion)
        print('\n')
    #----------------------------------------------
    if guessed == True:
        print('You guessed the word! You win! THE WORD IS "{}"'.format(secret_word))
    else :
        print('You ran out of guesses! You lose. The word was: {}'.format(secret_word) )
#---------------------Main Method------------------------------
def main():
    game() 
    time.sleep(1) 
    play_again = input("Play again? (yes/no): ").lower() 
    while play_again== 'yes' :
     main() 
     continue   
    else:
      print("Thanks for playing!") 
      exit
#---------------------Draw Method-------------------------------      
def draw_hanged_man(Attempts):
    hanged_man = [
             r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/   \ |
|   | |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
 ---  |
/     |
|     |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ | \ |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
/ |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
 ---  |
  |   |
  |   |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
  O   |
      |
      |
      |
      |
      |
      |
      |
-------
""",
        r"""
  -----
  |   |
      |
      |
      |
      |
      |
      |
      |
      |
-------
""",
    ]

    print(hanged_man[Attempts])

#-----------------------------------------------------
#Run the game
main()


































