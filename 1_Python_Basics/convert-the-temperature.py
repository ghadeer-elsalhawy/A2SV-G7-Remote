# Problem link: https://leetcode.com/problems/convert-the-temperature/

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, round(celsius * 1.80 + 32.00, 5)]
