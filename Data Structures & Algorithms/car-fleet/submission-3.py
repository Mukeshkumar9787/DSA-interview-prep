class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            pairs.append([position[i], time])
        pairs.sort(reverse=True)
        stack = []
        for _, time in pairs:
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)