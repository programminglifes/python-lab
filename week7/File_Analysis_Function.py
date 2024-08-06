def analyze_file(file_name):
    """
    Analyze a file and display statistics.

    Args:
        file_name (str): Name of the file to analyze.

    Returns:
        None
    """
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            words = text.split()
            num_words = len(words)
            num_vowels = sum(1 for char in text.lower() if char in 'aeiou')
            num_spaces = text.count(' ')
            num_lowercase = sum(1 for char in text if char.islower())
            num_uppercase = sum(1 for char in text if char.isupper())

            print(f"File: {file_name}")
            print(f"Number of words: {num_words}")
            print(f"Number of vowels: {num_vowels}")
            print(f"Number of blank spaces: {num_spaces}")
            print(f"Number of lowercase letters: {num_lowercase}")
            print(f"Number of uppercase letters: {num_uppercase}")

    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

# Example usage:
analyze_file('file1.txt')
