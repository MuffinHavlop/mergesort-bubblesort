#bubble sort
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j - 1] > arr[i]:
                arr[j - 1], arr[i] = arr[i], arr[j - 1]
    return arr

#merge sort
def merge(nums1, nums2):

    #declear a blank list to merge the 2 lists
    merged = []

    #indicies for lists, i for nums1, j for nums2
    i, j = 0, 0
    #begin of the loop, sorting numbers

    while i < len(nums1) and j < len(nums2):

        #sorting progress
        if nums2[j] < nums1[i]:
            merged.append(nums2[j])
            j += 1

        #sorting progress
        else:
            merged.append(nums1[i])
            i += 1

    #return the merged list, needed the last element because after sorting, one list will be exhausted but the other list will still have the largest element in it, so we'll just get both the list into here
    return merged + nums1[i:] + nums2[j:]

def merge_sort(arr):
    #checking if the length of the array is larger than 1, if yes, continue the function, if no, return the arr
    if len(arr) <= 1:
        return arr
    
    #find the mid point of the array
    mid = len(arr) // 2

    #split the array in to 2 parts, left and right
    left = arr[:mid]
    right = arr[mid:]

    #using recursion to sort the left and right side
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)
    #the recursion and merge_sort function will be repeated many times untill the length of a list (left, right, arr) equals to 1

    #merge the sorted list with the merge function written ealier
    sorted_list = merge(left_sorted, right_sorted)

    #return the list
    return sorted_list


arr = [-243, -12, -12, 0, 1, 1, 1, 2, 5, 6, 6, 7, 7, 12, 23]

print("merge sort:", merge_sort(arr))
print("bubble sort:", bubble_sort(arr))
