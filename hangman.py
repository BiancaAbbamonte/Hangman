import random
import hangman_art

from hangman_words import word_list

word = random.choice(word_list)


print(hangman_art.logo)
print(hangman_art.stages[6])
#print(word)


placeholder = ""
word_length = len(word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters = []
lives = 6


while not game_over:

    print(f"************************************{lives}/6 LIVES LEFT*****************************************")
    
    letter = input("Guess a letter: ").lower()


    if letter in correct_letters or letter in guessed_letters:
        print(f"You've already guessed {letter}")

    display = ""
    
    for i in word:
        if i == letter:
            display += i
            correct_letters.append(letter)
            guessed_letters.append(letter)
        elif i in correct_letters:
           display += i
        else:
            display += "_"
            guessed_letters.append(letter)

    print("Word to guess: " + display)

    if letter not in word:
       lives -= 1
       print(f"You guessed letter {letter}, that's not in the word. You lose a life.")
       
       if lives == 0:
          print("*************************************YOU LOSE*********************************************")
          print(f"The correct word was: {word}")
          game_over = True

    if "_" not in display:
        print("*************************************YOU WIN*********************************************")
        game_over = True
    
    print(hangman_art.stages[lives])