class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        left = ["(", "{", "["]
        right = [")", "}", "]"]
        for x in s:
            if x in left:
                stack.append(x)
            else:
                if len(stack) == 0:
                    return False
                if right.index(x) != left.index(stack[-1]):
                    return False
                else:
                    stack.pop()
        return len(stack) == 0


s = Solution()
ans = s.isValid("{[]}")
print(ans)

