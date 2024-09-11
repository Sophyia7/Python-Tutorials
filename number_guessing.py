import random 

def number_guessing_game(attempts_limit=7):
  number_to_guess = random.randint(1, 100)
  guessed_correctly = False
  attempts = 0


  print("Welcome to Number guessing game")
  print("I have selected a number from 1-100, can you guess it?")

  while attempts < attempts_limit and not guessed_correctly:
    try:
      guess = int(input("Please add your guess: "))
      attempts +=1

      if guess < number_to_guess:
        print("Too low!")
      elif guess > number_to_guess:
        print("Too high")
      else:
        guessed_correctly = True
        print(f"Congratulaitions, you guessed the number in {attempts} attempts")

    except ValueError:
      print("Oops! This is not a valid number, please a whole number")

  if not guessed_correctly:
    print(f"You are out of guesses, the correct guess was {number_to_guess}")
  
  print("Game over, Thanks for playing!")

number_guessing_game()




  



