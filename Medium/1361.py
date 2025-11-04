class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # 记录每个节点的入度
        in_degree = [0] * n
        # 记录每个节点的出度（用于验证每个节点最多有两个子节点）
        out_degree = [0] * n
        
        # 统计入度和出度
        for i in range(n):
            left = leftChild[i]
            right = rightChild[i]
            
            # 处理左子节点
            if left != -1:
                in_degree[left] += 1
                out_degree[i] += 1
                # 如果某个节点的入度大于1，直接返回False
                if in_degree[left] > 1:
                    return False
            
            # 处理右子节点
            if right != -1:
                in_degree[right] += 1
                out_degree[i] += 1
                # 如果某个节点的入度大于1，直接返回False
                if in_degree[right] > 1:
                    return False
        
        # 查找根节点（入度为0的节点）
        root_count = 0
        root = -1
        for i in range(n):
            if in_degree[i] == 0:
                root_count += 1
                root = i
                # 如果找到多个根节点，返回False
                if root_count > 1:
                    return False
        
        # 如果没有找到根节点，返回False
        if root_count != 1:
            return False
        
        # 验证所有节点是否连通且没有环
        visited = [False] * n
        stack = [root]
        visited[root] = True
        
        while stack:
            node = stack.pop()
            left = leftChild[node]
            right = rightChild[node]
            
            if left != -1:
                if visited[left]:
                    return False
                visited[left] = True
                stack.append(left)
            
            if right != -1:
                if visited[right]:
                    return False
                visited[right] = True
                stack.append(right)
        
        # 检查是否所有节点都被访问到
        return all(visited)
