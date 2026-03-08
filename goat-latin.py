class Solution:
    def toGoatLatin(self, sentence):

        vowels = "aeiouAEIOU"     # các nguyên âm
        words = sentence.split()  # tách câu thành các từ
        result = ""               

        i = 1  # vị trí từ

        for word in words:

            # nếu chữ đầu là nguyên âm
            if word[0] in vowels:
                new_word = word + "ma"

            # nếu chữ đầu là phụ âm
            else:
                new_word = word[1:] + word[0] + "ma"

            # thêm a theo vị trí
            new_word = new_word + ("a" * i)

            # ghép vào câu kết quả
            result = result + new_word + " "

            i = i + 1

        return result.strip()
