from util import can_stack

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        blocks = list(map(int, input().split()))
        result = can_stack(blocks)
        print(result)
