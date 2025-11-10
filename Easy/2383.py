class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        total_energy_needed = sum(energy) + 1  # 总精力需求为所有对手精力之和加1
        energy_train = max(0, total_energy_needed - initialEnergy)  # 计算精力训练小时数
        
        current_exp = initialExperience
        exp_train = 0
        
        # 遍历每个对手，计算经验训练需求
        for exp in experience:
            if current_exp <= exp:
                # 需要训练到比对手经验多1
                need_train = exp - current_exp + 1
                exp_train += need_train
                current_exp += need_train + exp  # 训练后获得经验加上击败对手获得的经验
            else:
                current_exp += exp  # 直接击败对手获得经验
        
        return energy_train + exp_train
