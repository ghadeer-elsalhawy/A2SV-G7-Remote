class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i+ 1 for i in range(n)]
        # print(friends)
        pointer = 0
        for _ in range(1, n): # rounds of the game
            step = 0
            while step < k:
                if friends[pointer] != -1:
                    step += 1
                if step == k:
                    break
                pointer = (pointer + 1) % n
                # print(pointer)
            # print("eliminated:", friends[pointer])
            friends[pointer] = -1
        # print(friends)
        res = 0
        for i in range(n):
            if friends[i] != -1:
                res = i
                break
        return friends[res]