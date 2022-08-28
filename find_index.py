# Given a sorted array of distinct integers and a target value, 
# RETURN THE INDEX if the target is found. If not,
# return the index where it would be if it were inserted in order.

# Input: nums = [1,3,5,6]
# Target = 5; Output = 2
# Target = 2; Output = 1
# Target = 7; Output = 4

def find_index(nums, target_num):
    
    if target_num in nums:
        result = nums.index(target_num)
        return result

    else:
        nums.append(target_num)
        nums.sort()
        result = nums.index(target_num)
        return result

nums = [1,3,5,6]
target_num = 5
#target_num = 2
#target_num = 7

print(find_index(nums, target_num))