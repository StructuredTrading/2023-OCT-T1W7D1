# Find out if a number is prime or not

def is_prime(number):
    for i in range(2, number):
        if(number % i == 0):
            print("Not a Prime")
            break
    else:
        print("A Prime")

while True:
    user_input = int(input("Enter a number to test if its a Prime number: "))
    is_prime(user_input)