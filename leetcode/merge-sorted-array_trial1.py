class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        j = 0
        n1values = 0
        while j < n and i < m + n and n1values < m:
            if nums1[i] >= nums2[j]:
                nums1.insert(i, nums2[j])
                j += 1
                i += 1
            else:
                i += 1
                n1values += 1

        for k in range(j, n):
            nums1.insert(i, nums2[k])
            i += 1
        del nums1[n + m:]
        return None