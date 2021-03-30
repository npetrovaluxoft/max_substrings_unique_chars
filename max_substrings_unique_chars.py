#!/usr/bin/python3


def split_on_max_substrings_unique_chars(string_to_split):
    """
    Splits a given string on maximum possible substrings in a way that each character is present in
    not more then one substring.
    :param string_to_split: A string to split.
    :return: Resulting list of strings.
    """
    str_len = len(string_to_split)

    if str_len == 0:
        return []

    if str_len == 1:
        return [string_to_split]

    #
    # Collect unique characters into a set.
    #
    unique_chars = {ch for ch in string_to_split}

    #
    # For each unique character, discover its last position
    # in a given string and put it into a dictionary
    # where the key is a character and stored value is
    # its last position.
    #
    last_positions = {ch: string_to_split.rindex(ch) for ch in unique_chars}

    substrings = []       # Resulting substrings.
    start_idx = 0       # Start index of a current substring.
    substr_end_idx = 0  # End index of a current substring.

    for i, ch in enumerate(string_to_split):
        pos = last_positions[ch]
        if pos > substr_end_idx:
            substr_end_idx = pos

        if i == substr_end_idx:
            sub_str = string_to_split[start_idx:(i + 1)]
            start_idx = i + 1
            substrings += [sub_str]

    return substrings


#
# Entry point.
#
while True:
    string = input("Enter a string of characters (or press 'Enter' to exit): ")
    if len(string) == 0:
        exit()

    result = split_on_max_substrings_unique_chars(string)
    lengths = list(map(len, result))
    print("Lengths: " + str(lengths))
    print("Result:  " + str(result) if (len(result) > 1) else "could not split")
