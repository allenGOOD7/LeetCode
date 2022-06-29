class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        # [[7,0],[4,4],[7,1],[9,6]]
        # [[9,6],[7,0],[7,1],[4,4]]
        
        # key point：矮的身高不會影響高的
        
        output = []
        
        for person in people:
            output.insert(person[1], person)
        
        return output