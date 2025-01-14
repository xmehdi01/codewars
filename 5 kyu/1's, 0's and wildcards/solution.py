import itertools
def possibilities(param):
    num_questions = param.count('?')
    possibilities = list(itertools.product('01', repeat=num_questions))
    result=[]
    for possibility in possibilities:
        new_string = list(param)
        p_index=0
        for i  in range(len(new_string)):
            if new_string[i] == '?':
                new_string[i] = possibility[p_index]
                p_index+=1
        result.append(''.join(new_string))
    return result