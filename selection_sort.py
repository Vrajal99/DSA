# Type: Python Source Code
# Description: Python program to implement Selection Sort algorithm
# Time Complexity: O(n^2), Best Case: O(n^2), Worst Case: O(n^2)
# Space Complexity: O(1)
# Uses: Selection Sort is used to sort the elements in an array in ascending order
#       It is an in-place comparison-based sorting algorithm for small input sizes
#       It is not suitable for large input sizes as its average and worst case complexities are of Ο(n2), where n is the number of items.


arr=input("Enter the array elements separated by space: ").split()
arr=[int(i) for i in arr]
# Convert the input string array to integer array for sorting purpose using list comprehension
# List comprehension syntax: [expression for item in list]
# The above list comprehension is equivalent to the below for loop
# for i in arr: arr.append(int(i)) 

def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        curr_max_pos=n-i-1
        max_ele_index= get_max(arr,curr_max_pos) # get the index of the maximum element in the array
        swap(arr,max_ele_index,curr_max_pos) # swap the maximum element with the current end position
    return arr

def get_max(arr,max_pos):
    max_idx=0
    for i in range(max_pos+1):    
        if arr[i]>arr[max_idx]:
            max_idx=i
    return max_idx # return the index of the maximum element in the array

def swap(arr,max_ele_index,curr_end_pos):
    arr[max_ele_index],arr[curr_end_pos]=arr[curr_end_pos],arr[max_ele_index]

print(selection_sort(arr)) # Output: [1, 2, 3, 4, 5]