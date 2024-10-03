from math import ceil
# write your code here
def internet_costs(duration_in_seconds, cost_per_block):
    minute_block = 6

    
    minutes_in_question = ceil(duration_in_seconds / 60) # could be used without ceil here but
                                                         # it's still used to be more readable

    blocks = ceil(minutes_in_question / 6)

    cost =  blocks * cost_per_block

    if duration_in_seconds == 0:
        return 0
    elif duration_in_seconds < 360:
        return cost_per_block
    else:
        return cost






