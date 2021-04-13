import random

### For Greedy Weight-Length Ratio
### use shouldSwap1() inside partition function
### For Greedy Weight/Length Ratio
### use shouldSwap2() inside partition function

def shouldSwap2(a, b):
    # weight/length ratio
    if a[0]/float(a[1]) > b[0]/float(b[1]):
        return 1
    else:
        return 0

def shouldSwap1(a, b):
    #print("Inside shouldSwap")
    #print("a: ", a, ", b: ", b)
    ## if a<b, return True
    ## else False

    ## for job scheduling :::greedy algo 1:::
    ## based on (weight - length) diff
    ## a[0] -> weight
    ## a[1] -> length
    ## if diff is same, return if [0] > b[0]
    if (a[0] - a[1]) > (b[0] - b[1]):
        #print("Returning True")
        return 1
    elif (a[0] - a[1]) < (b[0] - b[1]):
        #print("Returning False")
        return 0
    ## equal difference, check weights
    elif a[0] > b[0]:
        #print("Returning True")
        return 1
    #print("Returning False")
    return 0


def partition(a, p, q):
    '''
    #print("Inside partition: i=", p, ", j=", q)
    ## take random element as pivot
    #r = random.randint(p, q)
    #x = a[r]
    #print("Random element chosen:", x)
    #print("Last element: ", a[q])
    ## swap it with last element
    #a[r], a[q] = a[q], a[r]
    #print("Array: ", a)
    '''
    x = a[q]
    i = p-1
    ### j pointer se compare karte hai
    ### i pointer sorted array ko batata hai
    for j in range(p, q):
        ## if a[j] < x
        if shouldSwap2(a[j], x):
            i = i + 1
            a[j], a[i] = a[i], a[j]
    ### swap pivot with the partition point
    a[i+1], a[q] = a[q], a[i+1]
    return i+1


## array a[i....j], i and j both inclusive
def quick_sort(a, i, j):
    #print("\nInside Quick_sort:\ni: ", i, ", j: ", j)
    #print(a[i:j+1])
    if i<j:
        x = partition(a, i, j)
        #print("Inside quick_sort, partitioned around index: ", x)
        #print("After partition, array: ", a)
        quick_sort(a, i, x-1)
        quick_sort(a, x+1, j)
    

job = []
with open("jobs.txt", "r") as jobs:
    data = jobs.readlines()
    n = int(data.pop(0).strip())
    for line in data:
        w, l = line.split()
        job.append([int(w), int(l)])
    #print(job)
    quick_sort(job, 0, n-1)
    #print("After quick_sort: ", job)
    #print(n)
    s = 0
    c = 0
    for each in job:
        #print("\nJob: ", each)
        c = c + each[1]
        #print("Completion Time: ", c)
        s = s + each[0]*c
    print(s)
    
