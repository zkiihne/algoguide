




# https://leetcode.com/problems/longest-consecutive-sequence/
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums = set(nums)
        cmax = 1
        for num in nums:
            if num - 1 not in nums:
                count = 1
                curr = num
                going = True
                while going:
                    if curr + 1 in nums:
                        count = count + 1
                        curr = curr + 1
                    else:
                        going = False
                if cmax < count:
                    cmax = count
        return cmax





