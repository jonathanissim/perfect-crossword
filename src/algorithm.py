from squarecrossword import SquareCrossword
import multiprocess


class Algorithm:
    def __init__(self, trie, crossword_size, crossword=None):
        self.trie = trie
        self.crossword_size = crossword_size
        if crossword is None:
            self.crossword = SquareCrossword(crossword_size)
        else:
            self.crossword = crossword

    def find_crosswords(self, words_to_try, start_index=0):
        crossword_word_indexes = [0] * self.crossword.size * 2
        crossword_word_indexes[0] = start_index

        while True:
            potential_words = self.trie.keys(self.crossword.get_next_prefix())
            current_position_try_number = crossword_word_indexes[self.crossword.get_build_stage()]

            if self._finished_all_words(crossword_word_indexes, start_index, words_to_try):
                return

            if current_position_try_number >= len(potential_words):
                crossword_word_indexes[self.crossword.get_build_stage()] = 0
                self.crossword.remove_word()
                continue

            potential_word = potential_words[current_position_try_number]
            crossword_word_indexes[self.crossword.get_build_stage()] += 1

            self._debug_prints(potential_word)

            if potential_word in self.crossword.get_words_set():
                continue

            self.crossword.place_word(potential_word)
            # print(f"placing {potential_word}")
            # self.crossword.print_crossword()

            if not self.crossword.is_legal(self.trie):
                self.crossword.remove_word()
                continue

            if self.crossword.get_build_stage() == self.crossword.size * 2:
                self._found_complete_crossword()

    def _finished_all_words(self, crossword_word_indexes, start_index, words_to_try):
        return self.crossword.get_build_stage() == 0 and crossword_word_indexes[0] == words_to_try + start_index

    def _debug_prints(self, potential_word):
        if self.crossword.get_build_stage() == 0:  # and current_position_try_number % 100 == 0:
            with multiprocess.g_lock:
                multiprocess.number_of_tried_words.value += 1
                tries = multiprocess.number_of_tried_words.value
            print(f"try {tries} = {potential_word}")

    def _found_complete_crossword(self):
        with multiprocess.g_lock:
            multiprocess.number_of_crosswords.value += 1
            number_of_crosswords = multiprocess.number_of_crosswords.value
            multiprocess.shared_list.append(self.crossword.get_words())
        print(f"Found {number_of_crosswords} crosswords")
        self.crossword.print_crossword()
        self.crossword.remove_word()
