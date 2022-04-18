class Solution:
    def compareTimes(self, time1, time2):
        if time1 == time2:
            return 0
        
        (h1, m1) = self.parseTime(time1)
        (h2, m2) = self.parseTime(time2)

        if h1 > h2 or (h1 == h2 and m1 > m2):
            return 1
        
        if h2 > h1 or (h2 == h1 and m2 > m1):
            return -1
        
        raise "Bad time."

    def parseTime(self, time):
        sections = time.split(':')
        return (int(sections[0]), int(sections[1]))

    def timeDifferenceInMinutes(self, time1, time2):
        (h1, m1) = self.parseTime(time1)
        (h2, m2) = self.parseTime(time2)

        comparison = self.compareTimes(time1, time2)

        result = 0
        if comparison > 0:
            result = (h1 - h2 + 1) * 60 - (60 - m1) - m2
        elif comparison < 0:
            result = (h2 - h1 + 1) * 60 - (60 - m2) - m1
        
        if result <= 720:
            return result
        else:
            return 1440 - result

    def findMinDifference(self, timePoints):
        timePoints.sort(key=lambda x: self.parseTime(x))
        minimum = 24 * 60

        for i in range(len(timePoints) - 1):
            minimum = min(minimum, self.timeDifferenceInMinutes(timePoints[i], timePoints[i+1]))
        minimum = min(minimum, self.timeDifferenceInMinutes(timePoints[-1], timePoints[0]))

        return minimum

s = Solution()
print(s.findMinDifference(["23:59", "00:02", "11:59", "00:00", "12:23"]))