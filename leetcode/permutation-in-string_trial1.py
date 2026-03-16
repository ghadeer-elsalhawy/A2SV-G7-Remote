class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = Counter(s1)
        left = 0
        perm = {}
        status = False
        for right in range(len(s2)):
            if s2[right] not in freq:
                perm = {}
                left = right + 1
            else:
                while perm.get(s2[right], 0) == freq[s2[right]]: 
                    perm[s2[left]] -= 1
                    if perm[s2[left]] == 0:
                        del perm[s2[left]]
                    left += 1  
                
                perm[s2[right]] = perm.get(s2[right], 0) + 1 
                stat = True
                for k, v in freq.items():
                    if k in perm and perm[k] == v:
                        continue
                    else:
                        stat = False
                if stat: 
                    status = True
                    break
        return status