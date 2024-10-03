# write your code here
def hours(duration):
   return duration // 3600

def minutes(duration):
   h = hours(duration)

   duration = duration - (3600 * h)

   return duration // 60

def seconds(duration):
   h = hours(duration)
   duration -= 3600 * h


   m = minutes(duration)

   duration -= m * 60

   return duration 




