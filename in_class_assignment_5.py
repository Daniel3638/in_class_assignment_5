#Problem 1. Sort With Quicksort.
# Please build a function called "quicksort" that uses recursion to define the quicksort algorithm for a list of any length. 
# Build a main script that reads in the list provided, "numbers.txt", and runs it through your quicksort algorithm. 
# The main script should return the finished sorted list as "sorted.txt"
# All 3 files "In_class_assignment_5.py", "numbers.txt", and "sorted.txt" should all be added to your github repository and submitted as a github link.


'''Info on Quicksort Algorithm: 
The Quicksort algorithm is an efficient sorting algorithm developed by British computer scientist Tony Hoare in 1959.

Quicksort is a divide-and-conquer algorithm. Suppose you have a list of objects to sort. You start by choosing an item in the list, called the *pivot item*. 
This can be any item in the list. You then partition the list into two sublists based on the pivot item and recursively sort the sublists.

The steps of the algorithm are as follows:

1. Choose the pivot item.
2. Partition the list into two sublists:
        Those items that are less than the pivot item
        Those items that are greater than the pivot item
3. Quicksort the sublists recursively.
4. Each partitioning produces smaller sublists, so the algorithm is reductive. 

The base cases occur when the sublists are either empty or have one element, as these are inherently sorted. 
 '''


def quicksort(numbers_in_a_list, left, right):
    if(left < right):
        conquer = dividing(numbers_in_a_list, left,right)
        quicksort(numbers_in_a_list, left, conquer - 1)
        quicksort(numbers_in_a_list, conquer + 1, right)
        
def dividing(numbers_in_a_list,left,right):
    pivot = numbers_in_a_list[right]
    j = right - 1
    i = left 
    while(i < j):
        while i < right and numbers_in_a_list[i] < pivot:
            i += 1
        while j > left and numbers_in_a_list[j] >= pivot:
            j -= 1
        if(i < j):
            numbers_in_a_list[i], numbers_in_a_list[j] = numbers_in_a_list[j], numbers_in_a_list[i]
                 
                 
    if numbers_in_a_list[i] > pivot:
        numbers_in_a_list[i], numbers_in_a_list[right] = numbers_in_a_list[right], numbers_in_a_list[i]
        
    

    return i


def main():
    list1 = []
    filename = 'numbers.txt'
    with open(filename) as f:
        for line in f:
            list1 = [int(elt.strip().replace("[",'').replace(']','')) for elt in line.split(',')]
            
            
    quicksort(list1,0,len(list1) - 1)
    print(list1)
    
    outfile = open('Sorted.txt','w')
    
    outfile.write(str(list1))
    
    outfile.close()
if __name__ == "__main__":
    main()

#https://www.youtube.com/watch?v=9KBwdDEwal8 sourcing code 
