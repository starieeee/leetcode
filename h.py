from math import*
def main():
    sum = 0
    inT = int(input("Enter an integer: "))
    for i in range(1, inT + 1):
        sum += i**2
    print(f"Sum of squares of numbers 1--{inT} is {sum}")
main()