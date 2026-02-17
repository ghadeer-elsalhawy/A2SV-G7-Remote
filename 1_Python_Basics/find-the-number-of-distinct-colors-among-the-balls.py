class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        res = [0] * len(queries) 
        # balls = [0] * (limit + 1)
        # for i in range(len(queries)):
        #     balls[queries[i][0]] = queries[i][1]
        #     unique = set()
        #     for ball in balls:
        #         if ball != 0:
        #             unique.add(ball)
        #     res[i] = len(unique)
        balls = {}
        colors = {}
        for i, [idx, color] in enumerate(queries):
            if idx in balls:
                colors[balls[idx]] -= 1
                if colors[balls[idx]] == 0:
                    del colors[balls[idx]]
                balls[idx] = color
                if color not in colors:
                    colors[color] = 0
                colors[color] += 1
            else:
                balls[idx] = color
                if color not in colors:
                    colors[color] = 0
                colors[color] += 1
            res[i] = len(colors)
        return res
    