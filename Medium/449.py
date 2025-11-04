# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        
        result = []
        stack = []
        current = root
        
        # 使用迭代前序遍历序列化二叉树
        while current or stack:
            if current:
                result.append(str(current.val))
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                current = current.right
        
        return ",".join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        
        # 将字符串分割为数值列表
        values = list(map(int, data.split(",")))
        
        def build_tree(nums, lower, upper):
            """递归构建二叉搜索树"""
            if not nums or nums[0] < lower or nums[0] > upper:
                return None
            
            val = nums.pop(0)
            node = TreeNode(val)
            node.left = build_tree(nums, lower, val)
            node.right = build_tree(nums, val, upper)
            return node
        
        return build_tree(values, float('-inf'), float('inf'))

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
