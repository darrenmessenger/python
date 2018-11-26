def print_message(message):
    print(message)

print_message("Hello World!")

my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)
    
def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])

assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("£$%%^") == 0, "Special characters"
assert count_upper_case("Hello World") == 2, "Hello World"

print("All the tests passed")

def even_number_of_evens(numbers):
     # Check to see if the list is empty
    if numbers == []:
        return False
    else:
        # Set a `number_of_evens` variable that will be incremented each time
        # an even number is found
        evens = 0
        
        # Iterate of over each item and if it's an even number, increment the
        # `evens` variable
        for number in numbers:
            if number % 2 == 0:
                evens += 1
        
        if evens == 0:
            return False
        else:
            return evens % 2 == 0


assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three are even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four are even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

print("All the tests passed for the function even_number_of_evens")
