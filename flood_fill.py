# problem url https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3326/

class Solution:
    def fill(self, original_color, new_color, start_row, start_col, image, m, n):
        top = None
        down = None
        left = None
        right = None
        
        if 0<start_col:
            left = image[start_row][start_col-1]
            
        if 0<start_row:
            top = image[start_row-1][start_col]
            
        if start_row+1<m: 
            down = image[start_row+1][start_col]
        
        if start_col+1<n:
            right = image[start_row][start_col+1]
        
        
        if left == original_color:
            image[start_row][start_col-1] = new_color
            self.fill(original_color, new_color, start_row, start_col-1, image, m, n)

        if top == original_color:
            image[start_row-1][start_col] = new_color
            self.fill(original_color, new_color, start_row-1, start_col, image, m, n)
                
        if right == original_color:
            image[start_row][start_col+1] = new_color
            self.fill(original_color, new_color, start_row, start_col+1, image, m, n)
                
        if down == original_color:
            image[start_row+1][start_col] = new_color
            self.fill(original_color, new_color, start_row+1, start_col, image, m, n)
            
        if left!=original_color and right!=original_color and top!=original_color and down!= original_color:
            return

        
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        original_color = image[sr][sc]
        image[sr][sc] = newColor
        
        if original_color == newColor:
            return image
        
        m = len(image)
        n = len(image[0])
        self.fill(original_color, newColor, sr, sc, image, m, n)
        
        return image


'''
Solution written by someone else, better runtime.

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if len(image) == 0:
            return []
        
        X, Y = len(image), len(image[0])
        color = image[sr][sc]
        
        if color == newColor:
            return image
        
        frontier_stack = [(sr, sc)]
        while len(frontier_stack) > 0:
            point = frontier_stack.pop()
            x, y = point[0], point[1]
            image[x][y] = newColor
            
            candidates = ((x + 1, y),
                          (x - 1, y),
                          (x, y + 1),
                          (x, y - 1),)
            for cand in candidates:
                x, y = cand[0], cand[1]
                if x >= X or x < 0 or y >= Y or y < 0:
                    continue
                if image[x][y] == color:
                    frontier_stack.append(cand)
        
        return image
'''