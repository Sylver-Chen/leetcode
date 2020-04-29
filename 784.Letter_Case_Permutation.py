class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: string
        """
        # 从左往右遍历每个字符，保持ans为已遍历过的字符的所有字母大小的全排列
        # 当当前字符为数字时，遍历ans中全排列，将该数字添加到该全排列末尾
        # 当当前字符为字母时，遍历ans中全排列,增加一个该全排列的副本，分别添加字母的大小写
        ans = [[]]
        for char in S:
            n = len(ans)
            if char.isalpha():
                for i in range(n):
                    ans.append(ans[i][:])
                    ans[i].append(char.lower())
                    ans[n + i].append(char.upper())
            else:
                for i in range(n):
                    ans[i].append(char)
        return list(map("".join, ans))


s = Solution()
ans = s.letterCasePermutation("a1b2")
print(ans)
