file_path = input("Enter file path to file: ")
file = open(file_path)

character_counter = 0

for word in file:
    for character in word:
        character_counter += 1

print(f"Characters: {character_counter}")
