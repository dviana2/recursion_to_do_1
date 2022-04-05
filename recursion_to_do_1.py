# Recursive Sigma
# Write a recursive function that given a number returns the sum of integers from 1 to that number. 
# Example: rSigma(5) = 15 (1+2+3+4+5); rSigma(2.5) = 3 (1+2); rSigma(-1) = 0.

def sigma(x):
    if x <= 1:
        return 1
    else:
        return x + sigma(x-1)

print(sigma(4))


# Recursive Factorial
# Given num, return the product of ints from 1 up to num. If less than zero, treat as zero. 
# If not an integer, truncate. Experts tell us 0! is 1. rFact(3) = 6 (1*2*3). Also, rFact(6.5) = 720 (1*2*3*4*5*6).

def recursive_factorial(x):
    if x <= 1:
        return 1
    else:
        return x * recursive_factorial(x-1)

print(recursive_factorial(8))

