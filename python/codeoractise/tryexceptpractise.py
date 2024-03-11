def get_user_age():
  """
  This function prompts the user for their age and returns it as an integer.
  """
  """
  This function prompts the user for their age, validates the input, 
  and returns the age as an integer if valid.

  Steps:
  1. Prompts the user to enter their age using input("Enter your age: ")
  2. Wraps the user input in a try block to handle potential ValueError exceptions.
     - Attempts to convert the input to an integer using int(input(...))
  3. Within the try block, checks if the age is negative:
     - If negative, raises a ValueError with a custom message "Age cannot be negative".
  4. If the input is valid (integer and non-negative), returns the age.
  5. An except block handles any ValueError exceptions:
     - Prints an informative error message "Invalid input:" followed by the specific error details from the exception object (e).
     - Returns None to indicate that the age could not be retrieved due to invalid input.
  6. A finally block executes regardless of exceptions:
     - Prints a thank you message "Thanks for using the program!"

  This function ensures the user enters a valid age and provides informative messages 
  for both successful and unsuccessful input attempts.
  """
  try:
    age = int(input("Enter your age: "))
    if age < 0:
      raise ValueError("Age cannot be negative")
    return age
  except ValueError as e:
    print("Invalid input:", e)
    return None
  finally:
    print("Thanks for using the program!")

# Get user age
user_age = get_user_age()

if user_age:
  print(f"You are {user_age} years old.")
else:
  print("Failed to get your age.")
