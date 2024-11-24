class Interval:
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper


    def is_empty(self):
        if self.lower > self.upper:
            return True
        return False
        

    def contains(self, number):
        return number >= self.lower and number <= self.upper

        

    def overlaps_with(self, other_interval):
        if not (self.is_empty() or other_interval.is_empty()):
            return (other_interval.contains(self.lower)
                     or other_interval.contains(self.upper)) or (self.contains(other_interval.lower
                                                                                or self.contains(other_interval.upper)))
        
        return False



interval_1 = Interval(1, 4)
interval_2 = Interval(4, 8)
print(interval_1.overlaps_with(interval_2))
            