# retrieves the text utility module
from .text_utils import read_file, count_word_occurrences

# makes a function that analyzes token values in file
def run_prompt(file_path, token):
    # generates a prompt by reading a file and counting occurrences of token
    text = read_file(file_path)  # Read the corpus file
    # count 
    count = count_word_occurrences(text, token)
    
    # run the prompt
    return f"The token '{token}' appears {count} times in the corpus."