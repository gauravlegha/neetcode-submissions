class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=sorted(zip(position,speed))
        maxtime=0
        fleets=0
        for pos,sp in reversed(cars):
            t=(target-pos)/sp
            if t>maxtime:
                fleets+=1
                maxtime=t
        return fleets
