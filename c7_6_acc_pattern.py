# Count the number of characters in string str1. Do not use len(). Save the number in variable numbs.

str1 = "I like nonsense, it wakes up the brain cells. Fantasy is a necessary ingredient in living."
numbs = 0
for num in str1:
  numbs = numbs + 1
print(numbs)


# Create a list of numbers 0 through 40 and assign this list to the variable numbers. Then, accumulate the total of the list’s values and assign that sum to the variable sum1.

numbers = list(range(41))
sum1 = 0
for numb in numbers:
    sum1 = sum1 + numb
print(sum1)
