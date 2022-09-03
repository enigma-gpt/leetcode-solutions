import heapq


class Solution:
    def minRefuelStops_my_version(self, target: int, startFuel: int, stations: list[list[int]]) -> int:

        out = 0
        fuel = startFuel
        current_position = 0
        while current_position + fuel < target:

            if len(stations) <= 0 or stations[0][0] > (current_position + fuel):
                return -1

            station_with_most_fuel = 0
            highest_fuel_level = 0

            while len(stations) and stations[0][0] <= (current_position + fuel):
                station = stations.pop(0)

                if station[1] > highest_fuel_level:
                    station_with_most_fuel = station[0]
                    highest_fuel_level = station[1]

            fuel = fuel - (station_with_most_fuel - current_position) + highest_fuel_level
            current_position = station_with_most_fuel
            out += 1

        return out

    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        pq = []
        tank, stops, prev = startFuel, 0, 0
        for pos, fuel in stations + [[target, 0]]:
            tank -= (pos-prev)
            while tank < 0:
                if not pq: return -1
                tank += -heapq.heappop(pq)
                stops += 1
            heapq.heappush(pq, -fuel)
            prev = pos
        return stops


#print(Solution.minRefuelStops(Solution, 1, 1, []))

#print(Solution.minRefuelStops(Solution, 100, 1, [[10,100]]))

print(Solution.minRefuelStops(Solution, 100, 10, [[10,60],[20,30],[30,30],[60,40]]))

#print(Solution.minRefuelStops(Solution, 100, 50, [[40, 50]]))
