# Lab 2


### function 1:

Analyze the following function with respect to number

```python
def calculate_total(number):
    # Step 1: Establish variables and functions
    # Let n represent the input value number.
    # Let T(n) represent the number of operations needed to compute the result.
    
    total = 0  # 1 operation
    
    # Step 2: Count your operations
    # The loop runs n times.
    for i in range(number):  # n iterations
        x = i + 1  # 1 operation per iteration, so n operations
        total += x * x  # 3 operations (multiplication, addition, and assignment), so 3n operations
    
    # Step 3: Establish the mathematical expression for T(n)
    # T(n) = 1 + n + 3n + 1 = 4n + 2
    
    return total  # 1 operation

    # Step 4: Simplify the equation
    # T(n) = 4n + 2
    
    # Step 5: State your final result
    # Therefore, the time complexity of this function is O(n).

```

### function 2:

Analyze the following function with respect to number

```python
def function2(number):
    # Step 1: Establish variables and functions
    # Let n represent the input value number.
    # Let T(n) represent the number of operations needed to compute the result.

    # Step 2: Count your operations
    # number * (number + 1) → 1 multiplication and 1 addition, so 2 operations.
    # result * (2 * number + 1) → 1 multiplication and 1 addition, so 2 operations.
    # final result // 6 → 1 division.
    # Total number of operations: 2 + 2 + 1 = 5

    # Step 3: Establish the mathematical expression for T(n)
    # The total operations are constant, so T(n) = 5.

    # Step 4: Simplify the equation
    # Since T(n) = 5 is constant, it simplifies to O(1).

    # Step 5: State your final result
    # Therefore, the time complexity of this function is O(1).

    return (number * (number + 1) * (2 * number + 1)) // 6

```

### function 3:

Analyze the following with respect to the length of the list.  Note that the function call len() which returns the length of the list is constant (O(1)) with respect to the length of the list.
```python

def function3(list):
    # Step 1: Establish variables and functions
    # Let n represent the length of the input list.
    # Let T(n) represent the number of operations needed to sort the list.

    n = len(list)  # 1 operation

    # Step 2: Count your operations
    # Outer loop: Runs n - 1 times.
    # Inner loop: Runs n - 1 - i times, which sums to approximately (n^2)/2 iterations.
    # Comparison: 1 comparison per inner loop iteration, approximately (n^2)/2 comparisons.
    # Swap operations: 3 operations per swap, approximately 3(n^2)/2 operations.
    # Total number of operations: (n^2)/2 + 3(n^2)/2 = 2(n^2)

    for i in range(n - 1):  # Outer loop runs n - 1 times
        for j in range(n - 1 - i):  # Inner loop runs n - 1 - i times
            if list[j] > list[j + 1]:  # 1 comparison per iteration
                tmp = list[j]  # Swap starts
                list[j] = list[j + 1]  # Swap continues
                list[j + 1] = tmp  # Swap ends

    # Step 3: Establish the mathematical expression for T(n)
    # T(n) ≈ 2(n^2)

    # Step 4: Simplify the equation
    # T(n) ≈ 2n^2

    # Step 5: State your final result
    # Therefore, the time complexity of this function is O(n^2).

```
### function 4:

Analyze the following function with respect to number

```python
def function4(number):
    # Step 1: Establish variables and functions
    # Let n represent the input value number.
    # Let T(n) represent the number of operations needed to compute the result.

    total = 1  # 1 operation

    # Step 2: Count your operations
    # The loop runs n - 1 times.
    for i in range(1, number):  # n - 1 iterations
        total = total * (i + 1)  # 2 operations per iteration (addition and multiplication), so 2(n - 1) operations

    # Step 3: Establish the mathematical expression for T(n)
    # T(n) = 1 + 2(n - 1) + 1 = 2n

    return total  # 1 operation

    # Step 4: Simplify the equation
    # T(n) = 2n

    # Step 5: State your final result
    # Therefore, T(n) is O(n).
```


## In class portion


### Group members
List the members of your group member below:

	* Name 
	* ex. Hanbi Gong,Chaeeun Jang, Luwam Goitom-Worre
	* ...

### Timing Data

grab a screenshot of your excel graphs and put it here
<img width="479" alt="Part1" src="https://github.com/user-attachments/assets/c2fc37ee-8ecd-4ed3-aa44-06d75341525d">
<img width="459" alt="Part2" src="https://github.com/user-attachments/assets/c8ea6e6f-2c3e-48e6-b7a2-e15467466f67">
<img width="424" alt="Part3" src="https://github.com/user-attachments/assets/fa406172-89e9-43d5-b75b-590a7e1406e7">




### Summary 
|function| runtime based on analysis | Most similar curve | 
|---|---|---|
|partb_one()| O(n^2) | Quadratic |
|partb_two()| O(n)  |  Linear |
|partb_three()|  O(n) |  Linear |


### Discussion:

Look at the code from lab 1 and discuss the differences between fastest/slowest versions. Was it a difference in syntax? A difference in approach?  Write down your observations.


## Reflection:

1. for each function what growth rate best match your results?
- Parta_one:The time goes up like O(n^2), which means it gets slower pretty quickly as the input size increases. This fits what I see in the results.
- Partb_two: The time increases like O(n), which means it grows steadily. This matches my observations.
- Partc_three: This one also grows like O(n), showing a steady increase, just like partb_two().

2. Does your analysis match your analysis?  If not, where do you suppose the error occurred?
My analysis matches what I found in the results. If there are any differences, they might come from how the data was measured or other outside factors. It’s important to keep my measuring methods the same.

3. What sort of conclusions can you draw based on your observations?
- Knowing how functions grow helps me guess how they’ll perform with bigger inputs. The quadratic growth in partb_one() means it will slow down a lot with large data, while the linear growth in partb_two() and partb_three() shows they handle big data better.
- Since partb_one() is slower, there might be ways to make it faster by changing how it works.
- Functions that grow linearly can handle larger datasets better, which is useful for apps that need to work with a lot of data.



