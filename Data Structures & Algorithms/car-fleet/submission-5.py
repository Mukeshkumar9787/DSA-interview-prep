class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append(Car(position[i], speed[i], target))
        cars.sort(key = lambda x: x.pos, reverse=True)
        stack = []
        for car in cars:
            stack.append(car.time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

class Car:
    def __init__(self, pos, speed, target):
        self.pos = pos
        self.speed = speed
        self.time = (target - pos) / speed