import collections
class Solution(object):
    def run(self,task,interval):
        task_value = collections.Counter(task)
        max_task = task_value.most_common()[0][1]
        max_task_count = len([i for i,v in task_value.items() if v == max_task])
        return (max_task - 1) * (interval + 1) + max_task_count




if __name__ == "__main__":
    task = ["A","A","A","B","B","B"]
    interval = 2

    a = Solution()
    b = a.run(task,interval)
    print(b)
