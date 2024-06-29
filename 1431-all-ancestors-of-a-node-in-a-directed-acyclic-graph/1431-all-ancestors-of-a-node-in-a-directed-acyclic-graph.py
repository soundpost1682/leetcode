class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        answer = [[] for _ in range(n)]
        tmp = defaultdict(list)
        for i, v in edges:
            tmp[v].append(i)

        def deep(node, cur):
            for i in tmp[cur]:
                if i not in answer[node]:
                    deep(node, i)
                    answer[node].append(i)
        
        for i in range(n):
            deep(i, i)
        for k in answer:
            k.sort()
        return answer
