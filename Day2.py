## STARTER CODE
file = open('Day2_data', 'r')
data = file.read()
lines = data.splitlines()

# PART 1
def inc(nums):
    for i in range(len(nums) - 1):
        if nums[i + 1] > nums[i]:
            if nums[i + 1] - nums[i] > 3:
                return False
        else:
            return False
    return True

def dec(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            if nums[i] - nums[i + 1] > 3:
                return False
        else:
            return False
    return True

total = 0
for line in lines:
    nums = line.split()
    nums = list(map(int, nums))
    if nums[0] > nums[1]:
        if dec(nums):
            total += 1
    elif nums[0] < nums[1]:
        if inc(nums):
            total += 1
print(total)

# PART 2
total = 0
for line in lines:
    nums = line.split()
    nums = list(map(int, nums))
    for i in range(len(nums)):
        copy = nums.copy()
        copy.pop(i)
        if inc(copy) or dec(copy):
            total += 1
            break
print(total)