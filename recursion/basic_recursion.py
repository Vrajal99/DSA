# recursion


# def p_name(name,n,itr):
#     if itr>n-1: return
    
#     print(name)
#     itr+=1
#     p_name(name,n,itr)

# if __name__=="__main__":
#     your_name=input("Enter your name: ")
#     cnt=int(input("Enter how many times you want to print: "))
    
#     current_ctr=0

#     p_name(your_name,cnt,current_ctr)

########################## Approach 2 #####################

def name_print_n_times(your_name, n):
    if n==0: return

    print(your_name)
    name_print_n_times(your_name, n-1)

def print_1_to_n_recur(i,n):
    if i>n:
        return
    print(i)
    print_1_to_n_recur(i+1,n)

def print_n_to_1_recur(i,n):
    if i==0:
        return
    print(i)
    print_n_to_1_recur(i-1,n)

def print_1_to_n_backtrack(i,n):
    if i<1:
        return
    print_1_to_n_backtrack(i-1,n) 
    print(i)    # Note the ORDER OF print here after the recurssion call

def print_n_to_1_backtrack(i,n): 
    
    if i>n: # the loop starts from 1 and ends aat i>n
        return
    print_n_to_1_backtrack(i+1,n)
    print(i)    # Note the ORDER OF print here after the recurssion call

def sum_of_n(n,sum):
    if n<1:
        print(sum)
        return
    sum_of_n(n-1,sum+n)

def sum_of_n_functional(n):
    if n==0:return 0    #if n=0 then sum of 0 numbers in 0
    return n + sum_of_n_functional(n-1)

def factorial(n):
    if n==0: return 1

    return n*factorial(n-1)

def reverse_an_array_recursion(i,n,arr):

    if i>=n/2: return
    arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
    reverse_an_array_recursion(i+1,n,arr)

def reverse_of_array_2ptr(start,end,arr):

    if start>end:return
    arr[start],arr[end]=arr[end],arr[start]
    reverse_of_array_2ptr(start+1,end-1,arr)

def check_palindrome(s,i):

    if i>=len(s)/2:return True # Base Case if i crosses the middle element of the string then all left and right elements are equal and hence Palindrome
    if s[i]!=s[len(s)-i-1]:return False # If 1st and last element are not same then it's not a Palindrome
    return check_palindrome(s,i+1) # else keep cheking successive elements

def fibonacci(n):
    if n<=1:
        return n
    
    last=fibonacci(n-1) # successive fibonacci number is sum last and the second last number
    second_last=fibonacci(n-2) # NOTICE more than 1 recurssive call being made
    return last + second_last
    # return fibonacci(n-1) + fibonacci(n-2)
    
if __name__=="__main__":
    # your_name=input("Input You name: ")
    # print_count=int(input("Enter No. of times to print using Recurrsion: "))

    # # Print a text n times using recursion    
    # name_print_n_times(your_name, print_count)

    # # Print a from 1 to n using recursion
    # print_1_to_n_recur(1,5)

    # # Print a from n to 1 using recursion
    # print_n_to_1_recur(5,5)

    # # Print a from 1 to n using recursion
    # print_1_to_n_backtrack(5,5) # Note! That the arguements passed is changed. 
    
    # # Print a from n to 1 using recursion
    # print_n_to_1_backtrack(1,5) # Note! That the arguements passed is changed.
    
    # # Print sum of n numbers using parameters, here n=10, initial sum = 0
    # n=10
    # sum_of_n(n,0)
    # print(f"Sum of 1 to {n} numbers, using parameterised way, where a function prints on exit.")

    # # Print sum of n numbers using parameters, here n=10
    # n=10
    # print(f"Sum of 1 to {n} numbers is {sum_of_n_functional(n)}, using funcional way, where a function returns.")

    # # Print factoial of n
    # n=5
    # print(f"Factorial of {n} is {factorial(n)}")

    # Print reverse of an array
    arr=[1,2,3,4,5,6]
    reverse_an_array_recursion(0,len(arr),arr)
    print(f"Reverse  is {arr}")
    
    reverse_of_array_2ptr(0,len(arr)-1,arr)
    print(f"Reverse  is {arr}")

    #Check if the following string is palindrome
    n=7
    print(fibonacci(n)) # 0 based indexing
