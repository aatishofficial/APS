# leetcode - https://leetcode.com/problems/clone-graph
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        nodeCopy=Node(node.val)
        dic={node:nodeCopy}
        queue=collections.deque([node])
        while queue:
            node=queue.popleft()
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    neighborCopy=Node(neighbor.val)
                    dic[neighbor]=neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    queue.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy
