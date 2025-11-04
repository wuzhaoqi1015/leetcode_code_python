# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # 构建父节点映射表，用于向上遍历
        parent_map = {}
        
        def build_parent(node, parent):
            if not node:
                return
            parent_map[node] = parent
            build_parent(node.left, node)
            build_parent(node.right, node)
        
        build_parent(root, None)
        
        # 使用BFS搜索距离为k的节点
        from collections import deque
        result = []
        visited = set()
        queue = deque([(target, 0)])  # (节点, 当前距离)
        visited.add(target)
        
        while queue:
            node, dist = queue.popleft()
            
            # 如果当前距离等于k，将节点值加入结果
            if dist == k:
                result.append(node.val)
                continue
            
            # 如果距离超过k，提前终止
            if dist > k:
                continue
            
            # 遍历左子节点
            if node.left and node.left not in visited:
                visited.add(node.left)
                queue.append((node.left, dist + 1))
            
            # 遍历右子节点
            if node.right and node.right not in visited:
                visited.add(node.right)
                queue.append((node.right, dist + 1))
            
            # 遍历父节点
            if parent_map[node] and parent_map[node] not in visited:
                visited.add(parent_map[node])
                queue.append((parent_map[node], dist + 1))
        
        return result
