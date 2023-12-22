from typing import List
from squarecrossword import SquareCrossword
import random

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


def find_crosswords(trie, word_length):
    crossword = SquareCrossword(word_length)
    crossword_word_indexes = [0] * word_length * 2

    while True:
        # crossword.print_crossword()
        potential_words = trie.keys(crossword.get_next_prefix())  # Note this also calculated in is_legal
        # print(f"next prefix = {crossword.get_next_prefix()}")
        # print(f"potential_words = {potential_words}")
        current_position_try_number = crossword_word_indexes[crossword.get_build_stage()]
        # print(f"next current_position_try_number = {current_position_try_number}")
        # Tried all words from current crossword position
        if current_position_try_number >= len(potential_words):
            # print(f"exhausted possibilities")
            crossword_word_indexes[crossword.get_build_stage()] = 0
            crossword.remove_word()
            continue
        crossword_word_indexes[crossword.get_build_stage()] += 1
        crossword.place_word(potential_words[current_position_try_number])
        if not crossword.is_legal(trie):
            # print(f"crossword isn't legal")
            crossword.remove_word()
            continue
        if crossword.get_build_stage() == (word_length * 2):
            crossword.print_crossword()
            crossword.remove_word()
            # return crossword


def main():
    word_length = 5
    word_list = filter_fixed_length_words(read_file_into_list("../words.txt"), word_length)
    word_list.sort()

    # random.shuffle(word_list)
    print(f"number of words = {len(word_list)}")
    trie = marisa_trie.Trie(word_list)
    # print(trie.keys("ab"))

    find_crosswords(trie, word_length)

    # crossword1 = SquareCrossword(["chess", "crate", "snafu", "balls", "slime"])
    # crossword1.print_crossword()


if __name__ == "__main__":
    main()
