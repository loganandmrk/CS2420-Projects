lyst1 = [1,2,3,4,5,6]
lyst2 = [2,6,3,2,3,8,7]
lyst3 = [8,7,6,5,4,3,3]


def is_sorted(lyst):
    
    if (isinstance(lyst, list) and all(isinstance(i, int) for i in lyst)):
        if all(lyst[i] <= lyst[i + 1] for i in range(len(lyst) - 1)):
            return True
        else:
            return False
    else:
        raise TypeError("Data must be a list containing only integers.")
    
def quicksort(lyst):
    num_swap = 0
    num_comp = 0

    if len(lyst) <= 1:
        return lyst, num_comp, num_swap
    else:
        pivot = lyst[len(lyst) // 2]
        left = []
        equal = []
        right = []

        for i in lyst:
            num_comp += 1           # one comparison to pivot per item
            if i < pivot:
                left.append(i)
                num_swap += 1      # count the move/append
            elif i == pivot:
                equal.append(i)
                num_swap += 1
            else:
                right.append(i)
                num_swap += 1

        sorted_left, comp_left, swap_left = quicksort(left)
        sorted_right, comp_right, swap_right = quicksort(right)

        num_comp += comp_left + comp_right
        num_swap += swap_left + swap_right   # do NOT add len(equal) again

        return list(sorted_left + equal + sorted_right), num_comp, num_swap

def selection_sort(lyst):
    num_comp = 0
    num_swap = 0

    for i in range(len(lyst)):
        curr_min = i
        for j in range(i + 1, len(lyst)):
            num_comp += 1
            if lyst[j] < lyst[curr_min]:
                curr_min = j
        
        num_swap += 1
        lyst[i], lyst[curr_min] = lyst[curr_min], lyst[i]
    
    return lyst, num_comp, num_swap

def insertion_sort(lyst):
    num_swap = 0
    num_comp = 0

    for i in range(1, len(lyst)):
        j = i
        while j > 0:
            num_comp += 1
            if lyst[j] < lyst[j - 1]:
                num_swap += 1
                lyst[j], lyst[j - 1] = lyst[j - 1], lyst[j]
                j -= 1
            else:
                break

    return lyst, num_comp, num_swap

def merge(left, right):
    result = []
    i = 0
    j = 0
    num_comp = 0
    num_swap = 0

    while i < len(left) and j < len(right):
        num_comp += 1
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
            num_swap += 1
        else:
            result.append(right[j])
            j += 1
            num_swap += 1

    while i < len(left):
        result.append(left[i])
        i += 1
        num_swap += 1

    while j < len(right):
        result.append(right[j])
        j += 1
        num_swap += 1

    return result, num_comp, num_swap

def mergesort(lyst):
    if len(lyst) <= 1:
        return lyst, 0, 0

    mid = len(lyst) // 2
    lefthalf = lyst[:mid]
    righthalf = lyst[mid:]

    sorted_left, comp_left, swap_left = mergesort(lefthalf)
    sorted_right, comp_right, swap_right = mergesort(righthalf)

    merged, comp_merge, swap_merge = merge(sorted_left, sorted_right)

    total_comp = comp_left + comp_right + comp_merge
    total_swap = swap_left + swap_right + swap_merge

    return merged, total_comp, total_swap

def main():
    #print(quicksort(lyst2))
    #print(selection_sort(lyst2))
    #print(insertion_sort(lyst3))
    print(mergesort(lyst2))

if __name__ == "__main__":
    main()