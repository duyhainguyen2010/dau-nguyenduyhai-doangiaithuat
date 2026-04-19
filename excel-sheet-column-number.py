class Solution(object):
    def titleToNumber(self, columnTitle):
        ket_qua = 0

        for ky_tu in columnTitle:
            gia_tri = ord(ky_tu) - ord('A') + 1
            ket_qua = ket_qua * 26 + gia_tri

        return ket_qua
