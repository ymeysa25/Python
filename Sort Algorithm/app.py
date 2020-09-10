import time 
import random
import pandas as pd
import sys

# ============================ Sort Algorithm =============================

# =============================== Bubble Sort =============================
def bubble_sort(_arr): 
    # Make copy array, so doesn't change the real array
    _arr = arr.copy()

    # Get length array
    n = len(_arr) 

    # Traverse through all array elements
    for i in range(n-1): 

        # Compare element from index i with element afterward
        for j in range(0, n-i-1): 

            # Swap if the element found is greater 
            if _arr[j] > _arr[j+1] : 
                _arr[j], _arr[j+1] = _arr[j+1], _arr[j] 
    
    # return final array
    return _arr

# ==================================== End ================================

# =============================== Insertion Sort ==========================
def insertion_sort(arr):
    # Make copy array, so doesn't change the real array
    _arr = arr.copy()

    # list to collect all insertion prosess
    all_arr = []

    n = len(_arr) + 1

    # Traverse through all array elements
    for i in range(n):

        # Get length array that already selected
        m = len(_arr[0:i])

        if i+1 < n:
            # Append sorting process
            all_arr.append([_arr[0:i], _arr[i:n]])
            for j in range(m):
                # Swap if the element found is greater 
                if _arr[i] < _arr[j]:
                    _arr[i], _arr[j] = _arr[j], _arr[i]

    #  Append result array
    all_arr.append(_arr)
    return all_arr

# ==================================== End ================================

# =============================== Insertion Sort ==========================

def selection_sort(arr):
    all_arr = []
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        min_index = i
        all_arr.append(arr)
        for j in range(i+1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return all_arr

# ==================================== End ================================

# =============================== Insertion Sort ==========================  

""" 
    https://www.geeksforgeeks.org/python-program-for-quicksort/

    This function takes last element as pivot, places 
    the pivot element at its correct position in sorted 
    array, and places all smaller (smaller than pivot)
    to left of pivot and all greater elements to right 
    of pivot 
"""
def partition(arr,low,high): 
	i = ( low-1 )		 # index of smaller element 
	pivot = arr[high]	 # pivot 

	for j in range(low , high): 

		# If current element is smaller than or 
		# equal to pivot 
		if arr[j] <= pivot: 
		
			# increment index of smaller element 
			i = i+1
			arr[i],arr[j] = arr[j],arr[i] 

	arr[i+1],arr[high] = arr[high],arr[i+1] 
	return ( i+1 ) 

# ==================================== End ================================

# =============================== Insertion Sort ==========================

# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low --> Starting index, 
# high --> Ending index 

# Function to do Quick sort 
def quickSort(arr,low = 0, high = 0): 
    arr = arr.copy()
    if low < high: 

        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 

        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
    return arr

#Source https://www.geeksforgeeks.org/merge-sort/

# Python program for implementation of MergeSort 
def mergeSort(result): 
    if len(result) >1: 
        mid = len(result)//2 #Finding the mid of the array 
        L = result[:mid] # Dividing the array elements 
        R = result[mid:] # into 2 halves 

        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
        
        i = j = k = 0

        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                result[k] = L[i] 
                i+=1
            else: 
                result[k] = R[j] 
                j+=1
            k+=1
        
        # Checking if any element was left 
        while i < len(L): 
            result[k] = L[i] 
            i+=1
            k+=1
        
        while j < len(R): 
            result[k] = R[j] 
            j+=1
            k+=1
    return result
# ==================================== End ================================

# ================================== Get Time =============================

# The main function that Get time needed from Sorting process
# start --> Starting Time, 
# end --> Ending Tome 

def get_time(func, arr, qs = False):
    start = time.time()
    if qs:
        n = len(arr)
        result = func(arr, high = n-1)   
    else:
        result = func(arr)
    end = time.time()
    return end-start

# ==================================== End ================================
if __name__ == '__main__': 
    # print("Guide")
    print(
    """
    Guide
        1. Find the Shortest Time from each Sorting Algorithm
        2. Find result from each Sorting Algorithm
        3. Stop Program
    """)

    ALGORITHM = ["Buble Sort" , "Insertion Sort", "Selection Sort", "Quick Short", "Merge Sort"]
    
    while(True):
        sel = input("   Please input 1 or 2 : ")

        if sel == '1':
            total = 5000
            arr = [i for i in range(total)]
            unsort_arr = random.sample(arr, len(arr))   
            bs_time = get_time(bubble_sort, unsort_arr)
            is_time = get_time(insertion_sort, unsort_arr)
            ss_time = get_time(selection_sort, unsort_arr)
            qs_time = get_time(quickSort , unsort_arr, True)
            ms_time = get_time(mergeSort, unsort_arr)

            all_time = [bs_time, is_time, ss_time, qs_time, ms_time]
            df = pd.DataFrame(list(zip(ALGORITHM, all_time)), columns = ["Algorithm", "Time(s)"])

            print("\n     This is the time it takes each algorithm to sort", total, "numbers\n")
            print(df)
        
        elif sel == '2':
            # arr = sys.argv[1:]
            print("   Please input list of int element ex(1,2,3,4):", end = " ")
            arr = input()
            arr = [int(i) for i in arr.split(',')]

            n = len(arr)

            print("   ", ALGORITHM[0], " : ", bubble_sort(arr))
            print("   ", ALGORITHM[1], " : ", insertion_sort(arr)[-1])
            print("   ", ALGORITHM[2], " : ", selection_sort(arr)[-1])
            print("   ", ALGORITHM[3], " : ", quickSort(arr, high = n - 1))
            print("   ", ALGORITHM[4], " : ", mergeSort(arr))

        else:
            # state = False
            break

        tryagain = input("\n    Try Again (Y/N) : ")
        if tryagain.lower() == 'n':
            break
