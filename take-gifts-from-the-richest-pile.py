class Solution(object):
    def pickGifts(self, gifts, k):
        for i in range(k):
            max = -1
            tam = -1
            for j in range(len(gifts)):
                if gifts[j] > max:
                    max = gifts[j]
                    tam = j
            gifts[tam] = int(math.sqrt(gifts[tam]))

        kq = 0
        for i in range(len(gifts)):
            kq += gifts[i]
        return kq
