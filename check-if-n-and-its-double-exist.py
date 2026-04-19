class Solution(object):
    def checkIfExist(self, arr):

        result = set()
        
        for so in arr:
            # Kiểm tra xem có số nào gấp đôi hiện tại hoặc bằng nửa hiện tại không
            if (so * 2 in result) or (so % 2 == 0 and so // 2 in result):
                return True
            

            result.add(so)
            
     
        return False
