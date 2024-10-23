def read_file(file_path):
    # reads a file and returns its content as a string
    with open(file_path, 'r') as file:
        return file.read()

def count_word_occurrences(text, word):
    # counts the occurrences of a word in the given text
    return text.split().count(word)