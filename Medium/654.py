# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # 递归终止条件：如果数组为空，返回None
        if not nums:
            return None
        
        # 找到当前数组中的最大值及其索引
        max_val = max(nums)
        max_index = nums.index(max_val)
        
        # 创建根节点，值为最大值
        root = TreeNode(max_val)
        
        # 递归构建左子树：使用最大值左边的子数组
        root.left = self.constructMaximumBinaryTree(nums[:max_index])
        
        # 递归构建右子树：使用最大值右边的子数组
        root.right = self.constructMaximumBinaryTree(nums[max_index+1:])
        
        return root
