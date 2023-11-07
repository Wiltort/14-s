def buble_sort():
    with open('input.txt') as input:
        n = int(input.readline())
        P = [int(a) for a in input.readline().split()]
    
    for j in range (n):
        Exit = True
        for i in range (n-1):
            if P[i]>P[i+1]:
                Exit = False
                temp = P[i+1]
                P[i+1] = P[i]
                P[i] = temp
        if Exit:
            return P


if __name__=="__main__":
    print(*buble_sort())