#! /usr/binenv python

def bubble_sort(L):
    for i in range(len(L) - 1):
        for j in range(len(L) - 1 - i):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]

def main():
    l = [54,26,93,17,77,31,44,55,20]
    print(bubble_sort())
    
if __name__ == '__main__':
    main()
