class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        if S == T:
            return True
        s_stack = []
        t_stack = []
        for elm in S:
            if elm != "#":
                s_stack.append(elm)
            elif len(s_stack) > 0:
                s_stack.pop()
            else:
                continue
        for elm in T:
            if elm != "#":
                t_stack.append(elm)
            elif len(t_stack) > 0:
                t_stack.pop()
            else:
                continue
        return ''.join(s_stack) == ''.join(t_stack)

s = Solution()
ans = s.backspaceCompare("a#c", "b")
print(ans)


