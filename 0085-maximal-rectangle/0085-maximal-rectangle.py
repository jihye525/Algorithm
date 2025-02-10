class Solution:   
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        def largestRectangleArea(heights):
            stack = []
            max_area = 0
            heights.append(0)  

            for i, h in enumerate(heights):
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)

            return max_area

        rows, cols = len(matrix), len(matrix[0])
        height = [0] * cols  
        max_area = 0

        for i in range(rows):
            for j in range(cols):
                height[j] = height[j] + 1 if matrix[i][j] == '1' else 0
            
            max_area = max(max_area, largestRectangleArea(height))

        return max_area


