class Solution:
    def secondHighest(self, s: str) -> int:
        a = []
        for i in s:
            if i.isdigit():
                a.append(int(i))
        stack = [-1]
        maxs = max(a)
        for i in a:
            if i < maxs:
                while stack and stack[-1] < i:
                    stack.pop()
                    stack.append(i)
        return stack[-1]

if __name__ == '__main__':
    s = Solution()
    t = "asdac456a453dqwe1865s4df645s495q6w1e6qw13e"
    print(s.secondHighest(t))