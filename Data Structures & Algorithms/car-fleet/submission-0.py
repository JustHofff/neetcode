class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = [(position[i], speed[i]) for i in range(n)]
        cars.sort(reverse=True)

        stack = []

        for i in range(n):
            time = (target - cars[i][0]) / cars[i][1]

            if stack and time <= stack[-1]:
                continue

            stack.append(time)
        
        return len(stack)