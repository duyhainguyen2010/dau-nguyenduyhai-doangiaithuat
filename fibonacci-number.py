class Solution(object):
    def fib(self, n):
        # nếu n = 0 hoặc 1 thì trả luôn
        if n <= 1:
            return n
        
        # a = F(0), b = F(1)
        a = 0
        b = 1

        # bắt đầu tính từ F(2) tới F(n)
        for i in range(2, n + 1):
            c = a + b   # số tiếp theo
            a = b       # dời a lên
            b = c       # dời b lên
        
        return b
