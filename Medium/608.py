import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    # 创建结果DataFrame，初始包含所有节点id
    result = tree[['id']].copy()
    
    # 找出根节点（p_id为null的节点）
    root_nodes = tree[tree['p_id'].isnull()]['id'].tolist()
    
    # 找出所有有子节点的节点（内部节点）
    # 如果一个节点的id出现在其他节点的p_id列中，说明它有子节点
    parent_nodes = tree[tree['id'].isin(tree['p_id'])]['id'].tolist()
    
    # 定义判断节点类型的函数
    def get_node_type(node_id):
        if node_id in root_nodes:
            return 'Root'
        elif node_id in parent_nodes:
            return 'Inner'
        else:
            return 'Leaf'
    
    # 为每个节点添加类型
    result['type'] = result['id'].apply(get_node_type)
    
    return result
