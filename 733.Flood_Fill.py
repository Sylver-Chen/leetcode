class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        # BFS with queue
        color = image[sr][sc]
        if color == newColor:
            return image
        r_length, c_length = len(image), len(image[0])
        queue = [(sr, sc)]
        while len(queue) > 0:
            r, c = queue.pop()
            if image[r][c] == color:
                image[r][c] = newColor
                if r-1 >= 0:
                    queue.append((r-1, c))
                if r+1 < r_length:
                    queue.append((r+1, c))
                if c-1 >= 0:
                    queue.append((r, c-1))
                if c+1 < c_length:
                    queue.append((r, c+1))
        return image

s = Solution()
ans = s.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
print(ans)
