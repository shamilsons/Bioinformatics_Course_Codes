from random import *
import time
import random

#Binary search algorithm
def binary_search(lst,elm):
    index=-1
    low = 0
    high = len(lst)
    while low <= high:
        mid = (low+high)//2
        if lst[mid]==elm:
            index=mid
            break
        elif lst[mid] > elm:
            high=mid-1
        else:
            low=mid+1
    return index

#Bubble sort algorithm
def bubble_sort(lst):
    check=False
    while not check:
        check=True
        temp_var=0
        for i in range(len(lst)-1):
            if(lst[i]>lst[i+1]):
                check=False
                temp_var=lst[i]
                lst[i]=lst[i+1]
                lst[i+1]=temp_var

#Insertion sort
def insertion_sort(lst):
    for index in range(1,len(lst)):
        value=lst[index]
        i=index-1
        while i>=0:
            if value<lst[i]:
                lst[i+1]=lst[i]
                lst[i]=value
                i=i-1
            else:
                break

def main():
    #Generate a list of random 10 numbers
    lst=[randint(0,100) for r in xrange(10000)]

    #Call bubble sorting algorithm to sort a list
    #print lst
    start_time = time.time()
    bubble_sort(lst)
    print '%.3f'%(time.time() - start_time), "seconds taken for bubble sorting"


    #Call insertion sorting algorithm to sort a list
    random.shuffle(lst)
    #print lst
    start_time = time.time()
    #insertion_sort(lst)
    lst.sort()
    print '%.3f'%(time.time() - start_time), "seconds taken for insertion sorting"

    #Call binary search algorithm to find an element
    schnum=input('Enter a number to search 0-99:')
    start_time = time.time()
    print binary_search(lst,schnum), "index"
    print '%.3f'%(time.time() - start_time), "seconds taken for binary search"

main()
