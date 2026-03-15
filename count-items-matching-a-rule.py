class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        dem = 0

        for item in items:
            if ruleKey == "type":
                if item[0] == ruleValue:
                    dem += 1

            if ruleKey == "color":
                if item[1] == ruleValue:
                    dem += 1

            if ruleKey == "name":
                if item[2] == ruleValue:
                    dem += 1

        return dem
