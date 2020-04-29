class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 已经见过的对（值，索引）
        d = {}
        for i, num in enumerate(nums):
            if target-num in d:
                return [d[target-num], i]
            else:
                d[num] = i



