def merge_the_tools(string, k):
    result = []
    for i in range(0, len(string), k):
        sub_string = string[i:i+k]
        unique = ""
        for char in sub_string:
            if char not in unique:
                unique += char
        result.append(unique)
    return result
