class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        total = 0
        tgdocdung = 0
        for i in timeSeries:
            if i >= tgdocdung:
                total += duration
            else:
                total += (i + duration - tgdocdung)
            tgdocdung = i + total

        return total
        
