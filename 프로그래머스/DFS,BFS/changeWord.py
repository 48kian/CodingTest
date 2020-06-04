def solution(begin, target, words):
    answer = 0
    queue = []
    checked = [False] * len(words)  
    
    def dfs(curr):
        nonlocal answer
        nonlocal queue
        nonlocal checked
        count = 0
        temp = 0
        
        queue.append(curr)
        
        while len(queue) != 0:

            
            print(queue)
            curr = queue[0]
            del queue[0]
            
            for i in range(len(words)):
                if checked[i] == False and aCharDiff(curr, words[i]) == True:
                    checked[i] = True                                                   
                    queue.append(words[i])
            
            print(target)
            print(curr)
            
            if curr == target:
                if  count < answer:
                    answer = temp
                    print(213123123)
                    print(answer)               
                
            count += 1
                    
                    
    def aCharDiff(curr, comp):
        ccount = 0
        
        for i in range(len(comp)):
            if curr[i] == comp[i]:
                continue
            else:
                ccount += 1
        
        if ccount == 1:
            return True
        else:
            return False
        
    dfs(begin)
    
    return answer