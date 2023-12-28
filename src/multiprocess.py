from multiprocessing import Pool, Manager, Lock
from algorithm import Algorithm

manager = Manager()
number_of_crosswords = manager.Value(int, 0)
number_of_tried_words = manager.Value(int, 0)
shared_list = manager.list()


def find_crosswords_multiprocessing(crossword_size, trie, word_list, number_of_processes=256, max_words=10000):
    alg = Algorithm(trie, crossword_size)
    number_of_words_to_try = min(len(word_list), max_words)
    lock = Lock()
    with Pool(initializer=initialize_lock, initargs=(lock,)) as pool:
        words_per_process = _get_words_per_process(number_of_words_to_try, number_of_processes)
        print(words_per_process)
        pool.starmap(alg.find_crosswords,
                     [(words_per_process[i], (number_of_words_to_try // number_of_processes) * i) for i in
                      range(len(words_per_process))])
    print(shared_list)
    return shared_list



def initialize_lock(lock):
    global g_lock
    g_lock = lock


def _get_words_per_process(number_of_words, number_of_processes):
    result = [number_of_words // number_of_processes] * number_of_processes
    if number_of_words % number_of_processes != 0:
        result[-1] += number_of_words % number_of_processes
    return result


