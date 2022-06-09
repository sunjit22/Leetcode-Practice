import numpy as np
class Solution:
    def findProd(self, arr: list[int]):
        neg = 0
        negInd = list()
        arrSize = len(arr)
        print("Incoming arr - ", arr)
        if arrSize == 0:
            return -1
        if arrSize == 1:
            print("Size 1, going back")
            return arr[0]
        for i in range(arrSize):
            if arr[i] < 0:
                neg += 1
                negInd.append(i)
        if neg % 2 == 0:
            prod1 = np.prod(arr)
            print("neg%2 == 0", prod1)
            print("even number of negs, going back")
            return prod1
        else:
            p1 = -1
            p2 = -1
            print("arr - ", arr, " negInd[0] - ", negInd[0])
            if len(negInd) == 1 and negInd[0] + 1 == arrSize:
                p1 = np.prod(arr[:negInd[0]])
                print("Only 1 neg, in last position. Going back. p1, p2 - ", p1, p2)
                return max(p1, p2)
            if len(negInd) == 1 and negInd[0] == 0:
                p1 = np.prod(arr[negInd[0] + 1:])
            if negInd[0] + 1 < arrSize:
                print("p1 ", arr[negInd[0] + 1:])
                p1 = np.prod(arr[negInd[0] + 1:])
                print("p2 ", arr[:negInd[-1]])
                p2 = np.prod(arr[:negInd[-1]])
            print("p1, p2", p1, p2)
            return max(p1, p2)

    def maxProduct(self, nums: list[int]) -> int:
        # tempList = list()
        prods = list()
        arrSize = len(nums)
        if arrSize == 1:
            return nums[0]
        left = 0
        right = 0
        flag = 1
        for i in nums:
            if i == 0:
                flag = 0
                break
        if flag:
            return self.findProd(nums)
        for i in range(arrSize):
            if nums[i] != 0:
                right += 1
                print("right - ", right)
                if right == arrSize and nums[left:right]:
                    prods.append(self.findProd(nums[left:right]))
            if nums[i] == 0:
                prods.append(self.findProd(nums[left:right]))
                print("nums[left:right] - ", nums[left:right])
                left = i + 1
                # right = i+1
                print("now left - ", left, ", right - ", right)
                right = i + 1
                continue
            if left == right and left < arrSize:
                prods.append(self.findProd(nums[left]))

        print("prods - ", prods)
        maxN = max(prods)
        return int(max(maxN, 0))