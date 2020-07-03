numbers = [1, 1, 1, 1, 1]
target = 3

def solution(numbers, target):

    
    index = 0
    count = 0


    def dfs(numbers, target, index):

        if(index < len(numbers)) :
            dfs(numbers, target, index + 1)
            numbers[index] = numbers[index] * (-1)
            dfs(numbers, target, index + 1)

        elif(index == len(numbers)) :
            if(sum(numbers) == target) :
               nonlocal count
               count += 1

        return 

    dfs(numbers, target, index)

    return count


answer = solution(numbers, target)

print(answer)