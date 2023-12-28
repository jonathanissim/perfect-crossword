from typing import List
import random
import marisa_trie
from multiprocess import find_crosswords_multiprocessing
from file_utils import read_file_into_list


def filter_fixed_length_words(word_list: List[str], word_length=5):
    return [word for word in word_list if len(word) == word_length]


def main():
    crossword_size = 5
    word_list = filter_fixed_length_words(read_file_into_list("word-lists/wordle/wordle-words.txt"), crossword_size)
    # word_list.sort()
    # random.shuffle(word_list)
    word_list = word_list[:3000]

    trie = marisa_trie.Trie(word_list)
    # print(trie.keys(""))
    print(f"number of words = {len(word_list)}")

    find_crosswords_multiprocessing(crossword_size, trie, word_list, number_of_processes=16, max_words=16)


if __name__ == "__main__":
    main()
