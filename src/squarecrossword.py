from tabulate import tabulate
from simple_colors import *


class SquareCrossword:
    def __init__(self, size, across_words=None, down_words=None):
        if across_words is None:
            self.across_words = []
            self.down_words = []
            self.build_stage = 0
            self.size = size
        else:
            self.across_words = across_words
            self.down_words = down_words
            self.size = size
            self.build_stage = size * 2
        self.words_set = set(self.across_words + self.down_words)

    def get_words(self):
        return self.across_words + self.down_words

    def get_build_stage(self):
        return self.build_stage

    def get_words_set(self):
        return self.words_set

    def is_legal(self, trie):
        if self.build_stage <= 2:
            return True
        return self._is_legal_across(trie) and self._is_legal_down(trie)

    def _is_legal_down(self, trie):
        prefix_length = (self.build_stage + 1) // 2
        number_of_completed_down_words = self.build_stage // 2

        # print(f"in  number_of_completed_down_words stage = {number_of_completed_down_words}")
        # print(f"in  build stage = {self.build_stage}")
        # print(f"in  across words = {self.across_words}")
        # print(f"in  down words = {self.down_words}")

        for i in range(number_of_completed_down_words, self.size):
            prefix = ''.join([self.across_words[j][i] for j in range(prefix_length)])
            if next(trie.iterkeys(prefix), None) is None:
                # print(f"legal across failed on prefix {prefix}")
                return False
        return True

    def _is_legal_across(self, trie):
        prefix_length = self.build_stage // 2
        number_of_completed_across_words = (self.build_stage + 1) // 2

        # print(f"in  number_of_completed_across_words = {number_of_completed_across_words}")
        # print(f"in  build stage = {self.build_stage}")
        # print(f"in  across words = {self.across_words}")
        # print(f"in  down words = {self.down_words}")

        for i in range(number_of_completed_across_words, self.size):
            prefix = ''.join([self.down_words[j][i] for j in range(prefix_length)])
            if self._is_legal_prefix(prefix, trie):
                # print(f"legal down failed on prefix {prefix}")
                return False
        return True

    # @staticmethod
    # def _is_legal_prefix(prefix, trie):
    #     return len(trie.keys(prefix)) == 0
    @staticmethod
    def _is_legal_prefix(prefix, trie):
        return next(trie.iterkeys(prefix), None) is None

    # @staticmethod
    # def _is_legal_prefix(prefix, trie):
    #     return trie.has_keys_with_prefix(prefix)

    def place_word(self, word):
        # print(f"placing word: {word}")
        if self.build_stage % 2 == 0:
            self.across_words.append(word)
        else:
            self.down_words.append(word)
        self.words_set.add(word)
        self.build_stage += 1

    def remove_word(self):
        if self.build_stage % 2 == 1:
            word = self.across_words.pop()
        else:
            word = self.down_words.pop()
        self.words_set.remove(word)
        self.build_stage -= 1

    def get_next_prefix(self):
        if self.build_stage == 0:
            return ""
        if self.build_stage % 2 == 0:
            return self._get_next_across_prefix()
        else:
            return self._get_next_down_prefix()

    def _get_next_across_prefix(self):
        prefix_length = self.build_stage // 2
        number_of_completed_across_words = self.build_stage // 2
        return ''.join([self.down_words[i][number_of_completed_across_words] for i in range(prefix_length)])

    def _get_next_down_prefix(self):
        prefix_length = (self.build_stage + 1) // 2
        number_of_completed_down_words = (self.build_stage - 1) // 2
        return ''.join([self.across_words[i][number_of_completed_down_words] for i in range(prefix_length)])

    def print_crossword(self):
        print(cyan(tabulate(self.across_words), 'bright'))
        # print(cyan(tabulate(self.down_words), 'bright'))
