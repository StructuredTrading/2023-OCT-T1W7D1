# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def sum_of_multiples(multiple1, multiple2, lower_limit = 1, higher_limit = 1000):
    sum = 0

    # Iterate from 1 to 000
    for i in range(lower_limit, higher_limit):

        # add if multiple of 3 or 5
        if(i % multiple1 == 0 or i % multiple2 == 0):
            sum += i

    return sum

print(sum_of_multiples(3, 5))
print(sum_of_multiples(5, 7, 100, 500))