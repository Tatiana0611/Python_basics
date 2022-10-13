# Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*. 
# приоритет операций стандартный. Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5; 
# Добавить возможность использования скобок, меняющих приоритет операций. Пример: 1+2*3 => 7; (1+2)*3 => 9;

# 1 version


def calc(expression):
    i = 1
    while '*' in expression or '/' in expression:
        if expression[i] == '*':
            expression[i-1] = int(expression[i-1]) * int(expression[i+1])
            del expression[i+1], expression[i]
        elif expression[i] == '/':
            expression[i-1] = int(expression[i-1]) / int(expression[i+1])
            del expression[i+1], expression[i]
        else:
            i +=1

    i = 1
    while '-' in expression or '+' in expression:
        if expression[i] == '-':
            expression[i-1] = int(expression[i-1]) - int(expression[i+1])
            del expression[i+1], expression[i]
        elif expression[i] == '+':
            expression[i-1] = int(expression[i-1]) + int(expression[i+1])
            del expression[i+1], expression[i]
        else:
            i +=1
    print('Выводим из функции результат:', expression)
    return expression

       

expr_str = '1-2*3*4*(2+8*2)/4+9-3+7'
expr_list = list(expr_str)
print(expr_list)

while '(' in expr_list:
    bracket_left = expr_list.index('(')
    bracket_right = expr_list.index(')')
    expr_list = expr_list[:bracket_left] + calc(expr_list[bracket_left + 1 : bracket_right]) + expr_list[bracket_right + 1 :]

print(expr_str + '=>' + str(calc(expr_list)[0]))

# 2 version

# input_str = '1-2*3+2+4/1'
# input_list = list(input_str)
# print(input_list)

# for elem in input_str:
#     if elem.isdigit:

# def split_expression(expr):
#     buffer = ""
#     result = []
#     for digit in expr:
#         if digit.isdigit():
#             buffer += digit
#         else:
#             if buffer != "":
#               result.append(int(buffer))
#             result.append(digit)
#             buffer = ""
#     result.append(int(buffer))
#     return result


# def calculate(expr_list):
#     buffer_list = expr_list.copy()
#     index = 1
#     while "*" in buffer_list or "/" in buffer_list:
#         if buffer_list[index] == "*":
#             buffer_list[index] = buffer_list[index-1]*buffer_list[index+1]
#             buffer_list.pop(index+1)
#             buffer_list.pop(index-1)
#         elif buffer_list[index] == "/":
#             buffer_list[index] = buffer_list[index-1]/buffer_list[index+1]
#             buffer_list.pop(index+1)
#             buffer_list.pop(index-1)
#         else:
#             index += 1
#     index = 1
#     while "+" in buffer_list or "-" in buffer_list:
#         if buffer_list[index] == "+":
#             buffer_list[index] = buffer_list[index-1]+buffer_list[index+1]
#             buffer_list.pop(index+1)
#             buffer_list.pop(index-1)
#         elif buffer_list[index] == "-":
#             buffer_list[index] = buffer_list[index-1]-buffer_list[index+1]
#             buffer_list.pop(index+1)
#             buffer_list.pop(index-1)
#         else:
#             index += 1
#     return buffer_list[0]


# def calculate_with_brackets(expr_list):
#     buffer_list = expr_list.copy()
#     while "(" in buffer_list:
#       start = buffer_list.index("(")
#       end = buffer_list.index(")")
#       buffer_list[start] = calculate(buffer_list[start+1:end])
#       for i in range(end, start, -1):
#         buffer_list.pop(i)
#     return calculate(buffer_list)    
    


# expr = "1-2*3*4*2+8/4+9-3+7"
# expr_bracket = "(1-2)*3*4*2+8/(4+9-3)+7"

# print(eval(expr))
# print(calculate( split_expression(expr)))


# print(eval(expr_bracket))
# print(calculate_with_brackets(split_expression(expr_bracket)))

# 3 version

# input_list = eval(input_str)

# 4 version

# exec(f'print({input_str})')
