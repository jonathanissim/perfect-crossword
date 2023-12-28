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
            # print(f"prefix = {crossword.get_next_prefix()}")
            current_position_try_number = crossword_word_indexes[self.crossword.get_build_stage()]

            # Debugging
            if self.crossword.get_build_stage() == 0:  # and current_position_try_number % 100 == 0:
                if crossword_word_indexes[0] == words_to_try + start_index:
                    return
                with multiprocess.g_lock:
                    multiprocess.shared_list[0] += 1
                    tries = multiprocess.shared_list[0]
                print(f"try {tries} = {potential_words[current_position_try_number]}")

            if current_position_try_number >= len(potential_words):
                crossword_word_indexes[self.crossword.get_build_stage()] = 0
                self.crossword.remove_word()
                continue

            potential_word = potential_words[current_position_try_number]
            if potential_word in self.crossword.get_words_set():
                continue
            self.crossword.place_word(potential_word)
            crossword_word_indexes[self.crossword.get_build_stage()] += 1
            # print(f"placing {potential_word}")
            # crossword.print_crossword()

            if not self.crossword.is_legal(self.trie):
                self.crossword.remove_word()
                continue
            if self.crossword.get_build_stage() == (self.crossword.size * 2):
                with multiprocess.g_lock:
                    multiprocess.shared_list[1] += 1
                    number_of_crosswords = multiprocess.shared_list[1]
                print(f"Found {number_of_crosswords} crosswords")
                self.crossword.print_crossword()
                self.crossword.remove_word()
    
    def _place_potential_word(self):
        pass