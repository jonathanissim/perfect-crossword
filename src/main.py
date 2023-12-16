import marisa_trie


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
        print(f"An error occurred: {e}")

    return word_list


def main():
    word_list = read_file_into_list("../words.txt")
    trie = marisa_trie.Trie(word_list)
    print(trie.keys("ab"))


if __name__ == "__main__":
    main()
