class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # 首先对文件夹路径进行排序，确保父文件夹在子文件夹之前
        folder.sort()
        result = []
        
        # 遍历排序后的文件夹列表
        for f in folder:
            # 如果结果列表为空，直接添加当前文件夹
            if not result:
                result.append(f)
            else:
                # 获取结果列表中最后一个添加的文件夹
                last_folder = result[-1]
                # 检查当前文件夹是否是最后一个文件夹的子文件夹
                # 需要确保匹配路径后紧跟'/'或到达字符串末尾
                if not f.startswith(last_folder + '/'):
                    result.append(f)
        
        return result
