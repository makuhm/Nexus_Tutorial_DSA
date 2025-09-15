if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sorted = sorted(list(set(arr)))
    print(sorted[-2])
