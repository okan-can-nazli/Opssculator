import random
import sys

num_range = list(range(1, 10))

def generate_problem(): 
    
    num1 = random.choice(num_range)
    num2 = random.choice(num_range) 
    
    operations = ["+","-","*","/"]
    
    operation = random.choice(operations)
   
    if operation == "/":
        
        # Filter for valid divisors of num1 in the range
        divisors = [i for i in num_range if num1 % i == 0] 
        # If divisors exist, choose one; otherwise, use 1 (which is always a divisor)
        num2 = random.choice(divisors) if divisors else 1
        
    problem = f"{num1} {operation} {num2}"
    return problem


def get_correct_answer(problem):
    num1_str, operation, num2_str = problem.split(" ")
    num1 = int(num1_str)
    num2 = int(num2_str)

    
    if operation == '+':
        correct_answer = num1 + num2
        
    elif operation == '-':
        correct_answer = num1 - num2
        
    elif operation == '*':
        correct_answer = num1 * num2
            
    elif operation == "/":
        correct_answer = num1 // num2
        
    else:
        print("There is an error while getting the operation!")
        sys.exit(0)
        
    return correct_answer


def is_correct(problem, answer):  # solution checker
    
    correct_answer = get_correct_answer(problem)
    return answer == correct_answer


