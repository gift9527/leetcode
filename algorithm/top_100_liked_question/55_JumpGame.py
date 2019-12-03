class Solution(object):
    def run(self,array):
        m = 0

        for i,n in enumerate(array):
            if i > m:
                return False
            else:
                m = max(n + i,m)
        return True



if __name__ == "__main__":
    array = [2, 3, 1, 1, 4]
    a = Solution()
    b = a.run(array)
    print(b)