from typing import List

from tabulate import tabulate
import marisa_trie
from simple_colors import *


def read_file_into_list(file_path):
    word_list = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Remove leading and trailing whitespaces and add words to the list
                word_list.extend(line.strip().split())
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred while trying to open file: {e}")

    return word_list


def filter_fixed_length_words(word_list: List[str], word_length=5):
    return [word for word in word_list if len(word) == word_length]


def print_crossword(words):
    # print(cyan(tabulate(words), 'bright'))
    print(cyan(tabulate(words), ['bright', 'reverse']))

# algorithm
# def find_crosswords(word_list, trie, word_length=5):
#     potential_crossword = []
#     remaining_words = word_list
#     for level in range(word_length):
#         potential_crossword.extend(remaining_words[0])
#         remaining_words.pop(0)
#

# def is_legal_crossword(words):
    

def main():
    word_list = filter_fixed_length_words(read_file_into_list("../words.txt"))
    word_list.sort()

    print(f"number of words = {len(word_list)}")
    trie = marisa_trie.Trie(word_list)
    # print(trie.keys("ab"))

    print_crossword(["chess", "crate", "snafu", "balls", "slime"])


if __name__ == "__main__":
    main()
