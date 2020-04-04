# leetcode - https://leetcode.com/problems/binary-tree-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        cur=root
        pre=None
        while cur:
            if cur.left==None:
                res.append(cur.val)
                cur=cur.right
            else:
                pre=cur.left
                while pre.right!=None:
                    pre=pre.right
                pre.right=cur
                temp=cur
                cur=cur.left
                temp.left=None
        return res
