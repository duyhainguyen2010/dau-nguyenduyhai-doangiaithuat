class Solution(object):
    def capitalizeTitle(self, title):
        result  = []
        words = title.lower().split(" ")

        for i in range(len(words)):

            if len(words[i]) <= 2:
                result.append(words[i])

            else:
                result.append(words[i][0].upper() + words[i][1:])

        return " ".join(result)
