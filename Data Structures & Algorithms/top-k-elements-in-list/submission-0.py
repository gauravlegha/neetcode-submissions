from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. FIXED: Count frequencies in a single pass O(N)
        d = dict()
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
                
        # 2. FIXED: Sort items by their values (frequencies) in descending order
        # item[1] is the frequency count, item[0] is the actual number
        sorted_items = sorted(d.items(), key=lambda item: item[1], reverse=True)
        
        # 3. FIXED: Extract the top k keys (numbers) from the sorted list
        res = []
        for i in range(k):
            res.append(sorted_items[i][0])
            
        return res

