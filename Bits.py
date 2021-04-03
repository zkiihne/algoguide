
# https://leetcode.com/problems/counting-bits/
def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        output = [0, 1]
        prev = 1
        for i in range(2, num+1):
            if i == prev*2:
                prev = i
            output.append(output[i-prev] + 1)
        return output
