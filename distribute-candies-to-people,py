class Solution(object):
    def distributeCandies(self, candies, num_people):
        i = 0
        arr = [0] * num_people
        while(candies > 0):
            i += 1
            people = (i - 1) % num_people
            if i < candies:
                arr[people] += i
                candies -= i
            else:
                arr[people] += candies
                candies = 0
        return arr 
