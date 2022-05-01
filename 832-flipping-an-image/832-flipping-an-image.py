class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(image)):
            image[i] = image[i][-1::-1]
            for k in range(len(image[i])):
                if image[i][k] == 1:
                    image[i][k] = 0
                else:
                    image[i][k] = 1
        return image                 
                    
                    
        