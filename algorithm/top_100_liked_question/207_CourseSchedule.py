class Solution(object):
    def run(self, course_nums, requirements):
        graph = [[] for _ in range(course_nums)]
        visit = [0 for _ in range(course_nums)]
        for x, y in requirements:
            graph[x].append(y)





    def dfs(self):
        pass


if __name__ == "__main__":
    num = 2
    require = [[0, 1]]
