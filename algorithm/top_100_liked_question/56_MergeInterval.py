class Solution(object):
    def run(self,intervals):
        out = []

        for i in sorted(intervals,key=lambda i:i[0]):
            if out and i[0] <= out[-1][-1]:
                out[-1][-1] = max(out[-1][-1],i[-1])
            else:
                out.append(i)
        return out



if __name__ == "__main__":
    a = Solution()
    b = [[1,4],[4,5]]

    c = a.run(b)

    print(c)