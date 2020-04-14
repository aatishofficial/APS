# leetcode - https://leetcode.com/problems/binary-tree-right-side-view
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res,queue=[],[(root,0)]
        while queue:
            cur,level=queue.pop(0)
            if cur:
                if len(res)<level+1:
                    res.append([])
                res[level].append(cur.val)
                queue.append((cur.left,level+1))
                queue.append((cur.right,level+1))
        return [x[-1] for x in res]
