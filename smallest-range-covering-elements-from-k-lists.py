import heapq


class Solution:
    def smallestRange(self, nums):
        ares = []
        m = len(nums)
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                ares.append([nums[i][j], i])

        ares.sort()
        a = 10 ** 9
        left_idx = 0
        right_idx = 0
        i = 0

        while i < len(ares):
            left_lst = set([ares[i][1]])
            if len(left_lst) == m:
                return [ares[i][0], ares[i][0]]
            for j in range(flag, min(i+m,len(ares))):
                right_lst = set([ares[j][1]])
                left_lst = left_lst.union(right_lst)
                if len(left_lst) == m:
                    left_idx = ares[i][0]
                    right_idx = ares[j][0]
                    return [left_idx, right_idx]
            flag = min(i+m, len(ares))

            i +=1
        # for i in range(min_nnum, max_nnum + 1):
        #     left_lst = set(ares[i])
        #     if len(left_lst) == m:
        #         return [i, i]
        #     for j in range(i+1, max_nnum + 1):
        #         right_lst = set(ares[j])
        #         if right_lst:
        #             left_lst = left_lst.union(right_lst)
        #             if len(left_lst) == m:
        #                 if j - i < a:
        #                     a = j -i
        #                     left_idx = i
        #                     right_idx = j
        # i = min_nnum




        return [left_idx, right_idx]

class Solution2:
    def smallestRange(self, nums):
        li = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                li.append([nums[i][j], i])
        li.sort()

        visited = [0] * len(nums)
        count = 0
        left = 0
        start, end = -10**5, 10**5
        for right in range(len(li)):
            visited[li[right][1]] += 1
            if visited[li[right][1]] == 1:
                count += 1
                while count == len(nums):
                    if li[right][0] - li[left][0] < end - start:
                        start, end = li[left][0], li[right][0]
                    visited[li[left][1]] -= 1
                    if visited[li[left][1]] == 0:
                        count -= 1
                    left += 1
        return [start, end]


class Solution3:
    def smallestRange(self, nums):
        rangeLeft, rangeRight = -10 ** 9, 10 ** 9
        maxValue = max(vec[0] for vec in nums)
        priorityQueue = [(vec[0], i, 0) for i, vec in enumerate(nums)]
        heapq.heapify(priorityQueue)

        while True:
            minValue, row, idx = heapq.heappop(priorityQueue)
            if maxValue - minValue < rangeRight - rangeLeft:
                rangeLeft, rangeRight = minValue, maxValue
            if idx == len(nums[row]) - 1:
                break
            maxValue = max(maxValue, nums[row][idx + 1])
            heapq.heappush(priorityQueue, (nums[row][idx + 1], row, idx + 1))

        return [rangeLeft, rangeRight]





if __name__ == '__main__':
    s = Solution3()
    # b = [[-5,-4,-3,-2,-1],[1,2,3,4,5]]
    b = [[1,2,3],[1,2,4],[1,2,5]]
    # b = [[1]]
    # b = [[44754,66821,67697,67705,67745,67866,67890,67891,67893],[30112,56984,63713,65107,65868,68327,68422,68452],[-20989,-7893,21756,21919,21952,22027,22029,22103,22104,22131,22146],[-64491,3262,52473,65208,81359,81389,92554,93811,94311,94354,94414,94458,94496,94496,94504,94516,94529,94529,94530],[75112,87519,88776,91285,91338,91354,91360,91380,91381,91383],[23093,58724,69961,76713,76908,80636,80727,83412,83894,84190,84272,84360,84466,84468,84470,84474],[24985,31617,33069,46221,58104,58140,58200,58268,58305,58329,58357,58358,58396,58407,58410,58411,58413]]
    # b = [[11,38,83,84,84,85,88,89,89,92],[28,61,89],[52,77,79,80,81],[21,25,26,26,26,27],[9,83,85,90],[84,85,87],[26,68,70,71],[36,40,41,42,45],[-34,21],[-28,-28,-23,1,13,21,28,37,37,38],[-74,1,2,22,33,35,43,45],[54,96,98,98,99],[43,54,60,65,71,75],[43,46],[50,50,58,67,69],[7,14,15],[78,80,89,89,90],[35,47,63,69,77,92,94]]
    print(s.smallestRange(b))