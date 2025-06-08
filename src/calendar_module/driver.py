from util import find_day

if __name__ == "__main__":
    month, day, year = map(int, input("Enter date (MM DD YYYY): ").split())
    result = find_day(month, day, year)
    print(result)
