# take file path as input
# open file with read
# iterate through file - line in file, word in line, character in word

file_path = input("Enter file path to file: ")
file = open(file_path)

character_counter = 0

for word in file:
    for character in word:
        character_counter += 1

print(f"Characters: {character_counter}")