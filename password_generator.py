import random 

# File containing words
word_file = "words.txt"
word_list = []

# Read words from the file 
with open(word_file, 'r') as words: 
    for line in words: 
        word = line.strip().lower()  # Remove whitespace and lowercase the words
        if 3 < len(word) < 8:  # Check if the word length is between 4 and 7
            word_list.append(word)

def generate_password(): 
    password = ""
    for i in range(3):  
        password += word_list[random.randint(0, len(word_list) - 1)]  # Use word_list instead of words
    return password

# Print the generated password
print("Generated password is: ", generate_password())