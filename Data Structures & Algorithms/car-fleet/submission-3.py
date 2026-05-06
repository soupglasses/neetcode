class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for car_pos, car_speed in sorted(zip(position, speed), reverse=True):
            car_time = (target - car_pos) / car_speed
            if not stack:
                stack.append(car_time)
            elif car_time > stack[-1]:
                stack.append(car_time)
        print(stack)
        return len(stack)