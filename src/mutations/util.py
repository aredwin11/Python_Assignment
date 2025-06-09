def mutate_string(string, position, character):
    my_list = list(string)
    my_list[position] = character
    return ''.join(my_list)
