class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        outPut = [0]*len(temperatures)
        
        for i in range(len(temperatures) - 1, -1, -1):
            while stack != [] and temperatures[i] >= temperatures[stack[-1]]:
                    stack.pop()
                    
            if stack != [] and temperatures[i] < temperatures[stack[-1]]:
                outPut[i] = stack[-1] - i
                
            stack.append(i)
        
        return outPut
