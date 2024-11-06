#
# Author: Hanbi Gong
# Student Number: 111932224
#
# Place the code for your lab 3 here.  Read the specs carefully.  
#
# To test, run the following command :
#     python test_lab3.py
#

def factorial(number):
	if number == 0:
		total = 1
	else:
		total = number * factorial(number - 1)

	
	return total

def linear_search(lst, key):
    def search(i):
        if i == len(lst):
            return -1
        elif lst[i] == key:
            return i
        return search(i + 1)
    
    return search(0)


def binary_search(lst, key, left=0, right=None):
    if right is None:
        right = len(lst) - 1      
    if left > right:  
        return -1
    
    mid = (left + right) 
    
    if lst[mid] == key:  
        return mid
    elif lst[mid] > key: 
        return binary_search(lst, key, left, mid - 1)
    else: 
        return binary_search(lst, key, mid + 1, right)
