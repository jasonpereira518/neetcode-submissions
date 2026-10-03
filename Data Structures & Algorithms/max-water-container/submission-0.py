class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        l,r = 0, len(heights) - 1

        while l < r:
            area = 0
            if heights[l] <= heights[r]:
                
                area = min(heights[l],heights[r]) * (r-l)
                max_area = max(area, max_area)
                l += 1
            elif heights[l] > heights[r]:
                
                area = min(heights[l],heights[r]) * (r-l)
                max_area = max(area, max_area)
                r -= 1

        return max_area