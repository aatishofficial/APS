# leetcode - https://leetcode.com/problems/unique-binary-search-trees-ii/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n==0:
            return []
        return self.generate(1,n)
    def generate(self,start,end):
        res=[]
        if start>end:
            res.append(None)
            return res
        if start==end:
            res.append(TreeNode(start))
            return res
        left=right=None
        for i in range(start,end+1):
            left=self.generate(start,i-1)
            right=self.generate(i+1,end)
            for lnode in left:
                for rnode in right:
                    root=TreeNode(i)
                    root.left=lnode
                    root.right=rnode
                    res.append(root)
        return res
