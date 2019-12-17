class Solution(object):
    def run(self, street):
        last = 0
        now = 0
        for i in street:
            last, now = now, max(i + last, now)

        return now


if __name__ == "__main__":
    street = [2, 7, 9, 3, 1]

    a = Solution()
    b = a.run(street)
    print(b)
