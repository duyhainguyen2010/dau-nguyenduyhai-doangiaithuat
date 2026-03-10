class Solution:
    def numWaterBottles(self, numBottles, numExchange):

        tong_chai_da_uong = numBottles      
        chai_rong = numBottles 

        while chai_rong >= numExchange:

            chai_moi = chai_rong // numExchange
            tong_chai_da_uong += chai_moi

            chai_rong = chai_moi + (chai_rong % numExchange)

        return tong_chai_da_uong
