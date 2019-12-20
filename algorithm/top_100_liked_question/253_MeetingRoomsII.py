class Solution:
    def minMeetingRooms(self, intervals):
        if intervals is None or len(intervals) == 0:
            return 0

        tmp = []

        # 标记起始点终止点
        for inter in intervals:
            tmp.append((inter[0], True))
            tmp.append((inter[1], False))

        # 排序
        tmp = sorted(tmp, key=lambda v: (v[0], v[1]))

        n = 0
        max_num = 0
        for arr in tmp:
            # 起始点+1
            if arr[1]:
                n += 1
            # 终止点-1
            else:
                n -= 1
            max_num = max(n, max_num)
        return max_num


if __name__ == "__main__":
    s = [[0, 30],[5, 10],[15, 20]]
    a = Solution()
    b = a.minMeetingRooms(s)
    print(b)