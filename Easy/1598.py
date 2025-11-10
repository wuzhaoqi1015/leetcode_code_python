class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0  # 记录当前文件夹深度，主文件夹深度为0
        for log in logs:
            if log == "../":  # 返回上级目录
                if depth > 0:  # 只有不在主文件夹时才返回上级
                    depth -= 1
            elif log == "./":  # 停留在当前目录，深度不变
                continue
            else:  # 进入子文件夹，深度加1
                depth += 1
        return depth  # 当前深度就是返回主文件夹所需的最小步数
