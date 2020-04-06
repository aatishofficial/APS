# leetcode - https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        queue,res=collections.deque([(root,0)]),[]
        while queue:
            node,level=queue.popleft()
            if node:
                if len(res)<level+1:
                    res.insert(0,[])
                res[-(level+1)].append(node.val)
                queue.append((node.left,level+1))
                queue.append((node.right,level+1))
        return res
