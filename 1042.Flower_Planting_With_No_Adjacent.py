class Solution:
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int] 
        """
        from collections import defaultdict

        # 字典记录花园连通情况，list最大长度为3
        path_dict = defaultdict(list)
        # 字典记录已经种过花的花园，种的什么花
        garden_flower = {}
        for path in paths:
            path_dict[path[0]].append(path[1])
            path_dict[path[1]].append(path[0])

        flowers = set((1, 2, 3, 4))
        result = []
        # 遍历每个花园
        for i in range(1, N + 1):
            if i in path_dict:
                used_flowers = set()
                collected_gardens = path_dict[i]
                # 对于已经种过花的花园，排除这些花的类型
                for garden in collected_gardens:
                    if garden in garden_flower:
                        used_flowers.add(garden_flower[garden])
                res_flowers = flowers - used_flowers
                garden_flower[i] = res_flowers.pop()
            else:
                # 如果花园没和其他任何花园连通，随便种一种花即可
                garden_flower[i] = 1
            result.append(garden_flower[i])
        return result


s = Solution()
ans = s.gardenNoAdj(3, [[1, 2], [2, 3], [3, 1]])
print(ans)
