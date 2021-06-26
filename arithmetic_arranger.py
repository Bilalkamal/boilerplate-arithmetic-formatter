def check_not_num(item):
    return (item.isdigit() == False) or (item is None)


def arithmetic_arranger(problems, solution=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    operators = ["+", "-"]
    first_operands = []
    second_operands = []
    list_signs = []
    answers = []
    for problem in problems:
        nums = problem.split(" ")
        first, operator, second = nums[0], nums[1], nums[2]
        if operator not in operators:
            return "Error: Operator must be '+' or '-'."
        if check_not_num(first) or check_not_num(second):
            return "Error: Numbers must only contain digits."
        if len(first) > 4 or len(second) > 4:
            return "Error: Numbers cannot be more than four digits."
        first_operands.append(first)
        list_signs.append(operator)
        second_operands.append(second)
        if operator == "-": answers.append(int(first) - int(second))
        if operator == "+": answers.append(int(first) + int(second))
    # Print First line 
    final_str = ""
    for i in range(len(first_operands)):
        length = max([len(first_operands[i]),len(second_operands[i])])
        # print 2 spaces + space difference between both lengths + num 
        final_str += "  " 
        diff = length - len(first_operands[i])
        final_str += diff * " "
        final_str += first_operands[i]
        if i != len(first_operands)-1:
            final_str += "    "
    final_str += "\n"


    # Print second line 
    for i in range(len(second_operands)):
        length = max([len(first_operands[i]),len(second_operands[i])])
        # print 2 spaces + space difference between both lengths + num 
        final_str += list_signs[i] + " " 
        diff = length - len(second_operands[i])
        final_str += diff * " "
        final_str += second_operands[i]
        if i != len(first_operands)-1:
            final_str += "    "
    final_str += "\n"
    # Print third line  
    for i in range(len(second_operands)):
        length = max([len(first_operands[i]),len(second_operands[i])]) + 2
        final_str += length * "-"
        if i != len(first_operands) -1:
            final_str += "    "
    
    
    # Print fourth line   
    if solution:
        final_str += "\n"
        for i in range(len(second_operands)):
            length = max([len(first_operands[i]),len(second_operands[i])]) + 2
            answer = str(answers[i])
            diff = length - len(answer)
            final_str += diff * " "
            final_str += answer
            if i != len(first_operands)-1:
                final_str += "    "
    return final_str

# test = ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]
# result = arithmetic_arranger(test)

# expected = "  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------"
# print(result ==expected)

