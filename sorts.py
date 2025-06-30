def binary_search(seq, item):
    '''sorted seq, item to find.
       start at mid point, is item higher/lower
       O(logN)
    '''
    begin_idx = 0
    end_idx = len(seq) - 1

    while begin_idx <= end_idx:
        midpoint = begin_idx + (end_idx - begin_idx) // 2    
        midpoint_val = seq[midpoint]

        if midpoint_val == item:
            return midpoint
        elif item < midpoint_val:
            end_idx = midpoint - 1
        else:
            begin_idx = midpoint + 1

    return

print(binary_search([1, 2, 3, 4, 5], 5))


def merge_sort(seq):
    '''divide and conquer with 2 functions
       split in half, sort recursively, then merge halfs
       O(n * log(n))
    '''
    seq_len = len(seq)

    if seq_len <= 1:
        return seq

    midpoint = seq_len // 2    
    left_arr = merge_sort(seq[:midpoint])
    right_arr = merge_sort(seq[midpoint:])

    return merge(left_arr, right_arr)
        

def merge(left_arr, right_arr):
    '''func #2 of merge_sort'''
    result = list()      
    left_idx = 0
    right_idx = 0

    while left_idx < len(left_arr) and right_idx < len(right_arr):
        if left_arr[left_idx] < right_arr[right_idx]:
            result.append(left_arr[left_idx])
            left_idx += 1
        else:
            result.append(right_arr[right_idx])
            right_idx += 1
        
    result.extend(left_arr[left_idx:])
    result.extend(right_arr[right_idx:])

    return result


seq = [1, 8, 33, 2, 4, 22, 3]
print(merge_sort(seq))


def selection_sort(seq):
    '''find min value
       assign left as min value, this becomes sorted list, rest unsorted.
       find min value of unsorted list, add min to the the sorted list    
       O(n^2)
    '''
    len_seq = len(seq)
    idx_len = range(len_seq-1)

    for i in idx_len:
        min_val = i

        for j in range(i+1, len_seq):
            if seq[j] < seq[min_val]:
                min_val = j
        
        if min_val != i:
            seq[min_val], seq[i] = seq[i], seq[min_val]

    return seq

seq = [1, 8, 3, 2, 1, 2, 3]
print(selection_sort(seq))


def insert_sort(seq):
    '''1st item becomes sorted list, rest unsorted list
       take 1st item from unsorted list add to sorted list and compare items, 
       swap if necessary
       O(n^2)
    '''
    for i in range(1, len(seq)):
        value_to_sort = seq[i]

        while seq[i-1] > value_to_sort and i > 0:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i -= 1

    return seq

seq = [8, 3, 2, 1, 2, 3]
print(insert_sort(seq))


def bubble_sort(seq):
    '''sort 1st 2 items, sort 2 at a time.
       O(n²)'''
    sorted = False

    while not sorted:
        sorted = True

        for i in range(len(seq) - 1):
            if seq[i] > seq[i+1]:
                sorted = False
                seq[i], seq[i+1] = seq[i+1], seq[i]
    
    return seq


seq = [8, 3, 5, 10, 7, 1]
print(bubble_sort(seq)) 


def quick_sort(seq):
    '''low items, pivot, high items
       O(n*logn)
    '''
    if len(seq) <= 1:
        return seq
    
    pivot = seq.pop()
    lower_items = list()
    higher_items = list()

    for item in seq:
        if item < pivot:
            lower_items.append(item)
        else:
            higher_items.append(item)

    return quick_sort(lower_items) + [pivot] + quick_sort(higher_items)

  
seq = [4, 5, 1, 2, 33, 6, 4, 1]
print(quick_sort(seq))
