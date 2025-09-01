def josephus(n, k):
    if n == 1:
        return 1
    return (josephus(n - 1, k) + k - 1) % n + 1

if __name__ == "__main__":
    n = 7
    k = 3
    print("The safe position is", josephus(n, k))
