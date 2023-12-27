import multiprocessing
from typing import List
from squarecrossword import SquareCrossword
from algorithm import Algorithm
import random

from tabulate import tabulate
import marisa_trie
from simple_colors import *
# import multiprocessing
from multiprocessing import Pool, Lock
from multiprocessing.managers import BaseManager

import os, psutil
from shared import init


# process = psutil.Process()


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


def get_words_per_process(number_of_words, number_of_processes):
    result = [number_of_words // number_of_processes] * number_of_processes
    if number_of_words % number_of_processes == 0:
        return result

    result[-1] += number_of_words % number_of_processes
    return result


# def target(iterable_item):
#     for item in items:
#         # Do cool stuff
#         if (... some condition here ...):
#             lock.acquire()
#             # Write to stdout or logfile, etc.
#             lock.release()


def main():
    crossword_size = 5
    # word_list = filter_fixed_length_words(read_file_into_list("../word-lists/words.txt"), crossword_size)
    # word_list = filter_fixed_length_words(read_file_into_list("../word-lists/third-million.txt"), crossword_size)
    word_list = filter_fixed_length_words(read_file_into_list("word-lists/wordle/wordle-words.txt"), crossword_size)

    # with open("../word-lists/third-million-fours.txt", 'a') as file:
    #     for word in word_list:
    #         file.write(f"{word}\n")
    # return
    # word_list.sort()
    random.shuffle(word_list)
    word_list = word_list[:3000]

    trie = marisa_trie.Trie(word_list)
    # print(trie.keys(""))
    print(f"number of words = {len(word_list)}")

    alg = Algorithm(trie, crossword_size)

    number_of_processes = 256
    number_of_words_to_try = len(word_list)
    l = multiprocessing.Lock()
    # print(words_to_try_per_process(number_of_words_to_try, number_of_processes))

    with Pool(initializer=init, initargs=(l,)) as pool:
        words_per_process = get_words_per_process(number_of_words_to_try, number_of_processes)
        print(words_per_process)
        pool.starmap(alg.find_crosswords,
                     [(words_per_process[i], (number_of_words_to_try // number_of_processes) * i) for i in
                      range(len(words_per_process))])


if __name__ == "__main__":
    main()
