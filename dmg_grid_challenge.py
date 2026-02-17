def build_damage_grid(max_attack, max_defense): 
    attack_list = []
    
    
    for attack in range(1, max_attack + 1):
        defense_list = []
        for defense in range (1, max_defense + 1):
            if attack - defense <= 0:
                resolution = 0
                defense_list.append(resolution)
            else:
                resolution = attack - defense
                defense_list.append(resolution) 
        attack_list.append(defense_list)   

    return attack_list