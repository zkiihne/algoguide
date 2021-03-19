# Dynamic Programming -> a problem that can be solved recursively that has repeat work

# Sum -> when a DP problem asks for, total possible unique
# Example: https://leetcode.com/problems/combination-sum-iv/

# Min/Max -> when a DP problem asks for, shortest most longest least
# Min example: https://leetcode.com/problems/coin-change/
# Max example: 

def min(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # default
        if amount == 0:
            return 0

       # single row of memory
        dprow = []
        # for each value leading up to the final total
        for s in range(1, amount+1):
            min_val = float("inf")
            # for each of the options
            for i in range(0, len(coins)):
                value = coins[i]
                # conditioned comparison based on previous answers
                val = min(1 + dprow[s - value - 1], s - value + 1)
                if val < min_val:
                    min_val = val
            # single row modified with new answer
            dprow.append(min_val)
        if dprow[amount-1] == float("inf"):
            return -1
        return goodrow[amount-1]

# Linear -> when a DP problem does not require you to store past states
# Example: https://leetcode.com/problems/jump-game/


def linear(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # defaults
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        # single number to keep track
        maxforward = nums[0]
        for n in range(1, len(nums)-1):
            # iterate over adding or subtracting from single number
            maxforward = maxforward - 1
            if maxforward < nums[n]:
                maxforward = nums[n]
            if maxforward == 0:
                return False
            
        return True


















