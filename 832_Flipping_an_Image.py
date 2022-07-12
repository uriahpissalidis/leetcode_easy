class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        #ans, ans2 = [], []
        for i in range(len(image)):
            count = 0
            for j in range(len(image)):
                if image[i][j] == 0:
                    image[i][j] = 1
                    count += 1
                else:
                    image[i][j] = 0
                    count += 1
                if count == len(image):
                    image[i] = image[i][::-1]        
        return image