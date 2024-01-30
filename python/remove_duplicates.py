from typing import List

# Solution explanation:

#  This solution doesn't use any complex algorithms. They have a simple while. To maintain runtime in O(n) we use a second list to do add objects.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        key = nums[0]
        count = 0
        i = 0
        newList = []
        while i != len(nums):
            if nums[i] > key:
                newList.append(nums[i])
                count = 1
                key = nums[i]
                i += 1
            elif count < 2:
                newList.append(nums[i])
                i += 1
                count += 1

        nums.clear()
        nums[:len(nums)] = newList

        return len(nums)


nums = [1,1,1,2,2,3]

print(Solution().removeDuplicates(nums = nums))
print(nums)
