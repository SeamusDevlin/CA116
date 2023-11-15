#!/usr/bin/env python3

def enter_odd_number(count, numbers): if count < 10: num = input(f"Enter odd number #{count + 1}: ")
numbers[count] = int(num) if int(num) % 2 == 1 else 0
return enter_odd_number(count + 1, numbers)
return numbers
numbers = enter_odd_number(0, {})
odd_numbers_sum = sum(numbers.values())
print("The sum of the entered odd numbers is:", odd_numbers_sum)
