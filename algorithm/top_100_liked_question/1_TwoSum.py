class Solution(object):
    def run(self, array, target):
        a_dict = {}
        result = []
        for i in range(len(array)):
            if array[i] not in a_dict:
                a_dict[target - array[i]] = i
            else:
                result.append([i,a_dict[array[i]]])

        return result



if __name__ == "__main__":
    a = [2, 7, 11, 15]
    target = 9

    b = Solution()
    c = b.run(a, target)
    print(c)
