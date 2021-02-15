import csv

a = []
with open("QuickSort.txt") as file:
    arr = csv.reader(file)
    for i in arr:
        a.extend(i)

for i in range(len(a)):
    a[i] = int(a[i])

########## data parsed and stored ############
m = 0

def choosePivot(A, l, r):
    return l

## partition using first element as pivot
def partition1(A, l, r):
    #global m
    #m = m + (r-l+1) -1
    x = A[l]
    i = l+1
    for j in range(l+1, r+1):
        if A[j] < x:
            A[j], A[i] = A[i], A[j]
            i = i+1
    A[l], A[i-1] = A[i-1], A[l]
    return A, i-1

### partition using the last element as pivot
def partition2(A, l, r):
    global m
    m = m + (r-l+1) -1
##    x = A[r]
##    i = l
##    for j in range(l, r-1):
##        if A[j] < x:
##            i = i+1
##            A[j], A[i] = A[i], A[j]
##    A[r], A[i+1] = A[i+1], A[r]
##    return A, i+1
    ### swap last element with the first one and called partition1
    A[l], A[r] = A[r], A[l]
    return partition1(A, l, r)

def partition3(A, l, r):
    global m
    m = m + (r-l+1) -1
    #print("A: ", A[l:r+1])
    first = A[l]
    #print("first: ", first)
    last = A[r]
    #print("last: ", last)
    middle = A[l + (r-l)//2]
    #print("middle: ", middle)
    maxim = first + last + middle - max(first, last, middle) - min(first, last, middle)
    #print("Median found: ", maxim, "\n")
    if maxim == first:
        median = l
    elif maxim == last:
        median = r
    else:
        median = l + (r-l)//2
    # swap first element with median and call partition1
    A[l], A[median] = A[median], A[l]
    return partition1(A, l, r)
        

def quick_sort(A, l, n):
    if n<=l:
        return A
    ## partition1, by first element
    ## if using this one, remove the commented portion
    ## in function definition
    #A, p = partition1(A, l, n)

    ## partition2, by last element
    #A, p = partition2(A, l, n)

    ## partition3, using median of 3
    A, p = partition3(A, l, n)

    #print("partition done, A: ", A, " partition index: ", p)

    A = quick_sort(A, l, p-1)
    #print("First Half sorted")
    A = quick_sort(A, p+1, n)
    #print("Second Half Sorted")
    return A

#a = [3, 2, 1, 4, 5]
#a = quick_sort(a, 0, 4)
# answers: 6 10 6

#a = [4, 3, 2, 5, 1]
#a = quick_sort(a, 0, 4)
# answers: 7 8 6

#a = [2, 20, 1, 15, 3, 11, 13, 6, 16, 10, 19, 5, 4, 9, 8, 14, 18, 17, 7, 12]
#a = quick_sort(a, 0, 19)

#a = [3, 2, 10, 6, 7, 1, 9, 5, 4, 8]
#a = quick_sort(a, 0, 9)
# Answers: 21 22 20
#print(a)

a = quick_sort(a, 0, len(a)-1)
###162085
###164123
###138382
print(m)
