class Solution(object):
    def countNegatives(self, grid):
        kq = 0
    
        for hang in grid:
           
            for so in hang:
                
                if so < 0:
                    kq += 1
        return kq
