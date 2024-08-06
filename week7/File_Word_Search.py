def search_words_in_file(file_path, words_to_search):
    """
    Searches for given words in a file and displays the results.

    Args:
        file_path (str): Path to the file to be searched.
        words_to_search (list): List of words to search for.

    Returns:
        None
    """
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            for word in words_to_search:
                if word.lower() in file_content.lower():
                    print(f"'{word}' found in the file.")
                else:
                    print(f"'{word}' not found in the file.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

# Example usage
file_path = input("Enter the file path: ")
words_to_search = input("Enter the words to search for (separated by commas): ").split(',')

# Strip leading and trailing whitespaces from each word
words_to_search = [word.strip() for word in words_to_search]

search_words_in_file(file_path, words_to_search)
