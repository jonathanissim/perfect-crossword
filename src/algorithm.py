from squarecrossword import SquareCrossword
import os, psutil


class Algorithm:
    def __init__(self, trie, crossword_size, crossword=None):
        if crossword is None:
            self.crossword = SquareCrossword(crossword_size)
        else:
            self.crossword = crossword
        self.trie = trie
        self.crossword_size = crossword_size

    def find_crosswords(self):
        number_of_crosswords = 0
        word_list_length = len(self.trie.keys(""))
        crossword = SquareCrossword(self.crossword.size)
        crossword_word_indexes = [0] * self.crossword.size * 2

        while True:
            potential_words = self.trie.keys(crossword.get_next_prefix())
            print(f"prefix = {crossword.get_next_prefix()}")
            current_position_try_number = crossword_word_indexes[crossword.get_build_stage()]
            if current_position_try_number >= len(potential_words):
                crossword_word_indexes[crossword.get_build_stage()] = 0
                crossword.remove_word()
                continue
            crossword_word_indexes[crossword.get_build_stage()] += 1

            # Debugging
            if crossword.get_build_stage() == 1 and current_position_try_number % 100 == 0:
                print(f"try {current_position_try_number}")
                print(f"word = {potential_words[current_position_try_number]}")
            if crossword.get_build_stage() == 1 and current_position_try_number == word_list_length - 1:
                print(f"done. found {number_of_crosswords} crosswords")
                return

            potential_word = potential_words[current_position_try_number]
            if potential_word in crossword.get_words_set():
                continue
            crossword.place_word(potential_word)
            print(f"placing {potential_word}")
            crossword.print_crossword()
            if not crossword.is_legal(self.trie):
                # print(f"crossword isn't legal")
                crossword.remove_word()
                continue
            if crossword.get_build_stage() == (self.crossword.size * 2):
                number_of_crosswords += 1
                crossword.print_crossword()
                return crossword
                crossword.remove_word()
