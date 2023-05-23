#	Write a program to find the frequency of each word in a string.

def count_word_frequency(string):
    # Remove punctuation marks and convert string to lowercase
    string = string.lower()
    string = string.replace(".", "").replace(",", "").replace("!", "").replace("?", "").replace(":", "")

    # Split the string into words
    words = string.split()

    # Create a dictionary to store word frequencies
    word_freq = {}

    # Count the frequency of each word
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_freq


# Get input string from the user
input_string = input("Enter a string: ")

# Call the function to count word frequencies
frequency = count_word_frequency(input_string)

# Display the word frequencies
print("Word frequencies:")
for word, freq in frequency.items():
    print(f"{word}: {freq}")
