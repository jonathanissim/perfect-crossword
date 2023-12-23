from squarecrossword import SquareCrossword


class Algorithm:
    def __init__(self, trie, crossword_size, crossword=None):
        if crossword is None:
            self.crossword = SquareCrossword(crossword_size)
        else:
            self.crossword = crossword
        self.trie = trie
        self.crossword_size = crossword_size

    def find_crosswords(self):
        crossword = SquareCrossword(self.crossword.size)
        crossword_word_indexes = [0] * self.crossword.size * 2

        while True:
            # crossword.print_crossword()
            potential_words = self.trie.keys(crossword.get_next_prefix())  # Note this also calculated in is_legal
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
            if not crossword.is_legal(self.trie):
                # print(f"crossword isn't legal")
                crossword.remove_word()
                continue
            if crossword.get_build_stage() == (self.crossword.size * 2):
                crossword.print_crossword()
                crossword.remove_word()
                # return crossword
