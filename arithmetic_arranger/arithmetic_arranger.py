def arithmetic_arranger(problems, answers=False):
  # Checking the number of problems
  if len(problems) > 5:
    return "Error: Too many problems."

  # Splitting the numbers and operators given in the problems parameter. Appending individual values to their respective lists.
  first_num = []
  operator = []
  second_num = []

  for problem in problems:
    each = problem.split()
    first_num.append(each[0])
    operator.append(each[1])
    second_num.append(each[2])

  # Creating empty lists to be used in the final display
  first_line = []
  second_line = []
  third_line = []
  fourth_line = []
  arranged_problems = []

  # Adding the operator to the second line
  for first, second, op in zip(first_num, second_num, operator):
    if len(first) > len(second):
      len_diff = len(first) - len(second)
      second_line.append(op + " " * len_diff + second)
    else:
      second_line.append(op + " " + second)

  # Adding the first line based on the length of the second line
  for first, second in zip(first_num, second_line):
    len_diff = len(second) - len(first)
    first_line.append(" " * len_diff + first)

  # Adding the --- based on the length of the second line
  for second in second_line:
    third_line.append("-" * len(second))

  # Checking for + or - in operator
  if "+" not in operator or "-" not in operator:
    return "Error: Operator must be '+' or '-'."

  # Checking whether the data provided is a digit
  for i in range(len(first_num)):
    if not (first_num[i].isdigit() and second_num[i].isdigit()):
      return "Error: Numbers must only contain digits."

  # Checking the length of the digits and ensuring more than 4 can't be used
  for i in range(len(first_num)):
    if len(first_num[i]) > 4 or len(second_num[i]) > 4:
      return "Error: Numbers cannot be more than four digits."

  # Calculating the final answer and adding the necessary spaces
  for first, second, op, third in zip(first_num, second_num, operator, third_line):
    if op == "+":
      add = str(int(first) + int(second))
      len_diff = len(third) - len(add)
      fourth_line.append(" " * len_diff + add)
    elif op == "-":
      subt = str(int(first) - int(second))
      len_diff = len(third) - len(subt)
      fourth_line.append(" " * len_diff + subt)

  # Putting the values and answer in the final format
  if answers == True:
    arranged_problems = (4 * " ").join(first_line) + "\n" + (
      4 * " ").join(second_line) + "\n" + (4 * " ").join(third_line) + "\n" + (4 * " ").join(fourth_line)
  else:
    arranged_problems = (4 * " ").join(first_line) + "\n" + (4 * " ").join(second_line) + "\n" + (4 * " ").join(third_line)

  return arranged_problems
