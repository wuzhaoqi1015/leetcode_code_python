# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.values = set()  # 使用集合存储所有节点的值
        self._recover_tree(root, 0)  # 从根节点开始恢复二叉树，根节点值为0
        
    def _recover_tree(self, node: Optional[TreeNode], val: int):
        if not node:
            return
        node.val = val  # 恢复当前节点的值
        self.values.add(val)  # 将值加入集合
        # 递归恢复左子树，左子节点值为 2*x+1
        if node.left:
            self._recover_tree(node.left, 2 * val + 1)
        # 递归恢复右子树，右子节点值为 2*x+2
        if node.right:
            self._recover_tree(node.right, 2 * val + 2)

    def find(self, target: int) -> bool:
        return target in self.values  # 在集合中查找目标值


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
