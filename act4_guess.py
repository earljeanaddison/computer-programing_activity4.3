secret_number = 27
tries = 0

while True:
    guess = int(input("Guess: "))
    tries += 1

    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")
    else:
        print(f"Correct! You got it in {tries} tries.")
        break
