class Solution:
    def heightChecker(self, heights):

        chieu_cao_dung = sorted(heights)   # mảng chiều cao sau khi sắp xếp
        dem_sai = 0                        # đếm số vị trí sai

        for i in range(len(heights)):
            if heights[i] != chieu_cao_dung[i]:
                dem_sai = dem_sai + 1

        return dem_sai
