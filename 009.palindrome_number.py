class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 ==0):
            return False
        else:
            # 该步骤和007.reverse-integer.py相同，反转数字
            # 只要反转x的一半，然后对比两者即可
            half = 0
            while x > half:
                half = half * 10 + x % 10
                x = int(x / 10)
            return x == half or int(half/10) == x

s = Solution()
ans = s.isPalindrome(121)
print(ans)


