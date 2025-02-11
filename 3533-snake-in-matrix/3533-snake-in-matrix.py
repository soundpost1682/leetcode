class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        a,b=0,0
        for i in commands:
            if i == 'UP': a-=1
            elif i == 'DOWN': a+=1
            elif i=='RIGHT':b+=1
            elif i=='LEFT':b-=1
        return (a*n) + b
