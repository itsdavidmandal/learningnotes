import random

def guess_the_number():
  """
  This function implements the number guessing game logic.
  """
  # Generate a random number between 1 and 100
  secret_number = random.randint(1, 100)
  guess_count = 0

  # Start the guessing loop
  while True:
    try:
      guess = int(input("Guess a number between 1 and 100: "))
      guess_count += 1

      if guess < secret_number:
        print("Too low, try again!")
      elif guess > secret_number:
        print("Too high, try again!")
      else:
        # User guessed the number!
        print(f"Congratulations! You guessed the number in {guess_count} tries.")
        break

    except ValueError:
      print("Invalid input. Please enter a number.")
# Run game logic and print welcome message only when script is executed directly
if __name__ == "__main__":
  print("Welcome to the Number Guessing Game!")
  guess_the_number()
