from util import count_words

if __name__ == '__main__':
    n = int(input())
    words = [input() for _ in range(n)]

    unique_count, counts = count_words(words)
    print(unique_count)
    print(' '.join(map(str, counts)))
