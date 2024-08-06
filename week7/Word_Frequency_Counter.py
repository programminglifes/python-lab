def find_most_frequent_word(file_path):
    """
    Reads text from a file, finds the word with the most number of occurrences, and returns the result.

    Args:
        file_path (str): Path to the text file.

    Returns:
        tuple: A tuple containing the most frequent word and its frequency.
    """
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            word_freq = {}

            for word in words:
                word = word.lower()  # Convert to lowercase for case-insensitive comparison
                if word not in word_freq:
                    word_freq[word] = 1
                else:
                    word_freq[word] += 1

            most_frequent_word = max(word_freq, key=word_freq.get)
            frequency = word_freq[most_frequent_word]

            return most_frequent_word, frequency
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None, None

# Example usage
file_path = input("Enter the file path: ")
most_frequent_word, frequency = find_most_frequent_word(file_path)

if most_frequent_word:
    print(f"The most frequent word is '{most_frequent_word}' with a frequency of {frequency}.")
