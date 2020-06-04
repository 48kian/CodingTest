begin = "hit"
target = "cog"
#words = ["hot", "dot", "dog", "lot", "log", "cog"]	
words = ["hot", "dot", "dog", "lot", "log"]

'''
구현하는건 어렵지 않았지만..........
카운트를 신경을 못 써서 오래걸렸다
사실 bfs로 푸는게 더 나은 풀이인듯하다.
'''

def solution(begin, target, words):
    answer = 1000
    queue = []
    checked = [False] * len(words)  
    
    '''if target not in words :
        return 0'''

    def dfs(curr):
        nonlocal answer
        nonlocal queue
        nonlocal checked
        succ = False
        count = 0
        
        queue.append([curr,0])
        
        while len(queue) != 0:

            count += 1

            
            print(queue)
            curr = queue[0]
            del queue[0]
            
            for i in range(len(words)):
                if checked[i] == False and aCharDiff(curr[0], words[i]) == True:
                    checked[i] = True                                                   
                    queue.append([words[i],count])
            
            #print(target)
            #print(curr)
            
            if curr[0] == target:
                succ = True
                if  curr[1] < answer:
                    answer = curr[1]
                    print(answer)               
                
        
        if succ == False:
            answer = 0
                    
                    
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
    print(answer)

    return answer

solution(begin, target, words)