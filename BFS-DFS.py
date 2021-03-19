#Important algorithms for graph traversal


# DFS is about traversal of a graph via single adjacent nodes
# Example: https://leetcode.com/problems/flood-fill/
def DFS(self, image, sr, sc, newColor):
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)

        dfs(sr, sc)
        return image 

      
      

# BFS traverses all adjacent nodes
# When you want to find depth, 
# Example: https://leetcode.com/problems/minimum-depth-of-binary-tree/

def BFS(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            lDepth = self.BFS(root.left)
            rDepth = self.BFS(root.right)
            
            if min(lDepth, rDepth) == 0:
                return 1 + max(lDepth, rDepth)
            else:
                return 1 + min(lDepth, rDepth)
