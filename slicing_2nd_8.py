# Write code that uses slicing to get rid of the the second 8 so that here are only two 8’s in the list bound to the variable nums.

# knowing the position of the second 8 in the list:

nums = [4, 2, 8, 23.4, 8, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]

nums = nums[:4] + nums[5:]
print(nums)


# without knowing where the second number 8 is:

nums = [4, 2, 8, 23.4, 8, 9, 545, 9, 1, 234.001, 5, 49, 8, 9 , 34, 52, 1, -2, 9.1, 4]

num_eight = 0
for num in range(len(nums)):
    val = nums[num]
    if (val == 8):
        num_eight = num_eight + 1
        if (num_eight == 2):
            nums = nums[:num] + nums[num+1:]
            print(nums)
            break
