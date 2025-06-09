from util import merge_the_tools
if __name__ == '__main__':
    string = input("Enter the string: ")
    k = int(input("Enter the segment length: "))
    result = merge_the_tools(string, k)
    for segment in result:
        print(segment)
