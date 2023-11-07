def quicksort(array):
    if len (array) < 2:
        return array # базовый случай: массивы с 0 и 1 элементом уже отсортированы
    else:
        less = [i for i in array[1:] if i <= array[0]] #подмассив всех элементов, меньших опорного
        greater = [i for i in array[1:] if i > array[0]] #подмассив всех элементов, больших опорного
        return quicksort(less) + [array[0],] + quicksort(greater) 

def sort():
    with open('input.txt') as input:
        n = int(input.readline())
        P = [int(a) for a in input.readline().split()]
    
    return quicksort(P)


if __name__=="__main__":
    print(sort())