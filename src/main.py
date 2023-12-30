from typing import List
import marisa_trie
from multiprocess import find_crosswords_multiprocessing
from file_utils import read_file_into_list, write_crosswords_to_file
from config import CROSSWORD_SIZE, INPUT_WORD_LIST_FILE, OUTPUT_CROSSWORDS_FILE, NUMBER_OF_PROCESSES


def filter_fixed_length_words(word_list: List[str], word_length=5):
    return [word for word in word_list if len(word) == word_length]


def main():
    word_list = filter_fixed_length_words(read_file_into_list(INPUT_WORD_LIST_FILE), CROSSWORD_SIZE)
    word_list = word_list[:6500]

    trie = marisa_trie.Trie(word_list)
    print(trie.keys(""))
    print(f"number of words = {len(word_list)}")

    crosswords = find_crosswords_multiprocessing(CROSSWORD_SIZE, trie, word_list,
                                                 number_of_processes=NUMBER_OF_PROCESSES)
    write_crosswords_to_file(crosswords, OUTPUT_CROSSWORDS_FILE)


if __name__ == "__main__":
    main()
