# 给定一个没有重复数字的序列，返回其所有可能的全排列。
 
class Solution(object):
    def permute(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

        def backtrack(nums, path, visited, res):
            # 在已有路径path基础上，填充完剩余的所有数字
            # visited表示已经使用过的数字
            if len(nums) == len(path):
                # 注意此处不能用res.append(path])，因为在回溯时path被撤销，必须深拷贝
                res.append(path[:])
            for num in nums:
                if num not in visited:
                    visited.append(num)
                    path.append(num)
                    backtrack(nums, path, visited, res)
                    visited.pop()
                    path.pop()

        res = []
        backtrack(nums, [], [], res)
        return res


s = Solution()
ans = s.permute([1, 2, 3])
print(ans)
