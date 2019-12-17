class Solution(object):
    def run(self, array, k):
        for i in range(len(array)):
            for j in range(i-1):
                if array[j] < array[j+1]:
                    array[j],array[j+1] = array[j+1],array[j]
        return array[k-1]




if __name__ == "__main__":
    a = Solution()
    array = [3,2,1,5,6,4]
    k = 2
    b = a.run(array,k)
    print(b)