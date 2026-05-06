class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        count = 0
        current = float('inf')
        for car_pos, car_speed in sorted(zip(position, speed), reverse=True):
            car_time = (target - car_pos) / car_speed
            print(count, current,  car_pos, car_speed, car_time)
            if count == 0 or car_time > current:
                count += 1
                current = car_time
        return count