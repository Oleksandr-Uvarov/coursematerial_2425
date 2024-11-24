class Interval:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper


        def is_empty(self):
            if lower > upper:
                return True
            return False
        

        def contains(self, number):
            return number >= lower and number <= upper

        

        def overlaps_with(self, other_interval):
           return other_interval.contains(self.lower) or other_interval.contains(self.upper)
            