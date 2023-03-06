def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return number * 3 + 1

print('Enter a number')
try:
    number = int(input())
    print(number)
    while number != 1:
        number = collatz(number)
        print(number)
except ValueError:
    print('Please enter a number')

            
