def alphabet_war(fight):
    fight = list(fight)
    power = 0
    LEFT_UNITS = "sbpw" #s
    RIGHT_UNITS = "zdqm" #j
    
    for i in range(len(fight)):
        if fight[i] == 't':
            try: 
                if fight[i - 1] in RIGHT_UNITS:
                    fight[i - 1] = LEFT_UNITS[RIGHT_UNITS.index(fight[i - 1])]
                elif fight[i + 1] in RIGHT_UNITS:
                    fight[i + 1] = LEFT_UNITS[RIGHT_UNITS.index(fight[i + 1])]
            except IndexError: pass
        elif fight[i] == 'j': 
            try: 
                if fight[i - 1] in LEFT_UNITS:
                    fight[i - 1] = RIGHT_UNITS[LEFT_UNITS.index(fight[i - 1])]
                elif fight[i + 1] in LEFT_UNITS:
                    fight[i + 1] = RIGHT_UNITS[LEFT_UNITS.index(fight[i + 1])]
            except IndexError: pass
    
    for i in range(len(fight)):
        if fight[i] in LEFT_UNITS:
            power += LEFT_UNITS.index(fight[i]) + 1
        if fight[i] in RIGHT_UNITS:
            power -= RIGHT_UNITS.index(fight[i]) + 1
        
    if power > 0:
        return "Left side wins!"
    if power < 0:
        return "Right side wins!"
    return "Let's fight again!"
    return power
