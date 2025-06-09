from util import print_formatted

if __name__ == "_main_":
    n = int(input("Enter a number: "))
    formatted_output = print_formatted(n)
    for line in formatted_output:
        print(line)