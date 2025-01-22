def solution(skill, skill_trees):
    n = len(skill_trees)
    answer = n
    
            
    for skill_tree in skill_trees:
        stack = list(skill).copy()
        s = 0
        # 각 원소에 대해
        while s < len(skill_tree) :
            # 선행 스킬 순서에 있다면
            if skill_tree[s] in stack :
                # 첫번째 원소이면
                if stack[0] == skill_tree[s] :
                    stack.pop(0)
                # 아니면(불가능이면)
                else :
                    print('can\'t')
                    answer -= 1
                    s = 30
            s += 1
                    
    
    return answer