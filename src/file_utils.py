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


def write_list_to_file(list_of_word_lists, file_path):
    with open(file_path, 'w') as file:
        for word_list in list_of_word_lists:
            line = ','.join(word_list)
            file.write(f"{line}\n")
