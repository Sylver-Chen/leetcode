class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        while low < high:
            mid = int((low + high)/2)
            if isBadVersion(mid) is True:
                high = mid
            else:
                low = mid + 1
        return low
