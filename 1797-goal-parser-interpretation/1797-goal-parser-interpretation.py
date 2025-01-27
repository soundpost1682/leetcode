class Solution:
    def interpret(self, command: str) -> str:
        tmp1 = command.replace('()', 'o')
        tmp2 = tmp1.replace('(al)', 'al')
        return tmp2
