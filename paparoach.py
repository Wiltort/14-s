def run():
    with open('input.txt') as input:
        n = int(input.readline())
        m = int(input.readline())
        P = [int(a) for a in input.readline().split()]
        Q = [int(a) for a in input.readline().split()]
    result = []
    T = set(Q)
    print(T)
    result = [a for a in P if a in T or (T.add(a) or False)]
    return result


if __name__=="__main__":
    print(*run())