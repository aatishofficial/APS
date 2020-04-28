# leetcode - https://leetcode.com/problems/binary-tree-paths/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res=[]
        self.dfs(root,[root.val],res)
        return res
    def dfs(self,root,path,res):
        if not root.left and not root.right:
            res.append(self.help(path))
            return
        if root.left:
            self.dfs(root.left,path+[root.left.val],res)
        if root.right:
            self.dfs(root.right,path+[root.right.val],res)
    def help(self,path):
        t=''
        for i in range(len(path)-1):
            t+=str(path[i])+'->'
        t+=str(path[len(path)-1])
        return t
