


class Solution(object):

    def run(self,s,numRows):

            index = 0
            step = 1

            L = [""]*numRows

            for i in range(len(s)):
                if index == 0:
                    step = 1

                elif index == numRows - 1:
                    step = -1

                L[index] = L[index] + s[i]

                index = index + step

            return "".join(L)


if __name__ == "__main__":
    a = Solution()
    b = a.run("PAYPALISHIRING",3)
    print(b)











