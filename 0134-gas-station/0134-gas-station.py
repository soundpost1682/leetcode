class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        user, owe, money = None, 0,0
        for i in range(len(gas)):
            money += gas[i] - cost[i]
            if money < 0:
                user, owe, money = None, owe-money, 0
            elif user is None:
                user = i
        
        return user if money >= owe else -1
        
