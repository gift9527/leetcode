



class Solution(object):
    def two_sum(self,array,target):

        array_dict = {}
        result = []
        for i in range(len(array)):
            if array[i] in array_dict:
                result.append([array_dict[array[i]],i])

            else:
                array_dict[target-array[i]] = i



        return result

if __name__ == "__main__":
    a = Solution()
    b = [1,6,8,9,11]
    c = 17
    s = a.two_sum(b,c)
    print (s)