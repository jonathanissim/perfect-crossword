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


def write_crosswords_to_file(list_of_word_lists, file_path):
    with open(file_path, 'w') as file:
        for word_list in list_of_word_lists:
            line = ','.join(word_list)
            file.write(f"{line}\n")


# Remove duplications
    # with open("crosswords/wordle-crosswords.txt", "r") as file:
    #     lines = file.readlines()
    #     lines.sort()
    #     lines2 = [list(lines[i].split()) for i in range(len(lines))]
    #     lines3 = [lines2[i] for i in range(0, len(lines2), 2)]
    #     for line in lines3:
    #         print(line)
    #     with open("crosswords/wordle-crosswords2", "w") as file2:
    #         for line in lines3:
    #             file2.write(f"{line[0]}\n")