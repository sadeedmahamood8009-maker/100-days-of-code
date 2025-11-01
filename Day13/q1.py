number = int(input("Enter the number: "))
def odd_or_even(number):
    if number % 2 == 0:
        print(f"{number} This is an even number.")
    else:
        print(f"{number} This is an odd number.")
odd_or_even(number)