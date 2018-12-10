#! usr/bin/env python

'''
In this assignment,
you are asked to generate the first n elements of a Fibonacci series,
where n is taken from user's input.

You may want to start with the following snippet
'''

def printFibonacciNumbers(n):
    a,b = 0,1
    counter = 0
    while counter < n:
        print(a)
        a, b = b, a+b
        counter += 1
    

def main():
    n = int(input("Enter an integer n: "))
    print("\nThe first %d elements of a Fibonacci series are "% n)
    printFibonacciNumbers(n)
    
if __name__ == '__main__':
    main()
