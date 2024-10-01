# write your code here
def hours(number):
   return number // 3600

def minutes(number):
   seconds_left = 0

   if number >= 3600:
        seconds_left = hours(number)
   else:
        seconds_left = number // 60

   return seconds_left // 60

print(minutes(400))