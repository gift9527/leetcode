class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key = lambda x : (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res


if __name__ == "__main__":
    ins = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
    a = Solution()
    b = a.reconstructQueue(ins)
    print(b)