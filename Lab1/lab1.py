# Write the code for your lab 1 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab1.py
#
# Author: Hanbi Gong
# Student Number: 111932224
#


def wins_rock_scissors_paper(player, oponent):
    player = player.lower()
    oponent = oponent.lower()

    if player == oponent:
        return False
    elif player == "rock" and oponent == "scissors":  # Fixed here
        return True
    elif player == "scissors" and oponent == "paper":
        return True
    elif player == "paper" and oponent == "rock":
        return True
    else:
        return False


def factorial(n):
    result = 1
    if n == 0:
        return 1
    for i in range(1, n + 1):
        result *= i
    return result


def fibonacci(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    fib_n_1 = 1
    fib_n_2 = 0

    for i in range(2, n + 1):
        fib_n = fib_n_1 + fib_n_2
        fib_n_2 = fib_n_1
        fib_n_1 = fib_n

    return fib_n


def sum_to_goal(numbers, goal):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == goal:
                return numbers[i] * numbers[j]
    return 0
    

class UpCounter:

    def __init__(self, stepSize=1):
        self.stepSize = stepSize
        self.counter = 0
        self.newStepSize = None
    
    def count(self):
        return self.counter
    
    def update(self):
        if self.newStepSize is not None:
            self.stepSize = self.newStepSize

        self.counter += self.stepSize
        return self.counter


class DownCounter(UpCounter):

    def update(self):
        if self.newStepSize is not None:
            self.stepSize = self.newStepSize

        self.counter -= self.stepSize
        return self.counter

if __name__ == '__main__':
    c = UpCounter()
    print(c.count())  
    c.update()        
    print(c.count())  
    
    d = DownCounter()
    print(d.count())  
    d.update()        
    print(d.count())  
