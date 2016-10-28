#!/usr/bin/env python3

# The Collatz Sequence
# Take a number and run collatz function until result is one
# If even, floor divide by two
# If odd, multiply by three and add one
def collatz(num):
    number = int(num)

    if (number % 2 == 0):
        return (number // 2)
    else:
        return ((number * 3) + 1)

def main():
    try:
        num = input("Please enter a number: ")
    except NameError:
        print("You must enter an integer.")
        return -1

    try:
        while (int(num) > 1):
            num = collatz(num)
            print(num)
    except ValueError:
        print("You must enter an integer.")
        return -1

if __name__ == '__main__':
    main()