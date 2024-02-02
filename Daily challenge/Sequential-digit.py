"""An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]"""

#solution 

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        li = []

        for i in range(1,10):
            n = i 
            nex = i+1 
            while n <= high and nex<=9:
                n = n*10 + nex 
                if low <= n <= high:
                    li.append(n)
                nex += 1 
        li.sort()
        return li
        
