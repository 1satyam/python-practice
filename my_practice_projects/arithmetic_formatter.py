def arithmetic_arranger(problems,show_answer=False):
    #return error when problems>5
    if len(problems)>5:
        return 'Error: Too many problems.'
    output=[]
    for problem in problems:
        #to split every problem when there is a space
        values=problem.split()

        #return error if there is other operator than + or -
        if values[1] not in ('+','-'):
            return "Error: Operator must be '+' or '-'."
        
        try:
            value1=int(values[0])
            value2=int(values[2])
        except ValueError:
            return 'Error: Numbers must only contain digits.'
        if len(values[0])>4 or len(values[2])>4:
            return 'Error: Numbers cannot be more than four digits.'
        
        longest_len=max(len(values[0]),len(values[2]))
        width=longest_len +2
        l1=f'{value1:>{width}}'
        l2=f'{values[1]}{values[2]:>{width-1}}'
        dash='-'*width
        try:
            output[0]+=(' '*4)+l1
        except:
            output.append(l1)
        try:
            output[1]+=(' '*4)+l2
        except:
            output.append(l2)
        try:
            output[2]+=(' '*4)+dash
        except:
            output.append(dash)

        arranged_problem=f"{output[0]}\n{output[1]}\n{output[2]}"
        #when show_answer is TRUE the calculation is executed
        if show_answer:
            if values[1]=='+':
                ans=int(values[0])+int(values[2])
            else:
                ans=int(values[0])-int(values[2])
            l4=f"{str(ans):>{width}}"
            try:
               output[3]+=(' '*4)+l4
            except:
               output.append(l4)
    if show_answer:
        return f'{arranged_problem}\n{output[3]}'            
    return arranged_problem


#print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')
