def compute_xp_progress(daily_xp, level_cap):
    total_xp = 0
    total_xp_list = []
    for i in range(0, len(daily_xp)):
        if daily_xp[i] < 0:
            total_xp_list.append(total_xp)
        else:
            if total_xp + daily_xp[i] > level_cap:
                total_xp = level_cap
            else: 
                total_xp += daily_xp[i]
            total_xp_list.append(total_xp)
    
    return total_xp_list