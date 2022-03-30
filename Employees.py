class Employee:
    def __init__(self, id: int, importance: int, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees, id: int) -> int:
        total = 0
        dict = {}
        for ts in employees:
            dict[ts.id] = ts
        return self.circle(dict, id, total)


    def circle(self,dict, id, total):
        succ = []
        total += dict[id].importance
        succ += dict[id].subordinates
        if len(succ) > 0:
            for idx in succ:
                total = self.circle(dict, idx, total)
        else:
            return total
        return total



if __name__ == '__main__':
    s = Solution()
    a = Employee(1,5,[2,3])
    b = Employee(2,3,[])
    c = Employee(3,3,[])
    d = []
    d.append(a)
    d.append(b)
    d.append(c)
    qwe = s.getImportance(d, 1)
    print(qwe)