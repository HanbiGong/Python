# Analysis and Reflection for Lab 3

## function 1:

Analyze the following function with respect to number

```python
def function1(value, number):
	if (number == 0):	#1
		return 1	# 1
	elif (number == 1):	# 1
		return value	# 1
	else:
		return value * function1(value, number-1)	# 1 + ( n - 1)
```
T(n) = 1 + 1 + 1 + 1 + 1 + (n - 1)
T(n) = 5 + (n - 1)
T(n) = 4 + n
T(n) = O(n)
```

## function 2:

Analyze function2 with respect to the length of the mystring.  Hint, you will need to set up two mathematical functions for operator counting.  one for function2 and the other for recursive_function2

```python

def recursive_function2(mystring, a, b):
    # n is the length of mystring.
    # T(n) is the number of operations needed to check if mystring is a palindrome.

    if a >= b:                             # Check if the pointers have crossed (1 operation)
        return True                        # Return True if they have crossed (1 operation)
    else:
        if mystring[a] != mystring[b]:    # Compare the characters at positions a and b (1 operation)
            return False                   # Return False if they don’t match (1 operation)
        else:
            return recursive_function2(mystring, a + 1, b - 1)  # Make a recursive call (1 operation)

def function2(mystring):
    return recursive_function2(mystring, 0, len(mystring) - 1)

# Total operations for recursive_function2:
# - The base case check happens once for every call.
# - The character comparison also happens once for each call.
# - Each recursive call adds to the operation count.

# For a string of length n, the function will make at most n/2 comparisons.
#
# We can express the operation count like this:
# T(n) = 1 + 1 + 1 + T(n-2)
# - The first 1 is for checking the base case.
# - The second 1 is for the character comparison.
# - The third 1 is for returning if the characters match.
# - T(n-2) represents the recursive call.

# This pattern keeps going until we hit the base case:
# - If n is even: T(n) = n + 2
# - If n is odd: T(n) = n + 1
#
# So we can say T(n) is roughly T(n) = n + c, where c is some constant.

# To wrap it up, T(n) is O(n).

```

### function 3 (optional challenge):

Analyze the following function with respect to number


```python
def function3(value, number):
	if (number == 0): # 1 operation
		return 1
	elif (number == 1): # 1 operation
		return value
	else:
		half = number // 2 # 1 operation
		result = function3(value, half) # log(n)
		if (number % 2 == 0): # 1 operation
			return result * result
		else:
			return value * result * result

T(n) = 1 + 1 + 1 + log(n) + 1
T(n) = 4 + log(n)
T(n) = O(logn)


```

## Part C reflection

Answer the following questions

1. Describe how to a approach writing recursive functions, what steps do you take?
   
Writing recursive functions can be simplified by focusing on two key steps: establishing the base case, which handles the simplest input, and defining the recursive case, which uses the function itself to reduce the problem towards the base case. Recursion restates a problem in terms of itself, with each step moving closer to the solution. For example, in the factorial function, 0! = 1 is the base case, and n! = n * (n-1)! is the recursive case. Thinking of recursion as using an already working function can make it easier to code

2. Describe the process of analyzing recursive functions.  How does it differ from from analyzing non-recursive functions?  How is it the same?

Analyzing a recursive function is like analyzing a non-recursive one. We use similar methods to create a formula showing how many operations are needed based on data size. For the factorial function, we define n as the number to find the factorial of and T(n) as the number of operations for computing n!. If n is 0 or 1, it takes three operations. If n is 2 or greater, it takes six operations plus the operations for the recursive call. This leads to the formula T(n) = 6 + T(n - 1). Ultimately, we find that T(n) = 6n - 3, showing that the complexity is O(n).

