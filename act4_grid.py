while True:
    try:
        size = int(input("Size: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if 1 <= size <= 10:
        break
    print("Size must be between 1 and 10.")

for row in range(1, size + 1):
    for col in range(1, size + 1):
        print(f"{row * col:>4}", end=" ")
    print()
