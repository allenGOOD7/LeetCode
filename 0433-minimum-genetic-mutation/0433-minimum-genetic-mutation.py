class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        q = deque()
        q.append([start, 0])

        while q:
            curr_gene, mutation = q.popleft()
            
            if curr_gene == end:
                return mutation
            
            for i in range(8):
                for s in "ACGT":
                    next_gene = curr_gene[:i] + s + curr_gene[i+1:]
                    
                    if next_gene in bank:
                        bank.remove(next_gene)
                        q.append([next_gene, mutation + 1])
        
        return -1        
    