import random

max_attempts = 10;
max_number = 40;

ale = random.randint(1, max_number)  # Generate a random number between 1 and max_number



def temperature_adjuster(ale, max_attempts):
  """
  Random number guesser, input: ale(random number to guess), max_attempts(max number of guesses)
  """
  num = 0  # Initialize player's guessed number
  try_count = 0  # Initialize attempt counter

print("We have activated the heating in the offices and we don't know if the temperature is right, we have to adjust it so that people feel comfortable.")

  while (ale != num) and (try_count < max_attempts):
    # Prompt the player to input a guess
    num = int(input("How many degrees we put?: "))
    try_count += 1  # Increment attempt counter

    if ale == num:
      # If guess is correct, notify player of their win and attempts used
      print("Perfect!, the room its perfect now. You used ", try_count, "attempts!")
    elif ale > num:
      # If guess is too low, provide feedback
      print("Its hot here!")
    elif ale < num:
      # If guess is too high, provide feedback
      print("Its cold here!")

  if ale != num:
    # If the player fails to guess within 10 attempts, notify them
    print("You have exceeded the number of attempts:", try_count)

# Start the game by calling the function
temperature_adjuster(ale, max_attempts)