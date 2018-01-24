def get_permutations(string):
    if len(string) <= 1:
        return set([string])

    all_chars_except_last = string[:-1]
    last_char = string[-1]

    # recursive call: get all possible permutations for all chars except last
    permutations_of_all_chars_except_last = get_permutations(all_chars_except_last)

    # put the last char in all possible positions for each of
    # the above permutations
    permutations = set()
    for each_string in permutations_of_all_chars_except_last:
        for position in range(len(all_chars_except_last) + 1):
            permutation = each_string[
                          :position] + last_char + each_string[position:]
            permutations.add(permutation)

    return permutations


print get_permutations("uday")
