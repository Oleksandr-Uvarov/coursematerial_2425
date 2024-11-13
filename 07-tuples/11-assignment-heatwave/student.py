# write your code here
def heatwave(temperatures):
    count = 0
    count_thirty = 0
    for temperature in temperatures:
        if temperature >= 25:
            count += 1
            if temperature >= 30:
                count_thirty += 1

            if count >= 5 and count_thirty >= 3:
                return True
        else:
            count = 0
            count_thirty = 0
    return False